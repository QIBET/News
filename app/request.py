from app import app
from app import app
import urllib.request,json
from .models import article,source


Article = article.Article
Source = source.Source


#Getting the API key

api_key = app.config['NEWS_API_KEY']

#getting the article_url
source_url = app.config['SOURCE_URL']
articles_url = app.config['ARTICLES_URL']

#Function to get news

def get_sources():
    '''
    Function that gets response to url request
    '''
    get_news_url = source_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results
def process_results(news_list):
    '''
    Function to return a news in form of a list
    Args:
        news_list: a dictionary containing list of data
    returns:
        news_results: a list of news objects
    '''
    news_results = []
    for news_item in news_list:
        identifier = news_item.get("id")
        name = news_item.get("name")
        description = news_item.get("description")
        url = news_item.get("url")

        news_object = Source(identifier,name, description,url)
        news_results.append(news_object)
    
    return news_results

def get_articles(id):
    '''
    Function that gets returns news article
    '''
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_list)

    return articles_results
def process_articles_results(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain article details

    Returns :
        articles_results: A list of source objects
    '''
    article_results = []

    for article in articles_list:
        id = article.get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        image = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        url = article.get('url')

        article_object = Article(id,author,title,description,image,publishedAt,url)
        article_results.append(article_object)

    return article_results





