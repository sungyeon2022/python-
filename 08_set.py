'''
    set은 집합 형태의 자료형
    * 1. 중복된 데이터를 저장할 수 없음 --> **고유 값만 저장
    2. 데이터 자동 정렬 --> **데이터 저장 순서가 보장되지 않음
    예) 로또 번호 뽑기
'''

s1 = {1, 2, 5, 6, 7, 1, 5, -3, 6, 11} #중복 된 값은 자동 제외, 내부 알고리즘으로 자동 정렬
print(s1) #예시

lst1 =list(s1)
tu1= tuple(s1)
print(lst1)
print(tu1)
s2 = set(lst1)
print(s2)
#set도 튜플과 리스트의 관계와 같음
#데이터 추가
s1.add(999)
#데이터 삭제
s1.remove(5)
# s1.remove(5)
print(s1)#데이터 기준 삭제
s1.pop()
print(s1)#첫번째 데이터 삭제
s1.discard(2)
s1.discard(2)
print(s1)#데이터 기준 삭제는 remove와 동일함
#차이점 : remove는 삭제할 데이터가 없는 경우 Runtime에러(실행중 오류)를 출력 함
#discard는 삭제할 데이터가 없는 경우에도 에러가 발생하지 않음

