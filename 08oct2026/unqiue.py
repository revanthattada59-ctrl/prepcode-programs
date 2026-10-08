a = input()
l = []
for i in a:
    if i not in l:
        l.append(i)
ma = list(map(ord, l))
print(sum(ma))

