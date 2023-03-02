import math

N = int(input())

# for i in range(1,int(math.sqrt(N))+1):
#     print(i*i)


i = 1

while i*i <= N:
    print(i*i)
    i += 1

