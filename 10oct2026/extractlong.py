a = input()
l = list(map(int, a.split()))
l = [input() for i in range(n)]
ans = [val for val in l if len(val) > 4]
print(ans)
