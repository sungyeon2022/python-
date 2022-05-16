a,b,c=map(int,(input().split()))
d=int(input())
s=c+d
m=b+s/60
h=a+m/60
print(int(h%24),int(m%60),int(s%60))
