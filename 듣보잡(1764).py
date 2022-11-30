from sys import stdin,stdout
ip=stdin.readline
n,m=map(int,ip().split())
n_l=[]
m_l=[]
for _ in range(n):
    n_l.append(ip())
for _ in range(m):
    m_l.append(ip())
intersection=list(set(n_l)&set(m_l))
print(len(intersection))
for i in intersection:
    print(i)