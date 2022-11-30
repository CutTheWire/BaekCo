from sys import stdin,stdout
ip=stdin.readline; op=stdout.writelines

n,m=map(int,ip().split())
n_l=[]
m_l=[]
for _ in range(n):
    n_l.append(ip())
for _ in range(m):
    m_l.append(ip())
intersection=list(set(n_l)&set(m_l))
op(len(intersection))
for i in intersection:
    op(i)