a=int(input("임의의 양의 정수를 입력하시오 >>>> "))
re=0
for i in range(a,0,-1):
    re+=i
print(f"1부터 {a}사이 모든 정수의 합계는 {re}입니다.")