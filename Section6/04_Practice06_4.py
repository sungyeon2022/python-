# a={int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))}
# while len(a)<5:
#     a.add(int(input('0 ~ 9 사이 정수를 입력하세요 >>> ')))
# print(f'모두 입력되었습니다. \n입력된 값은 {a}입니다.',sep=',')
a=list()
while len(a)<5:
    no=int(input('숫자를 입력해 주세요 >>> '))
    if no not in a :
        a.append(no)
print(f'모두 입력되었습니다.\n입력된 값은 {a}입니다.')
