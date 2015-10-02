	
a =list(map(int, input().split()))
sum=0
marks=0
a.append(0)
for i in range(9):
 if a[i]!=2 or a[i+1]==2:
  sum+=a[i]
  marks+=1
print(int((sum+a[9])/(marks+1)//1))

