n,k=map(int,input().split())
l=list(map(int,input().split()))
t=[]
t=l[-k:]
del l[-k:]
s=t+l
print(*s)
