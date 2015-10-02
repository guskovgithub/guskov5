f=open('git5.1.txt')
a=[]
for line in f:
    a.append(line)
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(0,101):
    print('число',i,'встрачается', a.count(i),'раз', sep=' ')
