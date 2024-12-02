import random
from collections import Counter
from datetime import datetime


def generate_log_line():
    
    ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    
    date = datetime.now().strftime('%d/%b/%Y:%H:%M:%S +0000')
    
    
    request_method = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
    request_url = random.choice(['/home', '/about', '/contact', '/products'])
    request = f'"{request_method} {request_url} HTTP/1.1"'
    
    
    status_code = random.choice([200, 204, 500])
    
    
    bytes_sent = random.randint(100, 5000)
    
    
    return f'{ip_address} - - [{date}] {request} {status_code} {bytes_sent}\n'


log_file_name = 'server.log'

with open(log_file_name, 'w') as file:
    for _ in range(100):  
        file.write(generate_log_line())


with open(log_file_name, 'r') as file:
    log_lines = file.readlines()


status_codes = {200: 0, 204: 0, 500: 0}
ip_addresses = []

for line in log_lines:
    
    status_code = int(line.split()[8])
    
    
    if status_code in status_codes:
        status_codes[status_code] += 1
    
    
    ip_address = line.split()[0]
    ip_addresses.append(ip_address)


ip_counts = Counter(ip_addresses)
most_common_ips = ip_counts.most_common(3)


summary_file_name = 'summary_report.txt'

with open(summary_file_name, 'w') as file:
    
    file.write(f"Requests with status code 200: {status_codes[200]}\n")
    file.write(f"Requests with status code 204: {status_codes[204]}\n")
    file.write(f"Requests with status code 500: {status_codes[500]}\n")
    
    
    file.write("\nTop 3 IP addresses:\n")
    for ip, count in most_common_ips:
        file.write(f"{ip}: {count} requests\n")
    
    
    total_requests = len(log_lines)
    file.write(f"\nTotal requests: {total_requests}\n")

print(f"Summary report has been created in {summary_file_name}.")
