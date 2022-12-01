from sys import stdin 
ip=stdin.readline

def S():
    global n
    word=set()
    for i in range(len(n)):
        for j in range(i,len(n)):
            word.add(n[i:j+1])
    return len(word)

n=ip().rstrip()
print(S())