lower_base = "abcdefghijklmnopqrstuvwxyz"
upper_base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = 3
cipher = "khooR khOor"
decode = []

for char in cipher:
    if char.isalpha():
        if char.islower():
            decode.append(lower_base[(lower_base.index(char) - shift) % 26])
        elif char.isupper():
            decode.append(upper_base[(upper_base.index(char) - shift) % 26])
    else:
        decode.append(char)
    
print(''.join(decode))
