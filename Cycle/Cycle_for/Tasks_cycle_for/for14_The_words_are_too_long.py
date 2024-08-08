n = int(input())
for i in range(n):
    a = input()
    if len(a) > 10:
        one = a[0]
        last = a[-1]
        a = one + str(len(a)-2) + last
    print(a)