import socket
import des

host = socket.gethostname()
port = 5000
server_socket = socket.socket()
server_socket.bind((host, port))

server_socket.listen(2)
print(f"Server listening on {host}:{port}...")

print("Waiting for connection...")
conn, address = server_socket.accept()
print(f"Connection from: {address}\n")

key = "AABB09182736CCDD"
rkb, rk = des.generate_keys(key)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Received from client (encrypted message): {data}")

    data = des.decrypt(data, rkb, rk, is_ascii=True)
    print(f"Decrypted message: {data}\n")

    message = input("Input a message to the client: ")
    
    message = des.encrypt(message, rkb, rk, is_ascii=True)
    print(f"Encrypted message: {message}\n")

    conn.send(message.encode())