from app import app
from app import app
import urllib.request,json
from .models import article
from .models import source

Article = article.Article
Source = source.Source


#Getting the API key

api_key = app.config['NEWS_API_KEY']

#getting the article_url
source_url = app.config['SOURCE_URL']
articles_url = app.config['ARTICLES_URL']