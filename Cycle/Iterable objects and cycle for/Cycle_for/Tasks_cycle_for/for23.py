n = input()
d = []
for i in n:
    if i.isdigit() == True:
        d.append(int(i))
print(len(d), sum(d))