import unittest
from  app.models import Article,Source


class ArticleTest(unittest.TestCase):
    '''
    Test class to test the article class behaviour
    '''
    def setUp(self):
        '''
        Method to run before test
        '''
        self.new_article = Article("abc-news","Benard","The palestinian War","Been going on for long","https://mw3.wsj.net/mw5/content/logos/mw_logo_social.png","2021-12-03","Nyatanyau has had his full force felt",)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

class SourceTest(unittest.TestCase):
    '''
    Test class to test the source class behaviour
    '''
    def setUp(self):
        '''
        Method to run before test
        '''
        self.new_source = Source("abc-news","ABC News","Your trusted source for breaking news","https://abcnews.go.com")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


