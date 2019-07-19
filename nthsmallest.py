j,e=map(int,input().split())
p=list(map(int,input().split()))
f=min(p)
for i in range (e-1):
    f=min(p)
    p.remove(f)
    f=min(p)
print(f)
    
