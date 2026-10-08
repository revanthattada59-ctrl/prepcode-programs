l = []
n = int(input())
for _ in range(n):
    a = int(input())
    l.append(a)
print(l[::-1])
print(max(l), min(l))
