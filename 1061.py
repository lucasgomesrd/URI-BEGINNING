dia_inicial = input().split(" ")
dia_inicial_inteiro = int(dia_inicial[1])
hora_inicial_completa = input().split(" ")
hora_inicial = int(hora_inicial_completa[0])
minuto_inicial = int(hora_inicial_completa[2])
segundo_inicial = int(hora_inicial_completa[4])

dia_final = input().split(" ")
dia_final_inteiro = int(dia_final[1])
hora_final_completa = input().split(" ")
hora_final = int(hora_final_completa[0])
minuto_final = int(hora_final_completa[2])
segundo_final = int(hora_final_completa[4])

#Execução

dia = (dia_final_inteiro) - (dia_inicial_inteiro)

hora = (hora_final) - (hora_inicial)
if(hora < 0):
    hora = 24 + hora
    dia = dia - 1

minuto = (minuto_final) - (minuto_inicial)
if(minuto < 0):
    minuto = 60 + minuto
    hora = hora - 1

segundos = (segundo_final) - (segundo_inicial)
if(segundos < 0):
    segundos = 60 + segundos
    minuto = minuto - 1

if(dia <= 0):
    dia = 0

print('{} dia(s)'.format(dia))
print('{} hora(s)'.format(hora))
print('{} minuto(s)'.format(minuto))
print('{} segundo(s)'.format(segundos))

