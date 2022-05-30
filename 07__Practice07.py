ex=[99,78,100,91,81,85,54,100,71,50]
# sc=list()
#
# for i in ex:
#     if i+5<=100:
#         sc.append(i+5)
#     else:
#         sc.append(100)
#
# print(sc)

for i in range(len(ex)):
    if ex[i]+5<=100:
        ex[i]+=5
    else:
        ex[i]=100