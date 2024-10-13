n = list(input().lower())
schet = []
for i in n:
    schet.append(n.count(i))
print(max(schet))