
import socket
import subprocess

def get_local_ip_address():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

local_ip = get_local_ip_address()
print(local_ip)

subprocess.call("python manage.py runserver 0.0.0.0:8000", shell=True)
