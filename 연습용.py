while 1==1 :
    t = list(map(int, input().split()))
    if t[0]>t[1] :
        print('Yes')
    elif t[0]==0 and t[1]==0 :
        break
    else:
        print('No')