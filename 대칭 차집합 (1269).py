from sys import stdin 
ip=stdin.readline
n,m=map(int,ip().split())
n_l=set(map(int,ip().split()))
m_l=set(map(int,ip().split()))
print(len(list(n_l^m_l)))