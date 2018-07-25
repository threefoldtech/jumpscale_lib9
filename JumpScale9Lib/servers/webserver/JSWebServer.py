from js9 import j
# from .JSMainApp import JSMainApp
from gevent.pywsgi import WSGIServer
import sys
import os
from .JSWebLoader import JSWebLoader

JSConfigBase = j.tools.configmanager.base_class_config

TEMPLATE = """
    host = "localhost"
    port = 5050
    port_ssl = 0
    secret_ = ""
    ws_dir = ""
    """


class JSWebServer(JSConfigBase):
    def __init__(self,instance,data={},parent=None,interactive=False,template=None):

        JSConfigBase.__init__(self,instance=instance,data=data,parent=parent,
            template=template or TEMPLATE, interactive=interactive)

        # Set proper instance for j.data.schema

        self.host = self.config.data["host"]
        self.port = int(self.config.data["port"])
        self.port_ssl = int(self.config.data["port_ssl"])
        self.address = '{}:{}'.format(self.host, self.port)

        config_path = j.sal.fs.joinPaths(self.path,"site_config.toml")
        if j.sal.fs.exists(config_path):
            self.site_config = j.data.serializer.toml.load(config_path)
        else:
            self.site_config = {}

        self._inited = False
        self.loader = JSWebLoader()
    
    def init(self):
        
        if self._inited:
            return
        
        self.logger.info("init server")
    
        if self.path not in sys.path:
            sys.path.append(self.path)

        self.http_server = WSGIServer((self.host, self.port), self.app)

        self.app.http_server = self.http_server 

        self.app.server = self

        self.docs_load()

        j.servers.web.latest = self

        # self._sig_handler.append(gevent.signal(signal.SIGINT, self.stop))

        self._inited = False        


    def docs_load(self):
        for item in self.site_config["docsite"]:
            url=item["url"]
            name=item["name"]
            if url is not "":
                path = j.clients.git.getContentPathFromURLorPath(url)
                if not j.sal.fs.exists(path):
                    j.clients.git.pullGitRepo(url=url)
                j.tools.docgenerator.load(pathOrUrl=path,name=name)
        j.tools.docgenerator.process()        

    @property
    def path(self):
        return self.config.data['ws_dir'].rstrip("/")+"/"

    def sslkeys_generate(self):
        res = j.sal.ssl.ca_cert_generate(self.ws_dir)
        if res:
            self.logger.info("generated sslkeys for gedis in %s" % self.ws_dir)
        else:
            self.logger.info('using existing key and cerificate for gedis @ %s' % self.ws_dir)
        key = os.path.join(self.ws_dir, 'ca.key')
        cert = os.path.join(self.ws_dir, 'ca.crt')
        return key, cert

    def start(self, reset=False):
        print("start")

        # self.scaffold(reset=reset)

        self.init()
        print ("Webserver running")
        print (self)
        self.http_server.serve_forever()

    def stop(self):
        """
        stop receiving requests and close the server
        """
        # prevent the signal handler to be called again if
        # more signal are received
        for h in self._sig_handler:
            h.cancel()

        self.logger.info('stopping server')
        self.server.stop()

    def __repr__(self):
        return '<Flask Server http://%s  app_dir=%s)' % (self.address, self.path)

    __str__ = __repr__