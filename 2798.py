#블랙잭
N,M = map(int,input().split())
n = list(map(int,input().split()))
sum_list=[]
for i in range(N):
    for j in range(N):
        if i!=j:    
            for k in range(N):
                if k!=j and k!=i:
                    tot=n[i]+n[j]+n[k]
                    if tot >M:
                        pass
                    else:
                        sum_list.append(tot)
print(max(sum_list))