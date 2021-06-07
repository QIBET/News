class Article:
    '''
    class used to create instances of Articles objects
    '''

    def __init__(self,id,author,title,description,urlToImage,publishedAt,url):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.image = urlToImage
        self.publishedAt = publishedAt
        self.url = url

class Source:
    '''
    Class to create instances for source objects
    '''
    def __init__(self,id,name, description,url):
            self.id = id
            self.name = name
            self.description = description
            self.url = url