import random
vet = []
numeros_vet = []
for numero in range(1,51):
    vet.append(random.randint(1,10))
print(vet)
for n in vet:
    if n not in numeros_vet:
        
        print("numero repetido:",n)
        numeros_vet.append(n)