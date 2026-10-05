n=int(input())
for row in range(0,n):
    for col in range(0,n):
        if col<=row:
            print("* ",end =" ")
        else:
            print("  ",end =" ")
    print()
