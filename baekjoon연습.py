a,b,v =map(int,input().split())
c=0
while True:
    v-=a
    v+=b
    c += 1
    if v<=0:
        break
print(c)