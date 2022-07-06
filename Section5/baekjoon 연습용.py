a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

d=a[0]**2+a[1]**2+b[0]**2+b[1]**2
e=b[0]**2+b[1]**2+c[0]**2+c[1]**2
f=a[0]**2+a[1]**2+c[0]**2+c[1]**2

if d+e==f :
