aeronaves = []

def añadir_aeronaves(aeronaves):
    NA = int(input("Ingrese cantidad de aeronaves: "))
    for i in range(NA):
        print("\n--- Registro de Aeronave", i + 1, "---")
        
        matricula = input("Ingrese matrícula: ")
        modelo = input("Ingrese modelo: ")
        horas_vuelo = int(input("Ingrese horas de vuelo acumuladas: "))
        
        componentes = []
        
        cantidad_componentes = int(input("¿Cuántos componentes desea registrar?: "))
        
        for j in range(cantidad_componentes):
            print("\nComponente", j + 1)
            
            nombre = input("Nombre del componente: ")
            horas_uso = int(input("Horas de uso: "))
            limite = int(input("Límite de horas antes de mantenimiento: "))
            
            componente = {
                "nombre": nombre,
                "horas_uso": horas_uso,
                "limite": limite
            }
            
            componentes.append(componente)
        
        aeronave = {
            "matricula": matricula,
            "modelo": modelo,
            "horas_vuelo": horas_vuelo,
            "componentes": componentes
        }
        
        aeronaves.append(aeronave)

    print("\n\n--- REPORTE DE MANTENIMIENTO ---")

    melo = True

    for i in range(len(aeronaves)):
        aeronave = aeronaves[i]
        
        print("\nAeronave:", aeronave["matricula"], "-", aeronave["modelo"])
        
        componentes = aeronave["componentes"]
    
        for j in range(len(componentes)):
            comp = componentes[j]
            
            if comp["horas_uso"] >= comp["limite"]:
                print("ALERTA:", comp["nombre"], "- requiere mantenimiento (", comp["horas_uso"], "/", comp["limite"], ")")
                melo = False
            else:
                print("OK:", comp["nombre"], "- dentro del límite (", comp["horas_uso"], "/", comp["limite"], ")")

    if melo:
        print("\nTodo está en orden.")
    else:
        print("\nHay componentes que requieren mantenimiento.")

def mirar_aeronaves(aeronaves):
    if len(aeronaves) == 0:
        print("\nNo hay aeronaves registradas.")
        return

    print("\n--- AERONAVES REGISTRADAS ---")
    for i in range(len(aeronaves)):
        aeronave = aeronaves[i]
        print("\nAeronave", i + 1, ":", aeronave["matricula"], "-", aeronave["modelo"])
        print("Horas de vuelo acumuladas:", aeronave["horas_vuelo"])

        componentes = aeronave["componentes"]
        for j in range(len(componentes)):
            comp = componentes[j]
            print("  Componente:", comp["nombre"], "| Horas de uso:", comp["horas_uso"], "| Límite:", comp["limite"])

def mostrar_menu():
    print("\n" + "=" * 52)
    print("     PROGRAMA DE GESTIÓN DE AERONAVES".center(52))
    print("=" * 52)
    print("  1. Añadir aeronaves")
    print("  2. Mirar aeronaves")
    print("  3. Salir")
    print("=" * 52)

e = True
while e:
    mostrar_menu()
    try:
        O = int(input("Seleccione una opción (1-3): "))
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entre 1 y 3.")
        continue

    match O:
        case 1:
            añadir_aeronaves(aeronaves)
        case 2:
            mirar_aeronaves(aeronaves)
        case 3:
            print("\nGracias por usar el programa. ¡suerte!")
            e = False
        case _:
            print("Opción no válida, intente de nuevo.")