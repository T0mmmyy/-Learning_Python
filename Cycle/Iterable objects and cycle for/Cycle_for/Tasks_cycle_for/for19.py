s = input()
pred = input()
for i in pred.split():
    if s in i.lower():
        print(i)