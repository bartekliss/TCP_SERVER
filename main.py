import socket
import argparse

def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Serwer nasłuchuje na {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Połączono z {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Odebrano: {data.decode()}")
                conn.sendall(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Serwer TCP')
    parser.add_argument('-t', '--target', default='0.0.0.0', help='Adres, na którym serwer ma nasłuchiwać')
    parser.add_argument('-p', '--port', type=int, default=5555, help='Port, na którym serwer ma nasłuchiwać')
    args = parser.parse_args()

    run_server(args.target, args.port)
