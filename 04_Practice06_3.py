a=int(input('자판기에 얼마를 넣을까요? >>>> '))
i=1
while a>300:
    a=a-300
    print(f'커피 {i}잔에, 잔돈{a}원')
    i+=1