a=int(input())
b=int(input())
c=int(input())

# if a>=b and a>=c:
#     print(f'가장 큰 수는 {a}입니다.')
# elif b>=a and b>=c:
#     print(f'가장 큰 수는 {b}입니다.')
# elif c>=a and c>=b:
#     print(f'가장 큰 수는 {c}입니다.')
#
# #파이썬은 and를 &가 아닌 키워드를 이용한다.
#
# print(f'가장 큰 수는 {max(a,b,c)}입니다.')

# re=0
# if a>b:
#     re=a
# else:
#     re=b
# if re<c:
#     re=c
# print(re)
re=0
re = a if a>b else re
re = c if c>re else re
print(f'가장 큰 수는 {re}입니다.')



