#평균 
num = int(input())
score = list(map(int,input().split()))
m=max(score)
for i in range(num):
    score[i]=score[i]/m*100
print(sum(score)/num)
