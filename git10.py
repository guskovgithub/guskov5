n=input().split()
t=int(input())
for j in range(t):

 n.insert(0,n[-1])
 n.pop()
 if int(n[0])+1<len(n):
  n[int(n[0])+1:int(n[0])+1]=n[0]
  n.pop(0)
 
    

print(' '.join(n))

