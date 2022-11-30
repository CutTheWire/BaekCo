n,m=map(int,input().split())
n_l=set()
m_l=set()
for _ in range(n):
    n_l.add(input())
for _ in range(m):
    m_l.add(input())
inter=sorted(list(n_l&m_l))
print(len(inter))
print(*inter, sep="\n")