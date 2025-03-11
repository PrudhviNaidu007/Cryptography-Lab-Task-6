import socket
import random

def power(base, exp, mod):
    return pow(base, exp, mod)

host = "127.0.0.1"  
port = 5000  

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print("Connected to server!")

data = client.recv(1024).decode()  
P, G, server_public_key = map(int, data.split(','))

private_key = random.randint(2, P-2)
public_key = power(G, private_key, P)

client.send(str(public_key).encode())  

shared_secret = power(server_public_key, private_key, P)
print(f"Shared secret key: {shared_secret}")

client.close()
