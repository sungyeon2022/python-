a,b,c=map(int,(input().split())

if a[0]==a[1] & a[0]==a[2] & a[1]==a[2] :
    re=10000
    print(re+a[0]*1000)
elif a[0]!=a[1] & a[0]!=a[2] & a[1]!=a[2]:
    print(max(a)*100)
else:
    re=1000
    if a[0]==a[1]:
        print(re+a[0]*100)
    elif a[0]==a[2]:
        print(re + a[0] * 100)
    elif a[1]==a[2]:
        print(re+a[1]*100)