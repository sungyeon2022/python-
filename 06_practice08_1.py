a=10000
while 1==1:
    print(f"현재 {a}원이 있습니다.")
    i=int(input("사용할 금액 입력 >>> "))
    if i>0:
        if i > a:
            print(f"{a-i}원이 부족합니다.")
        else:
            a-=i
    else:
        print("0 이하의 금액은 사용할 수 없습니다.")
    if a==0:
        print(f"현재 {a}원이 있습니다.")
        break