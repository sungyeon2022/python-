a=int(input())
# c=[1,a]
# k=[]
# for i in range(1,a+1):
#     if a%i==0:
#         k.append(i)
# if c==k:
#     print("입력하신 숫자는 소수 입니다.")
# else:
#     print("입력하신 숫자는 소수가 아닙니다.")
if a>2:
    for i in range(2,a):
        if a%i==0:
            print("입력하신 숫자는 소수가 아닙니다.")
            break
    if i+1==a:
        print("입력하신 숫자는 소수입니다.")
elif a==2:
    print("입력하신 숫자는 소수입니다.")
else :
    print("입력하신 숫자는 소수가 아닙니다.")