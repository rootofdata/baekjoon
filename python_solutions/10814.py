#나이순 정렬
n = int(input())
order=[]
for _ in range(n):
    age,name = map(str,input().split())
    age=int(age)
    order.append((age,name))

order.sort(key=lambda parameter_list: parameter_list[0])
for i in order:
    print(i[0],i[1])