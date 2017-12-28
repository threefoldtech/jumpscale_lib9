

class OrgService:
    def __init__(self, client):
        self.client = client

    def createOrgRepo(self, data, org, headers=None, query_params=None, content_type="application/json"):
        """
        Create a repository in an organization
        It is method for POST /org/{org}/repos
        """
        uri = self.client.base_url + "/org/" + org + "/repos"
        return self.client.post(uri, data, headers, query_params, content_type)
