
from . import
from .Organization import Organization
from .Team import Team
from .api_response import APIResponse
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class OrgsService:
    def __init__(self, client):
        self.client = client

    def orgDeleteHook(self, id, org, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a hook
        It is method for DELETE /orgs/{org}/hooks/{id}
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgGetHook(self, id, org, headers=None, query_params=None, content_type="application/json"):
        """
        Get a hook
        It is method for GET /orgs/{org}/hooks/{id}
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks/" + id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgEditHook(self, data, id, org, headers=None, query_params=None, content_type="application/json"):
        """
        Update a hook
        It is method for PATCH /orgs/{org}/hooks/{id}
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks/" + id
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgListHooks(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's webhooks
        It is method for GET /orgs/{org}/hooks
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgCreateHook(self, data, org, headers=None, query_params=None, content_type="application/json"):
        """
        Create a hook
        It is method for POST /orgs/{org}/hooks
        """
        uri = self.client.base_url + "/orgs/" + org + "/hooks"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgDeleteMember(self, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Remove a member from an organization
        It is method for DELETE /orgs/{org}/members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/members/" + username
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgIsMember(self, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Check if a user is a member of an organization
        It is method for GET /orgs/{org}/members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/members/" + username
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgListMembers(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's members
        It is method for GET /orgs/{org}/members
        """
        uri = self.client.base_url + "/orgs/" + org + "/members"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgConcealMember(self, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Conceal a user's membership
        It is method for DELETE /orgs/{org}/public_members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/public_members/" + username
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgIsPublicMember(self, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Check if a user is a public member of an organization
        It is method for GET /orgs/{org}/public_members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/public_members/" + username
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgPublicizeMember(self, data, username, org, headers=None, query_params=None, content_type="application/json"):
        """
        Publicize a user's membership
        It is method for PUT /orgs/{org}/public_members/{username}
        """
        uri = self.client.base_url + "/orgs/" + org + "/public_members/" + username
        return self.client.put(uri, data, headers, query_params, content_type)

    def orgListPublicMembers(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's public members
        It is method for GET /orgs/{org}/public_members
        """
        uri = self.client.base_url + "/orgs/" + org + "/public_members"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgListRepos(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's repos
        It is method for GET /orgs/{org}/repos
        """
        uri = self.client.base_url + "/orgs/" + org + "/repos"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgListTeams(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        List an organization's teams
        It is method for GET /orgs/{org}/teams
        """
        uri = self.client.base_url + "/orgs/" + org + "/teams"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append((elem))
                return APIResponse(data=resps, response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgCreateTeam(self, data, org, headers=None, query_params=None, content_type="application/json"):
        """
        Create a team
        It is method for POST /orgs/{org}/teams
        """
        uri = self.client.base_url + "/orgs/" + org + "/teams"
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 201:
                return APIResponse(data=Team(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgGet(self, org, headers=None, query_params=None, content_type="application/json"):
        """
        Get an organization
        It is method for GET /orgs/{org}
        """
        uri = self.client.base_url + "/orgs/" + org
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Organization(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def orgEdit(self, data, org, headers=None, query_params=None, content_type="application/json"):
        """
        Edit an organization
        It is method for PATCH /orgs/{org}
        """
        uri = self.client.base_url + "/orgs/" + org
        resp = self.client.patch(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return APIResponse(data=Organization(resp.json()), response=resp)

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)
