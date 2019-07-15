NomeVendedor = str(input())
SalarioFixo = float(input())
TotalVendas = float(input())

SalarioTotal = SalarioFixo + (TotalVendas*0.15)

print("TOTAL = R$ %0.2f" %SalarioTotal)
