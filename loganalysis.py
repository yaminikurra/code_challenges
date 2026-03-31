import re
import sys
from datetime import datetime

def print_usernames():
    count =0
    with open("input.txt") as f:
        for x in f:
            if "john" in x:
                count+=1 
        print(count)

def print_ipaddress():
    unique_ips = {}
    ips =[]
    ippattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    with open("access.log") as f:
        for x in f:
            match = ippattern.search(x)
            if match:
                ips.append(match.group())
    
    for ip in ips:
        if ip not in unique_ips:
            unique_ips[ip] = 1
        else:
            unique_ips[ip]+=1
    
    top_ips = dict(sorted(unique_ips.items(),key=lambda item: item[1],reverse=True))
    

    with open("topips.txt", "w") as f:
        for ip,count in top_ips.items():
            f.write(f"{ip} reached {count} times\n")


def status_extract():
    status = int(sys.argv[1]) 
    if status in [200, 401, 403, 404, 500]:
        statuspattern = re.compile(rf"HTTP/1.1\"\ {status}")
        ippattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
        ips = set()
        
        with open("access.log") as f:
            for x in f:
                match = statuspattern.search(x)
                if match:
                    ipmatch = ippattern.search(x)
                    if ipmatch:
                        ips.add(ipmatch.group())
        print(ips)
    else:
        print("invalid status code entered")

def bruteforce_detection():
    ippattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+\"\s(\d{3})")
    timepattern = re.compile(r"\[(.+)\]")
    events = {}
    with open("access.log", "r") as lines:
        for line in lines:
            ipmatch = ippattern.search(line)
            timematch = timepattern.search(line)
            if ipmatch and timematch:
                ip = ipmatch.group(1)
                status = ipmatch.group(2)
                time = datetime.strptime(timematch.group(1), "%d/%b/%Y:%H:%M:%S %z")
                if ip not in events:
                    events[ip] = []
                events[ip].append((time,status))
    
    for ip, event in events.items():
        has_401 = [d for d,s in event if s== "401"]
        has_201 = [d for d,s in event if s== "200"]
        for d in has_401:
            for j in has_201:
                diff = abs((j-d).total_seconds())
                if diff < 300:
                    print(f"the {ip} is suspected for bruteforce attempt")
                    break
            else:
                continue
            break



#print_usernames()
#print_ipaddress()
#status_extract()
bruteforce_detection()