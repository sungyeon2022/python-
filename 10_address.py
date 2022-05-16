lst = [1,2,3,4,5]
print(id(lst))
lst.append(100)
print(id(lst))
lst.remove(2)
print(id(lst))

#mutable ---> list, set, dict, 메모리 주소가 변경되지 않고 지정되어 있음
print("----------------------------")
num = 10
print(id(num))
num = 20
print(id(num))
num = 'Test'
print(id(num))

newNum = num
print(id(newNum))
#(immutable) --> int, float, str, tuple ,메모리 주소가 원초적인 값은 바뀜
#파이썬의 메모리 지정 방식