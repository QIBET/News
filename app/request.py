from app.news_test import Source
from app import app
import urllib.request,json
from .models import article
from .models import source

Article = article.Article
Source = source.Source


#Getting the API key

api_key = app.config['NEWS_API_KEY']

#getting the article_url
