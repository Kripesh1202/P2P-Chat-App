import socket as s
import pickle as pk


class ServerSocket:
    """Create Server Socket"""
    def __init__(self, host_ip='0.0.0.0', port=1202):
        self.client_sock = ""
        self.client_addr = 0
        self.host_sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.host_sock.bind((host_ip, port))
        self.host_sock.listen(5)
    

    def add_connection(self):
        """Function to add client connection"""
        while True:
            print("waiting for connections")
            self.client_sock, self.client_addr = self.host_sock.accept()
            if self.client_sock:
                print("connection established with server by ", self.client_addr)
                return
    

    def recv_data(self):
        """Recv data from server"""
        data = self.client_sock.recv(3555)
        unpick_data = pk.loads(data)
        return unpick_data
    
    def close_server_sock(self):
        """Close server connection"""
<<<<<<< HEAD
<<<<<<< HEAD
        self.host_sock.close()
        print("Server Socket Closed")
=======
        self.host_sock.close()
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
=======
        self.host_sock.close()
        print("Server Socket Closed")
>>>>>>> c71df84 (updated exception errors)
