x=input().split()
a,b=x
a=int(a)
b=int(b)

if a>=b:
    y=24-a
    z=y+b
    print('O JOGO DUROU {} HORA(S)'.format(z))
    
else:
    y=24-a
    z=y+b
    zf=24-z
    print('O JOGO DUROU {} HORA(S)'.format(abs(zf)))
