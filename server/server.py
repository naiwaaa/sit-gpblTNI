#!/usr/bin/env python3

import socket
from modules import Processor

HOST = ""
PORT = 65432


if __name__ == "__main__":
    processor = Processor()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Socket listening...")
        while True:
            try:
                conn, addr = s.accept()
                with conn:
                    print("Connected by", addr)
                    while True:
                        command = conn.recv(1024).decode()
                        print("Received:", command)
                        if not command or command == "":
                            print("Received: <???>")
                            conn.sendall("<???>".encode())
                        answer = processor.process(command)
                        print("Answer:", answer)
                        conn.sendall(answer.encode())
            except Exception as ex:
                print("ERROR:", ex)
