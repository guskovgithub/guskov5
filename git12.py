n=int(input())
line=list(map(int,input().split()))
for i in range(n):
    amount=0
    for j in range(n):
        if line[i]>line[j]:
            amount+=1
    if amount==len(line)-(amount+1):
        
        break
print(line[i])    
        
