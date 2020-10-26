n = input().split()

for a in range(0, len(n)):
    if a%2 == 1 and abs(int(n[a]))%2 == 1:
        print(f'Index {a} -> {n[a]}')