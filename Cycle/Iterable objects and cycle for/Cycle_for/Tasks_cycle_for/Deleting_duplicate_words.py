n = input().split()
est = []
nety = []
for i in n:
    if i.lower() not in est:
        est.append(i.lower())
        nety.append(i)
print(*nety)