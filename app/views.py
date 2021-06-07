from flask import render_template,request,redirect,url_for
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
    
   

  
    title = 'Home - News Site'
    return render_template('index.html', title = title, newsList = get_news)

@app.route('/articles/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''

    # title= 'Articles'
    articles = get_articles(id)
    return render_template('article.html',articleList = articles)