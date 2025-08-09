#Check if the server’s TCP port is reachable - "socket" -  Low-level networking module to work with TCP/UDP connections directly. works at layer 4 (network layer).
#If reachable, send an HTTP GET request to the /health endpoint - "requests" - High-level HTTP library used to send and receive data over the web. works at layer 7(application layer).

import socket
import requests

#Check if the server’s TCP/UDP port is reachable 

def check_port(host, port, timeout):
    try:
        with socket.create_connection((host, port), timeout=5)
        print(f"the {host} on {port} able to reachable.")
        retun True
    except socket.errors()
        print(f"the {host} is not reachable on {port}.")
        return False

#If reachable, send an HTTP GET request to the /health endpoint

def check_http(url, timeout):
    try:
        response = requests.get(url, timeout = 5)
        if response.status_code == 200
            print(f"health request passed")
            return True
        else:
            print(f"HTTP health check failed. Status: {response.status_code}")
            return False

    except requests.exceptions.RequestExceptionsas e:
        print(f" HTTP request failed: {e}")
        return False        

if _name_ == "_main_":
    host = "google.come"
    port = 80
    url = f"http:/{host}/health"  

    if check_port(host, port):
        check_http(url)       
