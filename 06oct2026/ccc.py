n = int(input())
for i in range(0, n):
    for j in range(0, n):
        if i == 0 and j <= n // 2:
            print("* ", end=" ")
        elif i <= n // 2 and j == 0:
            print("* ", end=" ")
        elif i == n // 2 and j <= n // 2:
            print("* ", end=" ")
        elif j == n // 2:
            print("* ", end=" ")
        elif i == n - 1 and j >= n // 2:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print()
