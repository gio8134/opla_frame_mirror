import os
import socket

class UdpMirror:
    def __init__(self, port: int, buffer_size: int):
        self.port = port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        self.sock.bind(("0.0.0.0", self.port))
        print(f"UDP server listening on port {self.port}")
        try:
            while True:
                data, addr = self.sock.recvfrom(self.buffer_size)
                message = data.decode(errors="ignore").strip()
                print(f"Received from {addr}: {message}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.sock.close()
            print("Server stopped.")


if __name__ == "__main__":
    # Read environment variables for configuration
    port = int(os.getenv("UDP_PORT", "9999"))
    buffer_size = int(os.getenv("BUFFER_SIZE", "1024"))

    server = UdpMirror(port, buffer_size)
    server.start()
