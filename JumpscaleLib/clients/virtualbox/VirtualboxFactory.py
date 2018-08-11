from jumpscale import j

JSConfigBase = j.tools.configmanager.base_class_configs

from .VirtualboxClient import VirtualboxClient

class VirtualboxFactory(JSConfigBase):

    def __init__(self):
        self.__jslocation__ = "j.clients.virtualbox"
        JSConfigBase.__init__(self, VirtualboxClient)

    @property
    def client(self):
        return self.get("default",interactive=False)

    # def client_get(self,zerotiernetwork):
    #     return self.get("test",data={"zerotiernetwork":zerotiernetwork})

    def test(self, instance="test", reset=True):
        """
        js_shell 'j.clients.virtualbox.test()'
        """
    
        cl = j.clients.virtualbox.client
        #TODO: check VM is stopped, if not do so
        #TODO: check that VM is there, if not do not try to delete
        cl.reset_all()
        vm = cl.zos_create(name="test", reset=True, zerotierinstance="")
        vm.start()

        zcl = j.clients.zos.get(instance, data={
            "port": "4444"
        })
        retries = 10
        from time import sleep
        while retries:
            if zcl.is_running():
                print("DONE")
                break
            else:
                self.logger.debug("couldn't connect to the created vm will retry in 30s")
                sleep(30)
            retries -= 1
        else:
            print("something went wrong")


