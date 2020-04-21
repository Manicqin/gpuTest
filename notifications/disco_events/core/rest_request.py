class RestRequest:
    """Stores information about request such as method, ur, additional args"""

    def __init__(self, method: str, url: str, **kwargs):
        """Builds a REST request infomation from which request can be genearted

        Args:
            method (str): specific REST method
            url (str): specific REST url
        """
        self.method = method
        self.url = url
        self.args = kwargs
    
    def __str__(self):  
        return str(self.__class__) + "Rest request: method=%s, url=%s, add_args=%s" % (self.method, self.url, self.args)