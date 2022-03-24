#셀프넘버
def d(n):
    ans=n
    for i in range(0,len(str(n))):
        ans += int(n/10**i)%10
        return ans
self_number=list()
for i in range(1,10001):
    self_number.append(d(i))
for i in range(1,10001):
    if i not in self_number:
        print(i)