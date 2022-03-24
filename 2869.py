A,B,V = map(int,input().split())
n=(V-A)/(A-B)+1
a=int(n)
if n==a:
    print(a)
else:
    print(a+1)
    
#from math import ceil
#A, B, V = map(int, input().split())
#print( ceil((V-A)/(A-B)) + 1)
#ceil : 올림 함수