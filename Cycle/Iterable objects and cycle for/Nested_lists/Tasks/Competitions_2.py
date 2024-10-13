n, m = map(int, input().split())
a = []
max_bros = 0
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for x in range(m):
        max_bros_in_str = a[i][x]
        if max_bros_in_str > max_bros:
            max_bros = max_bros_in_str
            c = i
            d = x
print(max_bros)
print(c, d)