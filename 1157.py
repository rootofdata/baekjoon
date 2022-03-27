#단어 공부
a = input()
a=a.upper()
a_list=list(set(a))
cnt=[]
for i in a_list:
    b= a.count(i)
    cnt.append(b)
if cnt.count(max(cnt)) ==1:
    print(a_list[cnt.index(max(cnt))])
else: print("?")