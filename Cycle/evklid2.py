a = int(input())
b = int(input())
c = 0
while b > 0:
    #c = a % b
    #a = b
    #b = c
    a,b = b,a % b
print(a)