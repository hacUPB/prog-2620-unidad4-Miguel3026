tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

print("Informe de despegue: ")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"t+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")