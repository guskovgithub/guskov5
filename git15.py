WorkTime = int(input())
People = input().split()
Pick = int(input())
max = 0
for i in range(WorkTime - Pick +1):
    if int(People[i])+int(People[i+1])+int(People[i+2])> max:
           max = int(People[i])+int(People[i+1])+int(People[i+2])
print(max)
