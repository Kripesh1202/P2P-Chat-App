import socket as s
import pickle as pk


ip_addr = '127.0.0.1'
port = 1201

#def connect_server(ip_addr, port):
server_sock = s.socket(s.AF_INET, s.SOCK_STREAM)
server_sock.connect((ip_addr,port))
#return server_sock


def send_data(server_sock, data):
    pickled_data = pk.dumps(data)
    server_sock.send(pickled_data)


def recv_data(server_sock):
    p_recv_data = server_sock.recv(1024)
    up_data = pk.loads(p_recv_data)
    return up_data

if __name__ == '__main__':
    #connect_server('127.0.0.1', 1201)

    while True:
        user_input = str(input("Enter your msg: "))
        send_data(server_sock=server_sock, data=user_input)
        print(recv_data(server_sock= server_sock))

