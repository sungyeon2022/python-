a=int(input('몇 개의 과일을 보관할까요? >>> '))
k=list()
for i in range(1,a+1):
    k.append(input(f"{i}번째 과일을 입력하세요 >>>"))
print(f"입력받은 과일들은 {k}입니다.")