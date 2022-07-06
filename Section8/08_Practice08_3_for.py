re=False
for i in range(5):
    a = input("비밀번호를 입력하세요 >>> ")
    if a=="qwerty":
        print("비밀번호를 맞혔습니다.")
        break
if re==False:
    print("비밀번호 입력 횟루를 초과했습니다.")