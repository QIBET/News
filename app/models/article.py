class Article:
    '''
    class used to create instances of Articles objects
    '''

    def __init__(self,author,title,description,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.image = urlToImage
        self.publishedAt = publishedAt
        self.content = content