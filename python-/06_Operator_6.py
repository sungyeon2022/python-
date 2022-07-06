#시퀸스 연산자
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# lst3 = lst1 + lst2
# print(lst3)

str1 = 'Hello'
str2 = ' World!'
# str3 = str1 + str2
# str3 += '!!!!!!!'
# print(str3)

#------------------------------
#print('a'*3) #곱하기 정수만큼 반복
# print(str1*3) #문자열이나 리스트의 곱셈은 반복 명령임
#----------------------------------

#맵버쉽 연산자

#in, not in
lst1=[2,3,4,5,6,7,8,9,]
print(10 in lst1)
print(10 not in lst1)
print('e' in str1)
print('e' not in str1)

#삼항 연산자 조건식 결과 값 True일때와 False일때 나타낼 값을 표현한 식
#?
#(조건식의 결과가 참일때 나타낼 연산식) if 조건식 else (조건식 결과가 거짓일때 나타낼 연산식)

n = 10

msg = "짝수" if n%2==0 else "홀수"

print(msg)