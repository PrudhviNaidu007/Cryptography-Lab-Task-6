import socket
import random

def power(base, exp, mod):
    return pow(base, exp, mod)

host = "127.0.0.1"  
port = 5000  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print("Server is waiting for a connection...")

conn, addr = server.accept()
print(f"Connected to {addr}")

P = int(input("Enter a prime number (P): "))  
G = int(input("Enter a primitive root (G): "))

private_key = random.randint(2, P-2)
public_key = power(G, private_key, P)

conn.send(f"{P},{G},{public_key}".encode())  

client_public_key = int(conn.recv(1024).decode())  

shared_secret = power(client_public_key, private_key, P)
print(f"Shared secret key: {shared_secret}")

conn.close()
server.close()
