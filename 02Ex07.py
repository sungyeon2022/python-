a=input('비밀번호를 입력하시요 >>>> ')

ch_c=0
num_c=0
sp_c=0
sp_s='!@#$%^^&*()_+=<>?/.,=-'

for ch in a:
    if ch.isalpha():
        ch_c+=1
    elif ch.isnumeric():
        num_c+=1
    elif ch in sp_s:
        sp_c+=1


if ch_c>0 and num_c>0 and sp_c >0 and " " not in a:
    print("가능한 비밀번호입니다.")
else:
    print("불가능한 비밀번호입니다.")