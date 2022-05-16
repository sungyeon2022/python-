'''
    딕셔너리(dictionary) 예) 금고를 모은 은행
        데이터1 - 데이터2 한쌍으로 저장
        key - value
        키값과 저장 값이 한쌍으로 저장
        키값을 이용하여 데이터 추가, 삭제, 수정 가능
        키값을 알면 데이터를 바로 수정가능 **키 값은 중복 X, 저장 값은 수정 가능
'''
#dict 생성
#set이랑 형태가 같음, **키값은 set으로 관리
dict1 = {'홍길동':20, '김철수':33, '이영희':45}#key:Value
print(dict1)
print(dict1['홍길동'])
print(dict1['이영희'])
# print(dict1['이영희']) Key값이 존재하지 않는 다면 오류
dict1['이영희']=777
print(dict1['이영희'])#Key값을 이용하여 데이터를 수정 할 수 있음
#다른 사용법
dict2 = dict(A='TEST',B =True) #Key 값이 자동 문자열로 저장 됨
print(dict2)
#데이터 추가
dict1['김영희']=55
print(dict1)#Key값이 중복 되지 않으면 추가 됨
dict1.setdefault('김용수',111)#김용수라는 키 값과 데이터값 111추가
print(dict1)
#데이터 삭제
dict1.pop('김영희')
print(dict1)
dict1.pop('조성연')#삭제할 데이터가 없어도 오류가 나지않음


