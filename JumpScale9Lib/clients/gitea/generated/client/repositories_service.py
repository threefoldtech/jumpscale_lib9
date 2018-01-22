
from .Repository import Repository
from .api_response import APIResponse
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class RepositoriesService:
    def __init__(self, client):
        self.client = client

    def repoGetByID(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get a repository by id
        It is method for GET /repositories/{id}
        """
        uri = self.client.base_url + "/repositories/" + id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Repository(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)