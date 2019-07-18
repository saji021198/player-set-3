a=int(input())
for i in range(1,a):
    if(a%i==0):
        c=a//i
        if(c%2!=0):
            break
print(i)
