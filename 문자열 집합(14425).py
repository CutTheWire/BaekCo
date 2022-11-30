n,m=map(int,input().split())
main_S=[]
S=[]
sum=0
for _ in range(n):
    main_S.append(input())
for _ in range(m):
    S.append(input())
for i in main_S:
    sum+=S.count(i)
print(sum)