import random
Lo=[1,2,3]
nli=[]
c1=0
c2=0
c3=0
for _ in range(30):
    if c1>=10:
        Lo.remove(1)
        c1=0
    elif c2>=10:
        Lo.remove(2)
        c2=0
    elif c3>=10:
        Lo.remove(3)
        c3=0
    n=random.choice(Lo)
    if n==1:
        c1+=1
    elif n==2:
        c2+=1
    else:
        c3+=1
    nli.append(n)
print(nli)