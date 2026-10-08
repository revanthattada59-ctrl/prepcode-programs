l = list()
n=int(input())
for i in range(n):
    a=int(input())
    l.append(a)
ans = []
for val in l:
    if l.count(val) == 1 :
        ans.append(val)
print(ans)
