def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"combsutible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]
agregar_combustible(combustible_actual, 500)
print(combustible_actual) 