from sys import stdin
ip=stdin.readline

n,m=map(int,ip().split())
P={}

for i in range(1,n+1):
    p=ip().rstrip()
    P[i]=p
    P[p]=i

for i in range(m):
    quiz_P=ip().rstrip()
    if quiz_P.isdigit(): #숫자 판별 isdigit()
        print(P[int(quiz_P)])
    else:
        print(P[quiz_P])