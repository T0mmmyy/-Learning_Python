n, start, finish = map(int, input().split())
if start < finish:
    print(finish - start - 1 if n - finish >= finish - start or n - finish == 0 else n - finish + start - 1)
else:
    start, finish = finish, start
    print(finish - start - 1 if n - finish >= finish - start or n - finish == 0 else n - finish + start - 1)


n, a, b = map(int, input().split())
if a > b:
    a, b = b, a
print(min(b - a - 1, a + n - b - 1))