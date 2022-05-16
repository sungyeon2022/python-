'''
    리스트(List)=배열
        원하는 여러 데이터를 순서대로 저장 *중복된 데이터 저장 가능
        데이터 추가 순서로 저장
        데이터 추가 삭제 수정 가능
'''
#리스트 생성
li=[1,2,'Hello',True,False,'World'] #,데이터와 데이터 구분
print(li)
#리스트도 인덱스 번호를 이용해서 하나씩 뽑을 수 있다
print(li[0])
print(li[1])
print(li[2])
print(li[3])
print(li[4])
print(li[5])
#print(li[6]) 인덱스 범위 초과 오류
print("---------------------")
print(li[1:4])
ex=li[1:4] # ex에 li의 1번부터 4번까지 리스트 데이터를 저장
print(ex)
print(li)

#데이터 추가, 삭제, 수정

#추가 append 사용
li.append('Append')
print(li)
#끼워 넣기 3번
li.insert(3,777)
print(li) #3번째 이후 데이터가 한칸씩 밀림
#수정
li[3] = 100
print(li)
#삭제
li.pop() #맨 끝 데이터 삭제
print(li)
li.pop(2)
print(li)#2번 인덱스 데이터 삭제
li.remove(True)#일치하는 데이터 기준 삭제, 처음으로 검색 되는 데이터 삭제
print(li)
print(len(li)) #데이터 개수 출력
li.clear()
print(li)