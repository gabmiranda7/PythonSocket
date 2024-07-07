import socket

def main():
    HOST = "127.0.0.1"
    PORT = 50000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        message = input("[Cliente] Insira sua mensagem (ou digite 'quit' para sair): ")
        if message.lower() == "quit":
            break
        client.sendall(message.encode())
        data = client.recv(1024)
        print(f"Resposta do servidor: {data.decode()}")

    client.close()

if __name__ == "__main__":
    main()