import socket

# sending data
SERVER_IP = "localhost"
SERVER_PORT = 1234

# listening data
LISTEN_PORT = 1234


def help():
    print("""This library was created by Ivan (mixelburg).
     It allows you to easily create server socket and client socket""")


def server():
    """
    Creates a server side socket for you
    :return: client_soc, client_address, listening_sock
    """
    try:
        listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[+] Socket successfully created")
    except socket.error as err:
        print("[!] socket creation failed with error %s" % (err))

    server_address = ('', LISTEN_PORT)
    listening_sock.bind(server_address)
    print("[+] socket binded to %s" % (LISTEN_PORT))

    listening_sock.listen(5)
    print("[+] Waiting for incoming connections\n")

    client_soc, client_address = listening_sock.accept()
    print("[+] Client connected")
    return client_soc, client_address, listening_sock


def client():
    """
    Creates a client side socket for you
    :return: sock
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[+] Socket successfully created")
    except socket.error as err:
        print("[!] socket creation failed with error %s" % (err))

    server_adress = (SERVER_IP, SERVER_PORT)
    sock.connect(server_adress)
    print("[+] Successfully connected\n")

    return sock


def closer(listening_sock, client_soc):
    """
    Closes given sockets
    :param listening_sock:
    :param client_soc:
    """
    listening_sock.close()
    client_soc.close()

