n = int(input())
height_bus = 437
most = list(map(int, input().split()))
for i in range(n):
    if height_bus >= most[i]:
        print('Crash', i + 1)
        break
else:
    print('No crash')