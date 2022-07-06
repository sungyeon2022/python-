a=float(input('국어 점수를 입력하세요 >>> '))
b=float(input('영어 점수를 입력하세요 >>> '))
c=float(input('수학 점수를 입력하세요 >>> '))
result = (a+b+c)/3
print('평균은',result,'점이고,','결과는','합격입니다.' if result >= 80 else '불합격입니다.')