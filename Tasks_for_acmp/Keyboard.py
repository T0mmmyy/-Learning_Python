keyboard = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
n = input()
i = keyboard.index(n)
if keyboard[i] == keyboard[-1]:
    print(keyboard[0])
else:
    print(keyboard[i + 1])