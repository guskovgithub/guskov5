a=input().split()

a.insert(0, len(a))
a.pop()

print(' '.join(map(str, a)))

