a=0
y=0
for x in range(0,6):
    n = float(input())
    if n>0:
        a=a+1
        y=y+n
    
print('{} valores positivos'.format(a))
print('{:.1f}'.format(y/a))
