i = int(input())
cot = 0
a = []
while cot < i:
    n, m = map(int, input().split())
    print(19 * m + (n + 239) * (n + 366) // 2)
    cot += 1