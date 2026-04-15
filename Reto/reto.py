aeronaves = []

# Bucle para ingresar al menos 3 aeronaves
for i in range(3):
    print("\n--- Registro de Aeronave", i + 1, "---")
    
    matricula = input("Ingrese matrícula: ")
    modelo = input("Ingrese modelo: ")
    horas_vuelo = int(input("Ingrese horas de vuelo acumuladas: "))
    
    # Lista de componentes
    componentes = []
    
    # Cantidad de componentes
    cantidad_componentes = int(input("¿Cuántos componentes desea registrar?: "))
    
    # Registro de componentes
    for j in range(cantidad_componentes):
        print("\nComponente", j + 1)
        
        nombre = input("Nombre del componente: ")
        horas_uso = int(input("Horas de uso: "))
        limite = int(input("Límite de horas antes de mantenimiento: "))
        
        # Diccionario del componente
        componente = {
            "nombre": nombre,
            "horas_uso": horas_uso,
            "limite": limite
        }
        
        componentes.append(componente)
    
    # Diccionario de la aeronave
    aeronave = {
        "matricula": matricula,
        "modelo": modelo,
        "horas_vuelo": horas_vuelo,
        "componentes": componentes
    }
    
    # Guardar aeronave en la lista principal
    aeronaves.append(aeronave)


print("\n\n--- REPORTE DE MANTENIMIENTO ---")

# Variable para saber si todo está bien
melo = True

# Recorrer aeronaves
for i in range(len(aeronaves)):
    aeronave = aeronaves[i]
    
    print("\nAeronave:", aeronave["matricula"], "-", aeronave["modelo"])
    
    componentes = aeronave["componentes"]
    
    # Recorrer componentes
    for j in range(len(componentes)):
        comp = componentes[j]
        
        # Comparación
        if comp["horas_uso"] >= comp["limite"]:
            print("ALERTA:", comp["nombre"], "- requiere mantenimiento (", comp["horas_uso"], "/", comp["limite"], ")")
            melo = False
        else:
            print("OK:", comp["nombre"], "- dentro del límite (", comp["horas_uso"], "/", comp["limite"], ")")

# Mensaje final
if melo:
    print("\nTodo está en orden.")
else:
    print("\nHay componentes que requieren mantenimiento.")