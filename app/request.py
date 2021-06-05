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





