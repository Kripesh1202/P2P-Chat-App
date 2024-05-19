import socket as s
import pickle as pk
import time


class ClientSocket:
    """Create Client Socket"""
    def __init__(self):
        self.server_sock = s.socket(s.AF_INET, s.SOCK_STREAM)

    
    def connect_server(self, server_ip, port=None):
        """Connect to server"""
        while True:
            try:
                self.server_sock.connect((server_ip, port))
                print("connected with server")
                break
            except ConnectionRefusedError:
                print('connection refused error')

    def send_data(self, data):
        """Function to serilize and send data through socket"""
        picked_data = pk.dumps(data)
        self.server_sock.send(picked_data)

    def check_reachable(self):
        """Check server reachability"""
        try:
            retry=0
            while True:
                if self.server_sock.sendall(pk.dumps("server reach check")) is None:
                    return True
                retry+=1
                if retry == 5:
                    break
                print("Failed to reach server, retrying again in few seconds")
                time.sleep(5)
        except OSError:
            return False
    
    def close_sock(self):
        """Close server connection"""
        self.server_sock.close()
<<<<<<< HEAD
        print("Client Socket Closed")
=======
>>>>>>> a80bc70172e467c43b5fb15c755f6fb94644041f
