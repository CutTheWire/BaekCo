def find(s,e):
    global K
    if s == e:return
    m=(s+e)//2;find(s,m);find(m+1,e)
    if K <=e-s+1:J=sorted(I[s:e+1]);print(J[K-1]);exit()
    K -= e-s+1
N,K=map(int,input().split());I=list(map(int,input().split()));find(0, N-1);print(-1)