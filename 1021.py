x=input().split()
A,B,C=x
A=int(A)
B=int(B)
C=int(C)

if A >= (B+C):
    print('NAO FORMA TRIANGULO')

elif A**2 == ((B**2)+C**2):
    print('TRIANGULO RETANGULO')

elif A**2 > ((B**2)+C**2):
    print('TRIANGULO OBTUSANGULO')
    
elif A**2 < ((B**2)+C**2):
    print('TRIANGULO ACUTANGULO')
    
elif A == B and B == C:
    print('TRIANGULO EQUILATERO')
    
