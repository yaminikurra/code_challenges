# take in the number
n = list(map(int, input().split()))
variable = int(input())

# calculate answer
output = 0
for i in range(len(n)):
    coeff = n[i]*pow(variable,i)
    output+=coeff

# print answer
print(output)