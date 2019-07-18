a,b=map(int,input().split())
o=list(map(int,input().split()))
for i in range(0,len(o)):
    for j in range(1,len(o)):
        sum=o[i]+o[j]
        if sum==b:
            print("yes")
    break        
else:
    print("no")
