str=input()
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sc=0
bc=0
for i in str:
    if i in a:
        sc=sc+1
    else:
        bc=bc+1
print(bc)
print(sc)
