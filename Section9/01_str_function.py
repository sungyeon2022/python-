# #유니코드에 해당하는 글자를 뽑는 함수
# print(chr(65))#A
# print(chr(90))#Z
# print(chr(97))#a
# print(chr(122))#z
# print(chr(32))#space
# print(chr(48))#0
# print(chr(57))#9

for i in range(65,91):
    print(f"{chr(i)} - {chr(i+32)}")

#문자를 유니코드값으로 변경
print(ord('A'), ord('a'))