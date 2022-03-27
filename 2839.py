#2839
a=int(input())
cnt=0
while True:
    if a%5==0:
        a-=5
        cnt+=1
    elif a%3 ==0:
        a-=3
        cnt+=1
    else:
        a-=3
        cnt+=1
    if a==0:
        break
    if a<0:
        cnt=-1
        break
print(cnt)
        