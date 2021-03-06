from .Node import Node
from jumpscale import j

JSBASE = j.application.jsbase_get_class()


class PrimitivesFactory(JSBASE):
    def __init__(self):
        self.__jslocation__ = "j.sal_zos.node"
        JSBASE.__init__(self)

    @staticmethod
    def get(client):
        """
        Get sal for zos node
        Returns:
            the sal layer
        """
        return Node(client)
