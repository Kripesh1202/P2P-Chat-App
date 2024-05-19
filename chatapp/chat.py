from .core import server_socket as ss
from .core import client_socket as cs
from .util import base as b


class Chatapp:
    """Class with functions sent and recv msg"""
    def __init__(self):
        self.conf_data = b.ConfigFile().get_all_config()
        self.server_obj = ss.ServerSocket(host_ip=self.conf_data['SELF']['IP'], port=1202)
        self.client_obj = cs.ClientSocket()

    def init_server(self):
        """Initialize server to start receive messages"""
        self.server_obj.add_connection()

    def init_client(self):
        """Initialize client to start sending messages"""
        self.client_obj.connect_server(server_ip=self.conf_data['PARTNER']['IP'], port=1202)

    def return_server_obj(self):
        """Return server socket"""
        return self.server_obj

    def return_client_obj(self):
        """Return client socket"""
        return self.client_obj
