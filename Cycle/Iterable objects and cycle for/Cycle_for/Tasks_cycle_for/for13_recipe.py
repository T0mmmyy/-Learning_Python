n = int(input())
recipe = []
for i in range(n):
    a = input().lower()
    x = a.find('соль')
    if x > 0:
        continue
    else:
        recipe.append(a)
print(*recipe, sep=', ')