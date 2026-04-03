import socket

def subdomain_enum(hostname):
    with open("wordlist.txt","r") as lines:
        for line in lines:
            subname = f"{line.strip()}.{hostname}"
            try:
             ip = socket.gethostbyname(subname)
             print(f"valid domain {subname}")
            except Exception as e:
               continue
               
subdomain_enum("google.com")       
             
