# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
from js9 import j

from .api_service import ApiService

from .http_client import HTTPClient

JSBASE = j.application.jsbase_get_class()
JSConfigClient = j.tools.configmanager.base_class_config
JSConfigFactory = j.tools.configmanager.base_class_configs
TEMPLATE =  """
base_uri = "https://capacity.threefoldtoken.com"
"""


class Client(JSConfigClient):

    def __init__(self, instance, data={}, parent=None, interactive=False):
        super().__init__(instance=instance, data=data, parent=parent, template=TEMPLATE, interactive=interactive)
        http_client = HTTPClient(self.config.data['base_uri'])
        self.api = ApiService(http_client)
        self.close = http_client.close


class GridCapacityFactory(JSConfigFactory):

    def __init__(self):
        self.__jslocation__ = "j.clients.grid_capacity"
        self.connections = {}
        JSConfigFactory.__init__(self, Client)

    def configure(self, instance, base_uri, interactive=False):
        """
        :param base_uri: Url for grid_capacity api
        :type base_uri: str
        """
        data = {}
        data["base_uri"] = base_uri
        return self.get(instance=instance, data=data, interactive=interactive)