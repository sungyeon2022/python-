a=int(input("숫자입력 >>>> "))
k=[1]
for i in range(2,a//2+1):
    if a%i==0:
        k.append(i)
k.append(a)
print(k)
