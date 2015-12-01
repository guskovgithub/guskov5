from random import *
#input = open('git5.1.txt', 'r')
output = open('int_data.txt', 'w')
for i in range(0,10000):

   print(randint(0,100), file=output)
#input.close()
output.close()
