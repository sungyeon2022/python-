k=list(map(int,input().split()))

k.sort(reverse=True)

for i in k:
    rank=1
    for s in k:
        if i<s:
            rank+=1
        else:
            break
    print(f"{rank}등 - {i}점")