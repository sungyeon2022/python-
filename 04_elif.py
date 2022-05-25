'''
    elif 조건문 :
        실행문 1
        실행문 2

    if문 이후에 나옴
    if문의 조건을 제외한 조건
    if문과 elif에 조건에 모두 적용되지 않는 예외는 else로 처리한다(else는 문장에 필수는 아님)
'''

a=int(input())

if a > 20 :
    print('성인')
elif a >=17 :
    print('고등학생')
elif a >= 14 :
    print('중학생')
elif a >= 8 :
    print("초등학생")
else:
    print('미취학 아동')