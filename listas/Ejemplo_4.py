def MAX(lista):
    mayor = lista[0]
    for y in lista:
        if mayor < y:
            mayor = y
    return mayor

def Min(lista):
    menor = lista[0]
    for z in lista:
        if menor > z:
            menor = z
    return menor

import random
lista = []
for i in range(100):
    lista.append(random.randint(0, 5000))
mayor = lista[0]
for y in lista:
    if mayor < y:
        mayor = y
menor = lista[0]
for z in lista:
    if menor > z:
        menor = z
M, m = max(lista), min(lista)
print(f"{lista}. \n el maximo es: {M} = {mayor} y el minimo es: {m} = {menor}")