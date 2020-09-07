t=int(input())
for i in range(t):
    a=int(input())
    ar=set(list(map(int,input().split())))
    if 0 in ar:
        print(len(ar)-1)
    else:
        print(len(ar))