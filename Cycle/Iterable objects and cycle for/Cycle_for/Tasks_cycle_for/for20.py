a = [int(value) for value in input().split()]
r = int(input())
for i in range(len(a)):
    if a[i] == r:
        print(i + 1)
        break
else:
    print('ErrorValue')