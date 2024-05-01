import core.server_socket as ss
import core.client_socket as cs

import threading
# import asyncio


def init_server():
    """Initialize server to start receive messages"""
    server_sock = ss.ServerSocket(host_ip='0.0.0.0', port=1202)
    server_sock.add_connection()
    return server_sock

def init_client():
    """Initialize client to start sending messages"""
    client_sock = cs.ClientSocket()
    print("initializing client")
    client_sock.connect_server(server_ip='10.45.96.37', port=1201)
    # if client_sock.check_reachable():
    #     return client_sock
    return client_sock

# serv_sock = init_server()
# client_sock = init_client()

def send_to_server():
    """Send message to server"""
    client_sock = init_client()
    while True:
        retry = 0
        if client_sock == '':
            print("Connecting to server")
            client_sock = init_client()
            retry += 1
            if retry == 10:
                print("Could not able establish connection with server")
                break
            print("can't connect to server trying again in few seconds")
        else:
            if client_sock.check_reachable():
                print("connection established with server")
                while True:
                    # await asyncio.sleep(10)
                    msg = str(input("Message "))
                    if msg == 'bye':
                        print("connection closed")
                        client_sock.close_sock()
                        break
                    client_sock.send_data(data=msg)



def recv_from_client():
    """Recv message from client"""
    serv_sock = ''
    while True:
        if serv_sock:
            # await asyncio.sleep(5)
            print("waiting to recv msg from client")
            recv_msg = serv_sock.recv_data()
            print(recv_msg)
        else:
            print("connecting to client to recv message")
            serv_sock = init_server()


if __name__ == '__main__':
    recv_clie_process = threading.Thread(target=recv_from_client)
    send_serv_process = threading.Thread(target=send_to_server)

    recv_clie_process.start()
    send_serv_process.start()


    send_serv_process.join()
    recv_clie_process.join()     

    # mainloop = asyncio.get_event_loop()
    # mainloop.create_task(send_to_server())
    # mainloop.create_task(recv_from_client())
    # mainloop.run_forever()

    # send_to_server()