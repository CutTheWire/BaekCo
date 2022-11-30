n,m=map(int,input().split())
P=[]
quiz_P=[]
anw_p=[]
for _ in range(n):
    P.append(input())
for _ in range(m):
    quiz_P.append(input())
for i in quiz_P:
    try:
        if type(int(i)) is int:      
            anw_p.append(P[int(i)-1])
    except:
        anw_p.append(P.index(i)+1)
for i in anw_p:
    print(i)