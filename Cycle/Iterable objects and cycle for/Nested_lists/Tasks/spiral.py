n = int(input())
a = []
for i in range(n):
    a.append([0] * n)
st = 0
count = 1
fi = 0
sh = 0
for i in range(n):
    if sh == 0:
        st += 1
        for j in range(st, n - fi):
            a[i][j] += count
            count += 1
            sh = 1
    elif sh == 1:
        for j in range(st, n - fi):
            count += 1
            a[j][-i] += count
    elif sh == 2:
        for j in range(n + st, n + fi):
            a[i][j] += count
            sh = 2
            st += 1
    else:
        for j in range(n + st, n + fi):
            a[i][j] += count
            st += 1