import socket
import argparse

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 5555  # Port to listen on (non-privileged ports are > 1023)


def main(args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((args.target, args.port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


if _name_ == '_main_':
    parser = argparse.ArgumentParser(description='Serwer TCP')

    parser.add_argument('-t', '--target', default='')
    parser.add_argument('-p', '--port', type=int, default=5555)

    args = parser.parse_args()

    main(args)
