from logging import DEBUG


class Config:
    '''
    General parent class for configuration
    '''
    GENERAL_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: General parent class for configuration
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: General parent class for configuration
    '''

    DEBUG = True