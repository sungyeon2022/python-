a=1
while a<=9 :
    i = 1
    while i<=9 :
        print(f'{a}X{i}={a * i}')
        i += 1
    a+=1
#구구단이 a*b일 때 b를 1차 반복문 안에서 초기화 해주어야함**