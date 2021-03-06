from .ZerotierBootstrap import ZTBootstrap
from jumpscale import j
JSBASE = j.application.jsbase_get_class()


class ZerotierBootstrapFactory(JSBASE):
    def __init__(self):
        self.__jslocation__ = "j.sal_zos.zt_bootstrap"
        JSBASE.__init__(self)

    def get(self, zt_token, bootstap_id, grid_id, cidr):
        """
        Get sal for zerotier bootstrap in ZOS
        Returns:
            the sal layer 
        """
        return ZTBootstrap(zt_token, bootstap_id, grid_id, cidr)
