a=int(input())
b=int(input())
gcd=1
if a<b:
    l=a
    a=b
    b=l
for i in range(1,b+1):
    if b%i==0 and a%i==0:
        gcd = i
print(gcd)