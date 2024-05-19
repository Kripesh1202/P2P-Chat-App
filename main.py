import src.server as s
import src.client as c
import threading

def user_input():
    client_sock, ip_addr = serv.create_server()
    server_sock = clie.connect_server('127.0.0.1', 1201)

    while True:
        user_input = str(input("Enter your msg: "))

        client_sock.send_data(user_input)


