quzi = input().split()
time = int(input())



quzi = [ int(quzi[i]) for i in range(len(quzi))]
for i in range(time):
   
    quzi = quzi[0:-1-quzi[-1]] + [quzi[-1]] + quzi[-1-quzi[-1]:-1]    
    
print(quzi)
