n = int(input())
a, b, c = map(int, input().split())
mat = []
for i in range(n):
    mat.append([0] * n)
for i in range(n):
    for j in range(n):
        if i != j:
            mat[i][j] += b
        else:
            mat[i][j] += c
            for x in range(j + 1, n):
                mat[i][x] += a
            break
for y in mat:
    print(*y)