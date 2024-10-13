mesto = input()
x = int(input())
mesto = 1 if mesto == 'Home' else 2
print('Yes' if (x + 1) %  mesto == 0 else 'No')