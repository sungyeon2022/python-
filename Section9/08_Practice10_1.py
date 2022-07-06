print("점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요")
k=[]
a=int(input("점수 입력 >>> "))
while a>0:
    k.append(a)
    a = int(input("점수 입력 >>> "))

print(f'평균 = {sum(k)/len(k)}, 최대 = {max(k)}, 최소 = {min(k)}')