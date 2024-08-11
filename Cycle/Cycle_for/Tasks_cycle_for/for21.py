a = list(map(int, input().split()))
s = 9999
for i in a:
    if i < s and i > 0:
        s = i
if s == 9999:
    print('Empty')
else:
    print(s)