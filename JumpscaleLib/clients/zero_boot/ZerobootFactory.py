import os

from jumpscale import j

from .ZerobootClient import zero_bootClient
JSConfigFactoryBase = j.tools.configmanager.base_class_configs


class ZerobootFactory(JSConfigFactoryBase):

    def __init__(self):
        self.__jslocation__ = "j.clients.zboot"
        JSConfigFactoryBase.__init__(self, zero_bootClient)
