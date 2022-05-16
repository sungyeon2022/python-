box = 10
# =은 대입 연산자이다.(box라는 메모리 공간을 만들고 그 공간에 10을 저장하겠다)

print(box)
#변수 오른쪽에 =이 없으면 계산하는 값 용도로 쓰임
#이 때는 저장하는 용도가 아니라 변수가 저장한 값을 읽어옴
box = 20
box = 30
#box 변수에 30을 저장 이전에 저장하였던 20과 10은 무시 됨
print(box)
#따라서 출력 값은 30

t= 100
print(box+t)
#box와 t는 계산 용도로 사용 됨

result = box + t
#result변수에 box와 t의 합을 저장
print(result)
box = 200
print(result)