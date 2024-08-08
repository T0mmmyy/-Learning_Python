n = int(input())
for i in range(n):
    a = input().lower()
    x = a.find('рок') + 1
    if x > 0:
        print(i + 1, x)