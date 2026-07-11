#부녀회장이 될테야
n=int(input())
for i in range(n):
    floor=int(input()) #층
    num= int(input()) #호
    floor_0=[x for x in range(1,num+1)]
    for j in range(floor):
        for k in range(1,num):
            floor_0[k] +=floor_0[k-1]
    print(floor_0[-1])