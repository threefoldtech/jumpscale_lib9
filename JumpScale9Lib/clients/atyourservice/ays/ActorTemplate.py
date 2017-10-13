from requests.exceptions import HTTPError

def _extract_error(resp):
    if isinstance(resp, HTTPError):
        if resp.response.headers['Content-type'] == 'application/json':
            content = resp.response.json()
            return content.get('error', resp.response.text)
        return resp.response.text
    raise resp
    
class ActorTemplates:
    def __init__(self, repository):
        self._repository = repository
        self._ayscl = repository._ayscl

    def list(self, role=None, name=None):
        """
        List all actor templates.

        Returns: list of actor templates
        """
        try:
            resp = self._ayscl.listTemplates(self._repository.model['name'])
        except Exception as e:
            return _extract_error(e)

        ays_templates = resp.json()
        templates = list()
        for template in sorted(ays_templates, key=lambda template: template['name']):
            try:
                ays_template = self._ayscl.getTemplate(template['name'], self._repository.model['name'])
            except Exception as e:
                return _extract_error(e) 
            templates.append(ActorTemplate(self._repository, ays_template.json()))
        return templates

    def get(self, name):
        """
        Get an actor template by name.

        Args:
            name: name of the actor template

        Returns: actor template instance

        Raises: KeyError when no service match the specified arguments.
        """
        for template in self.list():
            if template.model['name'] == name:
                return template
        raise KeyError("Could not find template with name {}".format(role, name))

class ActorTemplate:
    def __init__(self, repository, model):
        self._repository = repository
        self._ayscl = repository._ayscl
        self.model = model

    def __repr__(self):
        return "actor template: %s" % (self.model["name"])

    __str__ = __repr__