n, m = map(int, input().split())
if n < m:
    a = [i**2 for i in range(n, m + 1)]
    print(a)
else:
    a = [i**3 for i in range(n, m - 1, -1)]
    print(a)