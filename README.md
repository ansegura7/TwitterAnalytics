# Twitter Analytics
Project where NLP techniques are used to perform analytics on tweets made by an account.

![PCA Plot](https://raw.githubusercontent.com/ansegura7/TwitterAnalytics/master/img/wordcloud.png)

## Dependencies
The project was carried out with the latest version of <a href="https://www.anaconda.com/distribution/" target="_blank" >Anaconda</a> on Windows.

To install this package with conda run one of the following:
``` console
conda install -c conda-forge tweepy
conda install -c conda-forge spacy
conda install -c conda-forge wordcloud
conda install -c conda-forge textblob
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
from datetime import date
from PIL import Image
from collections import Counter
from textblob import TextBlob

# Import NLP libraries
import re
import spacy.lang.es as es
import spacy.lang.en as en
from wordcloud import WordCloud

# Import plot libraries
import matplotlib.pyplot as plt
```

## Documentation
Below, some useful and relevant links to this project:

- <a href="https://realpython.com/twitter-bot-python-tweepy/" target="_blank" >How to Make a Twitter Bot in Python With Tweepy</a>
- <a href="https://textblob.readthedocs.io/en/dev/quickstart.html" target="_blank" >TextBlob Tutorial</a>

## Contributing and Feedback
Any kind of feedback/criticism would be greatly appreciated (algorithm design, documentation, improvement ideas, spelling mistakes, etc...).

## Author
- Created by Andrés Segura Tinoco
- Created on May 24, 2020

## License
This project is licensed under the terms of the MIT license.
