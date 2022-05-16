a=int(input())
b=1
cou=0
while b <= a:
    if a-b<a:
        a = a - b
        b = b + 1
        cou = cou + 1

print(cou)