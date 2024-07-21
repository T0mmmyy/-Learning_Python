a = int(input())
b = int(input())
nok = a * b
while b > 0:
    a,b = b,a % b
nok = nok // a
print(nok)