import os


from Jumpscale import j
from .OauthInstance import OauthClient

JSConfigFactory = j.tools.configmanager.JSBaseClassConfigs


class OauthFactory(JSConfigFactory):

    def __init__(self):
        self.__jslocation__ = "j.clients.oauth"
        JSConfigFactory.__init__(self, OauthClient)
