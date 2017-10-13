import requests
from .ays_service import AysService 
from .Repository import Repositories

BASE_URI = "https://localhost:5000"

class Client:
    def __init__(self, base_uri=BASE_URI, jwt=None):
        self._base_url = base_uri
        self._session = requests.Session()
        self._session.headers.update({"Content-Type": "application/json"})
        self._ayscl = AysService(self)
        self.repositories = Repositories(self)
        if jwt:
            self._set_auth_header('Bearer {}'.format(jwt))

    def _set_auth_header(self, val):
        ''' set authorization header value'''
        self._session.headers.update({"Authorization": val})

    def _get_headers(self, headers, content_type):
        if content_type:
            contentheader = {"Content-Type": content_type}
            if headers is None:
                headers = contentheader
            else:
                headers.update(contentheader)
        return headers

    def _handle_data(self, uri, data, headers, params, content_type, method):
        headers = self._get_headers(headers, content_type)
        if self._is_goraml_class(data):
            data = data.as_json()

        if content_type == "multipart/form-data":
            # when content type is multipart/formdata remove the content-type header
            # as requests will set this itself with correct boundary
            headers.pop('Content-Type')
            res = method(uri, files=data, headers=headers, params=params)
        elif data is None:
            res = method(uri, headers=headers, params=params)
        elif type(data) is str:
            res = method(uri, data=data, headers=headers, params=params)
        else:
            res = method(uri, json=data, headers=headers, params=params)
        res.raise_for_status()
        return res

    def _is_goraml_class(self, data):
        # check if a data is go-raml generated class
        # we currently only check the existence
        # of as_json method
        op = getattr(data, "as_json", None)
        if callable(op):
            return True
        return False

    def _get(self, uri, headers, params, content_type):
        headers = self._get_headers(headers, content_type)
        res = self._session.get(uri, headers=headers, params=params)
        res.raise_for_status()
        return res

    def _delete(self, uri, headers, params, content_type):
        headers = self._get_headers(headers, content_type)
        res = self._session.delete(uri, headers=headers, params=params)
        res.raise_for_status()
        return res

    def _post(self, uri, data, headers, params, content_type):
        return self._handle_data(uri, data, headers, params, content_type, self._session.post)

    def _put(self, uri, data, headers, params, content_type):
        return self._handle_data(uri, data, headers, params, content_type, self._session.put)