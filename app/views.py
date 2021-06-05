from flask import render_template
from app import app
from .request import get_sources

#Views
@app.route('/')
def index():
    '''
    Function that returns the index page and its data
    '''
    #getting news
    get_news = get_sources()
    print(get_news)
    title = 'Home - News Site'
    return render_template('index.html', title = title)
