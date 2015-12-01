from random import *
#input = open('git5.2.txt', 'r')
output = open('float_data.txt', 'w')
for i in range(0,1000):
  a=random()*100
  print((a//1)+(((a-a//1)*100)//1)/100, file=output)
#input.close()
output.close()
