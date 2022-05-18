t = int(input())
res = 0
for i in range(t):
    res = 0
    sol = list(input().split())
    print(sol)
    for j in sol:
        if j == sol[0]:
            res += float(j)
        else:
            if j == '@':
                res *= 3
            elif j == '%':
                res += 5
            elif j == '#':
                res -= 7
    print('%.2f' %res)

    #res는 결과 값 저장
    #for문에서 j in sol이 의미하는 것은 sol리스트의 처음부터 끝까지