salario = float(input())

if salario >= 0 and salario <= 2000.00:
    print('Isento')

elif salario >= 2000.01 and salario <= 3000.00:
    imposto0 = salario - 2000.00
    imposto8 = imposto0*0.08
    imposto_total = imposto8
    print('R$ {:.2f}'.format(imposto_total))

elif salario >= 3000.01 and salario <= 4500.00:
    imposto0 = salario - 3000.00
    imposto8 = 1000*0.08
    imposto18 = imposto0*0.18
    imposto_total = imposto8 + imposto18
    print('R$ {:.2f}'.format(imposto_total))

elif salario >= 4500.00:
    imposto0 = salario - 4500.00
    imposto8 = 1000*0.08
    imposto18 = 1500*0.18
    imposto28 = imposto0 *0.28
    imposto_total = imposto8 + imposto18 + imposto28
    print('R$ {:.2f}'.format(imposto_total))

