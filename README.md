# Twitter Analytics
Web Mining project in which descriptive statistics and NLP techniques are used to analyze the behavior of a Twitter account (my personal one) and the content of their respective tweets.

![WordCloud](https://raw.githubusercontent.com/ansegura7/TwitterAnalytics/master/img/wordcloud.png)

## Data
All tweets collected from a specific account using the <a href="https://developer.twitter.com/en" target="_blank" >Twitter API</a>.

## Performed Analysis
1. <a href="https://ansegura7.github.io/TwitterAnalytics/analysis/AccountAnalytics.html" >Twitter Account Analytics</a>
2. <a href="https://github.com/ansegura7/TwitterAnalytics/tree/master/etl">Store last tweets in MongoDB</a>

In the following <a href="https://github.com/ansegura7/TwitterAnalytics/tree/master/analysis" target="_blank">folder</a> you can see the results of the previous analyzes.

## Dependencies
The project was carried out with the latest version of <a href="https://www.anaconda.com/distribution/" target="_blank" >Anaconda</a> on Windows.

To install this package with conda run one of the following:
``` console
to create the virtual environment:

conda env create -f twitter-analytics-env.yml

to activate it, then run:

conda activate twitter-analytics-env
```

The specific Python 3.7.x libraries used are:

``` python
# Import util libraries
import tweepy
import random
import numpy as np
import pandas as pd
import yaml
import warnings
import calendar
import time
from datetime import date
from PIL import Image
from collections import Counter

# Import NLP libraries
import re
import spacy.lang.es as es
import spacy.lang.en as en
from textblob import TextBlob
from wordcloud import WordCloud

# Import plot libraries
import matplotlib.pyplot as plt

# Save tweets into MongoDB
from pymongo import MongoClient
from requests.exceptions import Timeout, SSLError, ConnectionError
from requests.packages.urllib3.exceptions import ReadTimeoutError, ProtocolError
```

## Documentation
Below, some useful and relevant links to this project:

- <a href="https://docs.tweepy.org/en/latest/" target="_blank">Tweepy Documentation</a>
- <a href="https://realpython.com/twitter-bot-python-tweepy/" target="_blank" >How to Make a Twitter Bot in Python With Tweepy</a>
- <a href="https://textblob.readthedocs.io/en/dev/quickstart.html" target="_blank" >TextBlob Tutorial</a>

## Contributing and Feedback
Any kind of feedback/suggestions would be greatly appreciated (algorithm design, documentation, improvement ideas, spelling mistakes, etc...). If you want to make a contribution to the course you can do it through a PR.

## Author
- Created by Andrés Segura-Tinoco
- Created on May 24, 2020
- Updated on Aug 16, 2021

## License
This project is licensed under the terms of the <a href="https://github.com/ansegura7/TwitterAnalytics/blob/master/LICENSE">MIT license</a>.
