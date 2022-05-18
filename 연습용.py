a=list(map(int,(input().split())))
re = 0
if a[0]==a[1] & a[0]==a[2] & a[1]==a[2] :
    re=10000
    print(re+a[0]*1000)
elif a[0]==a[1] & a[0]==a[2] & a[1]==a[2]:
    max=0
    for i in a :
        if max<i:
            max = i
    print(int(max)*100)
else:
    re=1000
    if a[0]==a[1]:
        print(re+a[0]*100)
    elif a[0]==a[2]:
        print(re + a[0] * 100)
    elif a[1]==a[2]:
        print(re+a[1]*100)


