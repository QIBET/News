from flask import render_template
from app import app
from .request import get_sources,get_articles

#Views
@app.route('/')
def index():
    '''
    Function that returns the index page and its data
    '''
    #getting news
    get_news = get_sources()
    getArticles = get_articles('source_id')
  
    title = 'Home - News Site'
    return render_template('index.html', title = title, newsList = get_news, articles_list = getArticles )
