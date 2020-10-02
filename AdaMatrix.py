t=int(input())
for tc in range(t):
    n = int(input())
    ar=[]
    for i in range(n):
        ar.append(list(map(int,input().split())))
    j = 1
    m = []
    for i in range(0,n):
        if ar[0][i]==j:
            m.append(0)
        else:
            m.append(1)
        j+=1
    if sum(m)==0:
        print(0)
    else:
        c=0
        for i in range(n-1,0,-1):
            if(m[i]+c)%2!=0:
                c+=1
        print(c)
 
    
