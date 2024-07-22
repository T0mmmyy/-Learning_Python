n = int(input())
prov = 2
while True:
    if n % prov == 0:
        print(prov)
        break
    else:
        prov += 1