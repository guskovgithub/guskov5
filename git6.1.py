
ourfile = open('git5.2.txt', 'r')
a=[]
for line in ourfile:
    a.append(line)

for i in range(len(a)):
    a[i]=float(a[i])
a=sum(a)/len(a)
print(a)
ourfile.close()




