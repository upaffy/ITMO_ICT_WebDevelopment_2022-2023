import socket
import typing as tp


class Server:
    def __init__(self, protocol_type: str):
        if protocol_type == "UDP":
            self.socket = self.__create_UDP_socket()
        elif protocol_type == "TCP":
            self.socket = self.__create_TCP_socket()

    def __create_TCP_socket(self) -> socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)

        return sock

    def __create_UDP_socket(self):
        sock = socket.socket()
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)

        return sock

    def send_data_to_client(self, client_socket: socket.socket, data: str):
        client_socket.send(data.encode())

    def get_data_from_client(self, client_socket: socket.socket) -> str:
        encoded_data = client_socket.recv(1024)
        data = encoded_data.decode("utf-8")

        return data

    def accept_connection(self) -> (socket, tp.Any):
        return self.socket.accept()
