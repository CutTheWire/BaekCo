from sys import stdin 
ip=stdin.readline
n,m=map(int,ip().split())
n_l=set(list(map(int,ip().split())))
m_l=set(list(map(int,ip().split())))
print(len(list(n_l^m_l)))