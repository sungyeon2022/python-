# for i in range(1,100):
#     f=i//10
#     k=i%10
#     if f!=0 and k!=0 and f%3==0 and k%3==0:
#         print("짝짝",end="\t\t")
#     elif f!=0 and f%3==0:
#         print("짝",end="\t\t")
#     elif k!=0 and k%3==0:
#         print("짝",end="\t\t")
#     else :
#         print(i,end="\t\t")
#     if i%10==0:
#         print("\n")

for i in range(1,100):
    msg=""
    if i>=10 and i//10 %3 ==0:
        msg='짝'
    if i%10 in [3,6,9]:
        msg +='짝'
    if msg=="":
        print(i,end='\t\t')
    else:
        print(msg,end="\t\t")
    if i%10==0:
        print()