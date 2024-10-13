a = str(input())
n = list(map(int,a))
count = 0
maxx = 0
for i in range(len(n)):
    if n[i] == 0:
        count += 1
        if maxx < count:
            maxx = count
    else:
        count = 0
print(maxx)