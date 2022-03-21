salario = float(input())

if salario >= 0 and salario <= 400.00 :
    novo_salario = (salario * 1.15)
    reajuste = round(novo_salario - salario)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 15 %')

if salario >= 400.01 and salario <= 800.00 :
    novo_salario = (salario * 1.12)
    reajuste = round(novo_salario - salario)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 12 %')

if salario >= 800.01 and salario <= 1200.00 :
    novo_salario = (salario * 1.1)
    reajuste = round(novo_salario - salario)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 10 %')

if salario >= 1200.01 and salario <= 2000.00 :
    novo_salario = (salario * 1.07)
    reajuste = round(novo_salario - salario)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 7 %')

if salario > 2000.00:
    novo_salario = (salario * 1.04)
    reajuste = round(novo_salario - salario)
    print('Novo salario: {:.2f}'.format(salario + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 4 %')
