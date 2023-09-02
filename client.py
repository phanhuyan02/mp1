import socket
import threading

# Define a list of server addresses
server_addresses = [
    ('172.22.159.9', 12345),  # Server 1
    ('172.22.95.9', 12345),  # Server 2
    # Add more servers as needed
]

def handle_server(server_address):
    # Create a socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect(server_address)
        print(f"Connected to the server at {server_address}")

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

# Create threads for each server connection
threads = []
for server_address in server_addresses:
    thread = threading.Thread(target=handle_server, args=(server_address,))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
