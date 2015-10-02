a=input().split()
k=int((len(a)/2)//1)
i=0
while i<k:
    print(a[i], a[(i+1)*(-1)], end=' ')
    i+=1
if len(a)%2!=0:
    print(a[i])
