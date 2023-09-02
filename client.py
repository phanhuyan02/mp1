import socket

# Define the server address
server_address = ('127.0.0.1', 12345)

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect(server_address)
    print("Connected to the server")

    # Input a search query from the user
    query = input("Enter a search query: ")

    # Send the query to the server
    client_socket.send(query.encode('utf-8'))

    data_size_str = client_socket.recv(1024).decode('utf-8')
    data_size = int(data_size_str)

    # Send an acknowledgment to the server ('ACK')
    client_socket.send('ACK'.encode('utf-8'))

    # Receive and print the results from the server
    received_data = b""
    while len(received_data) < data_size:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        received_data += chunk

    result = received_data.decode('utf-8')
    print(result)
except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the client socket
    client_socket.close()
