import unittest
from .models import article
from .models import source
Article = article.Article
Source = source.Source

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the article class behaviour
    '''
    def setUp(self):
        '''
        Method to run before test
        '''
        self.new_article = Article("Benard","The palestinian War","Been going on for long","https://mw3.wsj.net/mw5/content/logos/mw_logo_social.png","2021-12-03","Nyatanyau has had his full force felt",)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
    
    if __name__ == '__main__':
     unittest.main()
