# take in the number
n = list(map(int,input().split()))

output = 1

# calculate answer
for i in n:
    for j in range(2,int(i ** 0.5)+1):
        if i % j ==0 and i>2:
            prime = False
            break
    else:
        prime = True
    if prime:
        output *=i


# print answer
print(output)