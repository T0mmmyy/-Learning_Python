import random
n = int(input())
# met = []
# for i in range(n):
#     met.append(random.randint(-100, 100))
# count = [0] * 201
# for i in met:
#     count[i + 100] += 1
# for i in range(201):
#     if count[i] > 0:
#         print(i - 100)
met = list(map(int, input().split()))
schet = [0] * 202
for i in met:
    schet[i + 101] += i + 101
for i in range(202):
    if schet[i] > 0:
        print(schet[i] - 101)