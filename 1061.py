dia_inicio = int(input().split()[1])

h1, m1, s1 = map(int, input().split(" : "))

dia_fim = int(input().split()[1])

h2, m2, s2 = map(int, input().split(" : "))

inicio = (dia_inicio*24*3600 + h1*3600 + m1*60 + s1)
fim = (dia_fim * 24 * 3600 +h2 * 3600 + m2 * 60 + s2)

duracao = fim - inicio


dias = duracao // (24 * 3600)
duracao %= (24 * 3600)

horas = duracao // 3600
duracao %= 3600

minutos = duracao // 60
segundos = duracao % 60


print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
