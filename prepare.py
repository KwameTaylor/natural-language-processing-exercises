import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

import acquire

def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', article).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return str