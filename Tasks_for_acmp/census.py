n = int(input())
man = []
for i in range(n):
    age, pol = map(int, input().split())
    man.append(age if pol == 1 else -1)

print(man.index(max(man)) + 1 if len(man) > 1 and max(man) >= 0 else -1)