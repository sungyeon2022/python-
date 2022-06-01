while True:
    a=int(input("이번 영화의 평정을 입력하세요 >>> "))
    if 5<a or 1>a:
        print("평점은 1~5 사이면 입력할 수 있습니다.")
        continue
    print(f"평점: {'★'*a}")
    break