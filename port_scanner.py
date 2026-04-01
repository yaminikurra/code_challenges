import socket
import ssl

def scan_ports(target):
    ip = validateip(target)
    if ip:
        for port in range(1,1025):
            sock = socket.socket()
            sock.settimeout(0.3)
            result = sock.connect_ex((ip,port))
            if result ==0:
                print(f"{port} is open")
                banner_grab(ip,port)
            sock.close()

def validateip(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"{target} is not valid please provide valid IP/hostname")
    except Exception as e:
        print(f"something went wrong {e}")

def banner_grab(ip,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip,port))
        if port in [80,8080]:
            sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
        elif port in [443,8443]:
            context = ssl.create_default_context()
            wrapped = context.wrap_socket(sock, server_hostname = ip)
            wrapped.send(b'HEAD / HTTP/1.0\r\n\r\n')
            banner = (wrapped.recv(1024)).decode().split()
            print(banner)
            return
        banner = (sock.recv(1024)).decode().split()
        print(banner)
        sock.close()
    except Exception as e:
        print(f"no banner for port {port}")


scan_ports("scanme.nmap.org")



