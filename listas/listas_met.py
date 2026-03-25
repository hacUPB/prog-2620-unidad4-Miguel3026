from random import randint

meses = ["Enero", "Febrero", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre, Diciembre"]

lista = []

for i in range(12):
    dato = randint(20,80)
    lista.append(dato)

print(lista)

mayor = max(lista)
veces = lista.count(mayor)
mes = lista.index(mayor)

print(f"El {mayor} esta {veces} en la lista")
print(f"Se vendieron mas autos en {meses[mes]}")
print(f"Se vendieron {mayor} autos")
