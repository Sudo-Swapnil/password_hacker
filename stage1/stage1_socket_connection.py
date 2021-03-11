import sys
import socket


class PasswordHacker:
    def __init__(self):
        _args = sys.argv
        self.host = _args[1]
        self.port = int(_args[2])
        self.message = _args[3]
        self.client_socket = None
        self.server_response = None
        self.main()

    def create_socket(self):
        _address = (self.host, self.port)
        self.client_socket = socket.socket()
        self.client_socket.connect(_address)

    def socket_send_recv(self):
        _binary_message = self.message.encode()
        self.client_socket.send(_binary_message)
        _response = self.client_socket.recv(1024)
        _response = _response.decode()
        return _response

    def close_socket(self):
        self.client_socket.close()

    def main(self):
        self.create_socket()
        self.server_response = self.socket_send_recv()
        print(self.server_response)
        self.close_socket()


if __name__ == '__main__':
    PasswordHacker()
