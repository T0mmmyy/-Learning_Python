a = str(input())
# n = list(map(int,a))
n = a
print(a)
for i in n:
    op = n.pop()
    if op == i:
        continue
    else:
        print('NO')
        break
else:
    print('YES')












# while len(n) > 0:
#     op =  n.pop()
#     if op
# print(op)