import socket
import subprocess

# Define the host and port for the server
host = '172.19.62.216'
port = 12345

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(4)
print(f"Server listening on {host}:{port}")

while True:
    # Accept a connection from the client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    try:
        # Receive the query from the client
        query = client_socket.recv(4096).decode('utf-8')

        # Simulate a local grep command with -H to display file names
        grep_command = f"grep -H '{query}' log.log"  # Replace with your log file path
        result = subprocess.getoutput(grep_command)

        # Split the result by lines to count matching lines and display file names
        result_lines = result.split('\n')
        num_matching_lines = len(result_lines)

        # Send the number of matching lines and results back to the clien
        response = f"{result}\nNumber of matching lines: {num_matching_lines}"
        # Send the size of the data to the client first
        data_size = len(response.encode('utf-8'))
        client_socket.send(str(data_size).encode('utf-8'))

        # Wait for acknowledgment from the client before sending the data
        acknowledgment = client_socket.recv(1024).decode('utf-8')

        if acknowledgment == 'ACK':
            # Send the data to the client
            client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error processing query: {str(e)}")

    finally:
        client_socket.close()