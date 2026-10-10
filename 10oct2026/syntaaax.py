n = int(input())
l = [int(input()) for i in range(4, 13)]
ans = ["even" if n % 2 == 0 else "odd" for val in l]
print(l)
print(ans)
