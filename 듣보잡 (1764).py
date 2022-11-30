from sys import stdin
ip=stdin.readline
n,m=map(int,ip().split())
n_l=set()
m_l=set()
for _ in range(n):
    n_l.add(ip().rstrip())
for _ in range(m):
    m_l.add(ip().rstrip())
inter=sorted(list(n_l&m_l))
print(len(inter))
print(*inter, sep="\n")