from Jumpscale import j
from .PortalClient import PortalClient

JSConfigBaseFactory = j.tools.configmanager.JSBaseClassConfigs


class PortalClientFactory(JSConfigBaseFactory):

    def __init__(self):
        self.__jslocation__ = "j.clients.portal"
        self._portalClients = {}
        JSConfigBaseFactory.__init__(self, PortalClient)
