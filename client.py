import socket
import des

host = socket.gethostname()
port = 5000
client_socket = socket.socket()
client_socket.connect((host, port))

key = "AABB09182736CCDD"
rkb, rk = des.generate_keys(key)

while True:
    message = input("Input a message to the server: ")
    
    message = des.encrypt(message, rkb, rk, is_ascii=True)
    print(f"Encrypted message: {message}\n")

    client_socket.send(message.encode())

    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Received from server (encrypted message): {data}")

    data = des.decrypt(data, rkb, rk, is_ascii=True)
    print(f"Decrypted message: {data}\n")