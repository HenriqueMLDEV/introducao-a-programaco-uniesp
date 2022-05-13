from random import randint

m = []
l = soma = 0
for x in range(1, 11):
  n = []
  for y in range(1, 11):
    numero = randint(10, 20)
    soma = soma+numero
    n.append(numero)
  print(n)
  l += 1
  m.append(n)

print("-----------------------------")

soma_total = 0
for linha in m:
  for coluna in linha:
    soma_total = soma_total+coluna
print("o valor total da soma é: {}".format(soma_total) )  

print("-----------------------------")

print("matriz * 3")

f = []
for linha in m:
  g = []
  for coluna in linha:
    numero_3 = coluna*3
    g.append(numero_3)
  f.append(g)

  print(g)