

class TeamsService:
    def __init__(self, client):
        self.client = client

    def orgAddTeamMember(self, username, id, headers=None, query_params=None, content_type="application/json"):
        """
        Remove a team member
        It is method for DELETE /teams/{id}/members/{username}
        """
        uri = self.client.base_url + "/teams/" + id + "/members/" + username
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgAddTeamMember(self, data, username, id, headers=None, query_params=None, content_type="application/json"):
        """
        Add a team member
        It is method for PUT /teams/{id}/members/{username}
        """
        uri = self.client.base_url + "/teams/" + id + "/members/" + username
        return self.client.put(uri, data, headers, query_params, content_type)

    def orgListTeamMembers(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        List a team's members
        It is method for GET /teams/{id}/members
        """
        uri = self.client.base_url + "/teams/" + id + "/members"
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgAddTeamMember(self, org, repo, id, headers=None, query_params=None, content_type="application/json"):
        """
        This does not delete the repository, it only removes the repository from the team.
        It is method for DELETE /teams/{id}/repos/{org}/{repo}
        """
        uri = self.client.base_url + "/teams/" + id + "/repos/" + org + "/" + repo
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgAddTeamMember(self, data, org, repo, id, headers=None, query_params=None, content_type="application/json"):
        """
        Add a repository to a team
        It is method for PUT /teams/{id}/repos/{org}/{repo}
        """
        uri = self.client.base_url + "/teams/" + id + "/repos/" + org + "/" + repo
        return self.client.put(uri, data, headers, query_params, content_type)

    def orgListTeamRepos(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        List a team's repos
        It is method for GET /teams/{id}/repos
        """
        uri = self.client.base_url + "/teams/" + id + "/repos"
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgDeleteTeam(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete a team
        It is method for DELETE /teams/{id}
        """
        uri = self.client.base_url + "/teams/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def orgGetTeam(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get a team
        It is method for GET /teams/{id}
        """
        uri = self.client.base_url + "/teams/" + id
        return self.client.get(uri, None, headers, query_params, content_type)

    def orgEditTeam(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        Edit a team
        It is method for PATCH /teams/{id}
        """
        uri = self.client.base_url + "/teams/" + id
        return self.client.patch(uri, data, headers, query_params, content_type)
