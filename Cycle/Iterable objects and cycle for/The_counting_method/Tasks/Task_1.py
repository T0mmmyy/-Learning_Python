n = input()
schet = [0] * 10
for i in n:
    schet[int(i)] += 1
for i in range(len(schet)):
    if schet[i] > 0:
        print(i, schet[i])