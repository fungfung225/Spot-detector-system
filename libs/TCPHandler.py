import pickle
import struct
from socket import *

# packet header format: data length(8 bytes)
_HEADER_FMT = "Q"
_HEADER_SIZE = struct.calcsize(_HEADER_FMT)


def get_my_ip():
    return gethostbyname(gethostname())


class TCPHandler:

    def __init__(self, socket_in: socket):
        self.socket = socket_in
        self.recv_buffer = b""

    def connect(self, ip, port):
        self.socket.connect((ip, port))

    def bind(self, ip, port):
        self.socket.bind((ip, port))

    def listen(self):
        self.socket.listen()
        return self.socket.accept()

    def send_str_message(self, msg: str):
        self.socket.sendall(msg.encode())

    def recv_str_message(self, buffer_size: int = 1024):
        return self.socket.recv(buffer_size).decode()

    def send_obj(self, py_obj):
        data = pickle.dumps(py_obj)
        packet = struct.pack(_HEADER_FMT, len(data)) + data
        self.socket.sendall(packet)

    def recv_obj(self):
        while len(self.recv_buffer) < _HEADER_SIZE:
            packet = self.socket.recv(4 * 1024)
            if not packet:
                break
            self.recv_buffer += packet

        data_size = struct.unpack(_HEADER_FMT, self.recv_buffer[:_HEADER_SIZE])[0]
        self.recv_buffer = self.recv_buffer[_HEADER_SIZE:]

        while len(self.recv_buffer) < data_size:
            self.recv_buffer += self.socket.recv(4 * 1024)

        data = self.recv_buffer[:data_size]
        self.recv_buffer = self.recv_buffer[data_size:]
        return pickle.loads(data)

    def disable_blocking(self):
        self.socket.setblocking(False)

    def set_socket_timeout(self, time_out):
        self.socket.settimeout(time_out)

    def close_connection(self):
        self.socket.close()

    def get_my_ip(self):
        return self.socket.getsockname()[0]

    def get_my_port(self):
        return self.socket.getsockname()[1]
