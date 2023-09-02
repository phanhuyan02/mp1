import random
import string

# Define the log file path
log_file_path = 'log.log'
desired_lines = 300000

# Function to generate random log entries
def generate_log_entry():
    timestamp = '2023-09-02 12:00:00'
    log_level = random.choice(['INFO', 'WARNING', 'ERROR'])
    message = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    return f"{timestamp} [{log_level}] {message}\n"

# Create the log file
with open(log_file_path, 'w') as log_file:
    for _ in range(desired_lines):
        log_entry = generate_log_entry()
        log_file.write(log_entry)

print(f"Log file '{log_file_path}' created with approximately {desired_lines} lines.")
