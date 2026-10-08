a=input()
l=[]
vow= "aeiouAEIOU"
for i in a:
    if i not in l and i not in vow:
        l.append(i)
print(l)