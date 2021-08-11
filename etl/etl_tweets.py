# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:55:14 2021

@author: ansegura
"""

# Import libraries
import yaml
import tweepy
from requests.exceptions import Timeout, SSLError, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError
from pymongo import MongoClient

######################
### CORE FUNCTIONS ###
######################

# Util function - Read dict from yaml file
def get_dict_from_yaml(yaml_path):
    result = dict()
    
    with open(yaml_path) as f:
        yaml_file = f.read()
        result = yaml.load(yaml_file, Loader=yaml.FullLoader)
    
    return result

def get_auth():
    # Read twitter bot credentials
    yaml_path = '../code/config/credentials.yml'
    twt_login = get_dict_from_yaml(yaml_path)
    
    # Setup bot credentials
    consumer_key = twt_login['consumer_key']
    consumer_secret = twt_login['consumer_secret']
    access_token = twt_login['access_token']
    access_token_secret = twt_login['access_token_secret']
    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    return auth
    
# Util function - Fetch tweets list from a specific user
# Note: Twitter only allows access to a users most recent 3240 tweets with this method
def get_all_tweets(api, screen_name):
    all_tweets = []
    
    # Make initial request for most recent tweets (200 is the maximum allowed count)
    try:
        new_tweets = api.user_timeline(screen_name = screen_name, count=200, tweet_mode='extended')

        # Save most recent tweets
        all_tweets.extend(new_tweets)

        # Save the id of the oldest tweet less one
        oldest = all_tweets[-1].id - 1

        # Keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:

            # All subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name, count=200, tweet_mode='extended', max_id=oldest)

            # Save most recent tweets
            all_tweets.extend(new_tweets)

            # Update the id of the oldest tweet less one
            oldest = all_tweets[-1].id - 1
    
    except (tweepy.TweepError) as e:
        print('Error 1:', e)
    
    except (Timeout, SSLError, ConnectionError, ReadTimeoutError, ProtocolError) as e:    
        print('Error 2:', e)
        
    # Transform the tweepy tweets into an array that contains the relevant fields of each tweet
    tweet_list = []
    for tweet in all_tweets:
        new_tweet = {
            'id': tweet.id_str,
            'created_at': tweet.created_at,
            'message': tweet.full_text,
            'lang': tweet.lang,
            'hashtags': [ht['text'] for ht in tweet.entities['hashtags']],
            'user_mentions': [mt['screen_name'] for mt in tweet.entities['user_mentions']],
            'retweet_count': tweet.retweet_count,
            'favorite_count': tweet.favorite_count,
            'retweeted': tweet.retweeted,
            'source': tweet.source,
            'display_text_range': tweet.display_text_range
        }
        tweet_list.append(new_tweet)
    
    return tweet_list

# Util function - Upsert documents into MongoDB
def mongodb_upsert_docs(mdb_login, doc_list):
    
    # Login
    client = MongoClient(mdb_login['server'], mdb_login['port'])
    db = client[mdb_login['db']]
    coll = db[mdb_login['collection']]
    total_docs = coll.count_documents({})
    print (coll.name, "has", total_docs, "total documents.")
    
    # Upsert documents
    for doc in doc_list:
        coll.update_one(
            {"id" : doc['id']},
            {"$set": doc},
            upsert=True
        )

#####################
### START PROGRAM ###
#####################
if __name__ == "__main__":
    
    # 1. Create Twitter API object
    auth = get_auth()
    api = tweepy.API(auth)
    api.verify_credentials()
    print(">> Authentication OK")
    
    # Show user account details
    tw_user_name = "@seguraandres7"
    user = api.get_user(screen_name=tw_user_name)
    print(">> User details:")
    print(user.name)
    print(user.description)
    print(user.location)
    print(user.created_at)
    
    # 2. Fetching tweet list from a specific user
    tweet_list = get_all_tweets(api, screen_name=tw_user_name)
    
    # 3. Upsert tweets into MongoDB
    yaml_path = 'config/credentials.yml'
    mdb_login = get_dict_from_yaml(yaml_path)
    mongodb_upsert_docs(mdb_login, tweet_list)
    print('>> tweets upserted:', len(tweet_list))
    
#####################
#### END PROGRAM ####
#####################
