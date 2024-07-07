import socket
import threading

def handle_client(client_socket, client_addr):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Mensagem recebida de {client_addr[0]}:{client_addr[1]}: {data.decode()}")
            client_socket.sendall(b"Mensagem Recebida")
    except ConnectionAbortedError as e:
        print(f"A conexão foi encerrada pelo Cliente.")
    finally:
        client_socket.close()
        print(f"Conexão com {client_addr[0]}:{client_addr[1]} encerrada.")

def main():
    HOST = "127.0.0.1"
    PORT = 50000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Aguardando conexões em {HOST}:{PORT}")

    while True:
        client_socket, client_addr = server.accept()
        print(f"Conexão recebida de {client_addr[0]}:{client_addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_addr))
        client_handler.start()

if __name__ == "__main__":
    main()
