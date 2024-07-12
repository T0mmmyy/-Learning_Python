m = int(input())
man = list(map(int, input().split()))
g = int(input())
girl = list(map(int, input().split()))
man.sort()
girl.sort()
i = 0
j = 0
count = 0
while i < m and j < g:
    if abs(man[i] - girl[j]) <=1:
        count = count + 1
        i = i + 1
        j = j + 1
    elif man[i] < girl[j]:
        i = i + 1
    else:
        j = j + 1
print(count)
