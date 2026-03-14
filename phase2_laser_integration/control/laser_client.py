# control/laser_client.py

import socket
import json


class LaserClient:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port

    def send_coordinate(self, x: float, y: float, z: float = 0):
        """
        C# 레이저 서버로 좌표 전송
        """
        data = {
            "x": float(x),
            "y": float(y),
            "z": float(z)
        }

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                sock.send(json.dumps(data).encode())

        except ConnectionRefusedError:
            print("[LaserClient] C# 서버 연결 실패")