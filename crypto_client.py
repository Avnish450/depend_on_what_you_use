import socket
import ssl


def create_secure_socket(target_url):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_context = ssl._create_unverified_context()
    return ssl_context.wrap_socket(sock)
