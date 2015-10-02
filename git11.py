k,n=int(input()),int(input())
a=[]
for i in range(k):
     a.append(1)
for i in range(k,n+1):
    a.append(0)
    for j in range(i-k,i):
       a[i]+=int(a[j])
print(a[n])       
    
     
