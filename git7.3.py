f=open('git5.1.txt')
a=[]
b=[]
k=0
for l in range(0,100):
    b.append(l)
for line in f:
    a.append(line)
for j in range(len(a)):
    a[j]=int(a[j])
for i in range(0,100):
    if i in a:
        k+=1
        
        
    
             
print(k)

f.close()
