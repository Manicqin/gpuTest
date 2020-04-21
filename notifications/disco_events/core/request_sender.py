from .rest_request import RestRequest
import requests

class RequestSender:
    """Sends REST requests."""

    @classmethod
    def send(cls, request: RestRequest):
        """Sends REST request to server
        Args:
            request (RestRequest): information about request
        
        Returns:
            requests.Response: response from server

        Raise:
            ValueError: When try to send invalid request
            HTTPError: When request failed
        """
        if request is None:
            raise ValueError('No request to send')
        
        response = requests.request(method=request.method, url=request.url, **request.args)
        response.raise_for_status()
        return response

    @classmethod
    def get(cls, url: str, params = None, **kwargs):
        """Sends GET request to the server
        Args:
            url (str): Endpoint url
            params (dict,optional): url query parameters

        Returns:
            requests.Response: response from server

        Raise:
            ValueError: When try to send invalid request
            HTTPError: When request failed
        """
        return cls.send(RestRequest('get', url, params=params, **kwargs))

    @classmethod
    def options(cls, url: str, **kwargs):
        """Send OPTIONS request to the server
        Args:
            url (str): Endpoint url

        Returns:
            requests.Response: response from server

        Raise:
            ValueError: When try to send invalid request
            HTTPError: When request failed
        """
        return cls.send(RestRequest('options', url, **kwargs))
    
    @classmethod
    def head(cls, url: str, **kwargs):
        """Send HEAD request to the server
        Args:
            url (str): Endpoint url

        Returns:
            requests.Response: response from server

        Raise:
            ValueError: When try to send invalid request
            HTTPError: When request failed
        """
        return cls.send(RestRequest('head', url, **kwargs))

    @classmethod
    def post(cls, url: str, data = None, json = None, **kwargs):
        """Sends PUT request to the server
        Args:
            url (str): Endpoint url
            data (dict, optional): List of tuples, bytes, or file-like object to send in the body
            json (optional): Json data to send in the body.

        Returns:
            requests.Response: response from server

        Raise:
            ValueError: When try to send invalid request
            HTTPError: When request failed
        """
        return cls.send(RestRequest('post', url, data=data, json=json, **kwargs))

    @classmethod
    def put(cls, url: str, data = None, **kwargs):
        """Sends PUT request to the server
        Args:
            url (str): Endpoint url
            data: (dict, optional): list of tuples, bytes, or file-like object to send in the body

        Returns:
            requests.Response: response from server

        Raise:
            ValueError: When try to send invalid request
            HTTPError: When request failed
        """
        return cls.send(RestRequest('put', url, data=data, **kwargs))

    @classmethod
    def patch(cls, url: str, data = None, **kwargs):
        """Sends PATCH request to the server
        Args:
            url (str): Endpoint url
            data: (dict, optional): list of tuples, bytes, or file-like object to send in the body

        Returns:
            requests.Response: response from server

        Raise:
            ValueError: When try to send invalid request
            HTTPError: When request failed
        """
        return cls.send(RestRequest('patch', url, data=data, **kwargs))

    @classmethod
    def delete(cls, url: str, **kwargs):
        """Sends DELETE request to the server
        Args:
            url (str): Endpoint url

        Returns:
            requests.Response: response from server

        Raise:
            ValueError: When try to send invalid request
            HTTPError: When request failed
        """
        return cls.send(RestRequest('delete', url, **kwargs))