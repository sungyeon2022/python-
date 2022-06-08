minh=[]
maxh=[]
a=int(input())
for i in range(a):
    j=int(input())
    if len(minh)==0 and len(maxh)==0:
        minh.append(j)
        print(max(minh))
    elif len(minh)>len(maxh):
        if max(minh)>j:
            minh.
