a=int(input())
c=list()
while a>0 :
    c.append(int(input()))
    a-=1
    c.sort()
    if len(c)%2==0 :
        print(c[len(c)//2-1])
    else :
        print(c[len(c)//2])