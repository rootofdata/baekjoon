#조합 0의 개수
n,m=map(int,input().split())
#2의 경우, #2! ->1 4! -> 3 6!-> 4 8!-> 7
def split_two(x):
    two_cnt=0
    while x!=0:
        x=x//2
        two_cnt+=x
    return two_cnt

def split_five(x):
    five_cnt=0
    while x!=0:
        x=x//5
        five_cnt+=x
    return five_cnt
two=split_two(n)-split_two(m)-split_two(n-m)
five=split_five(n)-split_five(m)-split_five(n-m)
print(min(two,five))
