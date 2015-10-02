n=int(input())
up=[]
dn=[]*2
up.append(1)

print(' '.join(map(str, up)))
    
for i in range(n):
    for j in range(i+2):
        if j==0:
            dn.append(1)
        elif j==i+1:
            dn.append(1)
        else:
            dn.append(up[j]+up[j-1])
    print(' '.join(map(str, dn)))
    up=[]
    for j in range(len(dn)):
        up.append(int(dn[j]))
    
    dn=[]
        
    
    
    
