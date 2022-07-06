co=0
a=list(map(int,input().split()))
for i in a:
    if i%3==0 or i%5==0:
        co+=1
print(co)
