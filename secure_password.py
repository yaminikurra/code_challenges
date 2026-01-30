def is_secure_password(password):
    if len(password) < 8 or " " in password :
        return False
    has_upper = False
    has_lower = False
    has_digit = False

    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit
    
password = input()
print("is this password secure: " + str(is_secure_password(password)))
