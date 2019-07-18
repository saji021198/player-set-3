p,q2=map(str,input().split())
q2=int(q2)
for i in range(q2):
    p=p[-1]+p[:-1]
print(p)
