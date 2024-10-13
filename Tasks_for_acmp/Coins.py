n = int(input())
gerb = []
reshka = []
for i in range(n):
    coin = int(input())
    if coin == 0:
        gerb.append(coin)
    else:
        reshka.append(coin)
print(len(gerb) if len(gerb) <= len(reshka) else len(reshka))