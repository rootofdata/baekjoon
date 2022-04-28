#통계학
import sys

N= int(input())
num_list=[]
for _ in range(N):
    num=int(sys.stdin.readline())
    num_list.append(num)
print(round(sum(num_list)/N)) #산술평균 출력

#중앙값 
num_list.sort()
print(num_list[N//2])

#최빈값
from collections import Counter
cnt=Counter(num_list).most_common()
if len(cnt)>1 and cnt[0][1]==cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

#범위
print(max(num_list)-min(num_list))