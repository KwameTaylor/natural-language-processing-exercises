import numpy as np
import pandas as pd

from requests import get
import re
from bs4 import BeautifulSoup
import os

def get_blog_articles(urls):
    articles = []

    for url in urls:
        # Make request and soup object
        headers = {'User-Agent': 'Codeup Data Science'} 
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # get title and paragraph/content
        title = soup.find('h1').text
        content = soup.find('p').text

        # store articles
        article = {'title': title, 'content': content}
        articles.append(article)
            
    # save as a DataFrame
    df = pd.DataFrame(articles)
    
    return df