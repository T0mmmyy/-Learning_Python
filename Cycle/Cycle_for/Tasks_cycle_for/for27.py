s = input()
stack = []
goor = True
for i in s:
    if i in '([{':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            gorr = False
            break
        open = stack.pop()
        if open == '(' and i == ')':
            continue
        if open == '{' and i == '}':
            continue
        if open == '[' and i == ']':
            continue
        gorr = False
if goor and len(stack) == 0:
    print('YES')
else:
    print('NO')