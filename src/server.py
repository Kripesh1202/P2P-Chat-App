import socket as s
import pickle as pk

def create_server():
    server_sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_sock.bind(('127.0.0.1', 1201))

    server_sock.listen()

    (client_sock, ip_addr) = server_sock.accept()

    return client_sock, ip_addr

def send_data(client_sock, data):
    pickled_data = pk.dumps(data)
    client_sock.send(pickled_data)


def recv_data(client_sock):
    p_recv_data = client_sock.recv(1024)
    up_data = pk.loads(p_recv_data)
    return up_data


if __name__ == '__main__':
    client_sock, ip_addr = create_server()
    while True:
        server_input = str(input("Enter server msg: "))
        send_data(client_sock=client_sock, data=server_input)
        print(recv_data(client_sock=client_sock)) 

