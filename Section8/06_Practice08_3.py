k="qwerty"
# c=0
# while c != 5:
#     i=input("비밀번호를 입력하세요 >>> ")
#     c+=1
#     if i==k:
#         print("비밀번호를 맞혔습니다.")
#         break
#     if c==5:
#         print("비밀번호 입력 횟루를 초과했습니다.")
#         break
for i in range(6):
    a = input("비밀번호를 입력하세요 >>> ")
    if a==k:
        print("비밀번호를 맞혔습니다.")
        break
    if i==4:
        print("비밀번호 입력 횟루를 초과했습니다.")
        break
