'''
    인덱스(index)
        1. 문자열에서 각 문자마다 부여 된 번호
        2. 맨 앞에서부터는 0부터 번호가 매겨짐
        3. 맨 뒤에서부터는 -1 번호가 시작 (맨뒷자리 뽑을 때 편함)
'''
s='hello'
print(s[0],s[-5])
print(s[1],s[-4])
print(s[2],s[-3])
print(s[3],s[-2])
print(s[4],s[-1])
#부분수정은 안 됨 s[2] = 'k'

num = '100' #num = str(100) 같은 의미
print(num[0],num[-3])
print(num[1],num[-2])
print(num[2],num[-1])

