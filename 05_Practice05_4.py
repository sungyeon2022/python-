a=str(input())
print(f"차량번호는 '{a}'는","오늘운행가능 입니다." if int(a[-1])%2==0 else "운행불가 입니다.")