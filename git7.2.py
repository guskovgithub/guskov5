f=open('git5.1.txt')
a=[]
min=10**10
max=0
for line in f:
    a.append(line)
for i in range(len(a)):
    a[i]=int(a[i])
for j in range(len(a)):
    if a.count(a[j])>max:
        max=a[j]
    if a.count(a[j])<min:
        min=a[j]
        
        
print('самое часто встречающееся', max,)
print('самое редко встречающееся', min,)
    
