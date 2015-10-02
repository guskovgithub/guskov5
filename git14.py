n=int(input())
time=[]

people=[]
count=0
for i in range(n):
    time=input().split()
    for k in range(len(time)):
        people.append(int(time[k]))
    time=[]
T=int(input())
for i in range(0,2*n,2):
    if T>=people[i] and people[i+1]>=T:
        count+=1
print(count)        
        
    
    
