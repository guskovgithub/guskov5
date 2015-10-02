f=open("git5.2.txt")
a=[]
for line in f:
    a.append(line)
for i in range(len(a)):
    a[i]=float(a[i])
print(max(a), a.index(max(a)), sep=' ')
print(min(a), a.index(min(a)), sep=' ')

f.close()
