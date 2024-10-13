n = list(map(int, input().split()))
for i in n:
    for x in range(i):
        print('*', end='')
    print()