
ourfile = open('git5.2.txt', 'r')
a=[]
squareSum=0
for line in ourfile:    #переносим значения из в файла в список а, каждый элемент имеет тип str
   a.append(line)

for i in range(len(a)): #меняем тип элементов со сторки на действительный 
    a[i]=float(a[i])
for i in range(len(a)): #находим сумму квадратов 
    squareSum+=a[i]**2
MeadleOfSquares=squareSum/len(a) #ср знач суммы квадратов              
    
Meadle=sum(a)/len(a)
print((MeadleOfSquares-Meadle**2)**(0.5))
ourfile.close()




