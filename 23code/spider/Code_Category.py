
class Category(object):
    """docstring for Category"""
    def __init__(self, title=None,href=None):
        super(Category, self).__init__()
        self.title = title
        self.href = href

    def __str__(self):
        return self.title+"@"+self.href

