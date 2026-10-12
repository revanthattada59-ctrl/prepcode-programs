l = [1, 3, 2, 4, 100, 2, 200]
s = set()
s.update(l)
l = sorted(list(s))
count = 1
length = 0
for cur in range(1, len(l)):
    prev = cur - 1
    if l[prev] + 1 == l[cur]:
        count = count + 1
    else:
        count = 1
    length = max(count, length)
print(length)
