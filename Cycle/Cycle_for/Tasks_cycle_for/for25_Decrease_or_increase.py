n = list(map(int, input().split()))
for i in range(len(n) - 1):
    if n[i] < n[i + 1] or n[i] == n[i + 1]:
        pass
    else:
        print('False')
        break
else:
    print('True')