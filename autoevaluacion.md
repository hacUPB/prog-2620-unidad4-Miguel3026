# 📝 Plantilla de Autoevaluación: Gestión de Mantenimiento de Flota Aeronáutica ✈️

**Instrucciones para los estudiantes:**
1. Hagan una copia de este archivo y guárdenlo en la raíz de su repositorio con el nombre `AUTOEVALUACION.md`.
2. Lean cuidadosamente cada criterio de la rúbrica.
3. En el apartado **Nota Esperada**, asignen una calificación numérica (de 0.0 a 5.0) que consideren justa para su trabajo en ese criterio.
4. En el apartado **Justificación**, expliquen con sus propias palabras por qué merecen esa nota. Sean críticos y honestos.
5. En el apartado **Evidencia**, inserten pantallazos de la ejecución de la consola, imágenes de su diagrama o bloques de código (usando la sintaxis de Markdown con \`\`\`) que respalden su justificación.
6. Al final, calculen su nota definitiva esperada según los porcentajes.

---

## 👥 1. Información del Equipo

* **Miembro 1:** [Miguel Angel Mejia Loaiza] - [000257893]
* **Miembro 2:** [Deybid Felipe Catillo Valencia] - [000575761]

---

## 📊 2. Evaluación por Criterios

### Criterio 1: Diagrama y Lógica (Valor: 20%)
*Evalúa si el diagrama es claro, lógico y representa fielmente la estructura de datos utilizada (listas/diccionarios) y el flujo del programa.*

* **Nota Esperada (0.0 - 5.0):** [5.0]
* **Justificación:** 
  > *El programa sigue las especificaciones, lo logica y la estructura dada por los ejercicios anteriores, manteniendo la eficiencia sin perder calidad en el resultado final.*
* **Evidencia:**
  *Inserta aquí la imagen de tu diagrama ![Diagrama 1](../prog-2620-unidad4-Miguel3026/imagenes/WhatsApp%20Image%202026-04-15%20at%2010.10.56%20AM.jpeg)![Diagrama 2](../prog-2620-unidad4-Miguel3026/imagenes/Captura%20de%20pantalla%202026-04-15%20141518.png)*

### Criterio 2: Uso de Estructuras (Listas y Diccionarios) (Valor: 30%)
*Evalúa si se utilizaron diccionarios y listas de manera correcta y anidada para almacenar los datos ingresados por el usuario, sin redundancias.*

* **Nota Esperada (0.0 - 5.0):** [5.0]
* **Justificación:**
  > *En el codigo se trabajo con una rubrica interna de optimizacion donde se eliminaron la mayor cantidad de redundancias posibles sin perder eficiencia, claridad y estetica.*
* **Evidencia:**
  
  ```python

  aeronaves = []

  for i in range(3):
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
 

### Criterio 3: Cumplimiento de Restricciones Técnicas (Valor: 20%)
*Evalúa el respeto total a las reglas: uso de ciclos clásicos (for/while), cero uso de list comprehensions, y ninguna librería/función avanzada no vista en clase.*

* **Nota Esperada (0.0 - 5.0):** [5.0]
* **Justificación:**
    > *En el transcurso del programa se observa el uso de las herramientas vistas en clase junto con los diagramas realizados*
* **Evidencia:** 
```python
  for i in range(3):
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
``````

### Criterio 4: Funcionalidad del Código (Valor: 15%)
*Evalúa si el programa pide datos correctamente, no se "crashea" y genera el reporte final de mantenimiento esperado.*

* **Nota Esperada (0.0 - 5.0):** [4.5]
* **Justificación:**
    > *Describe la experiencia de uso: La experiencia del usuario es fluida, dinamica, estica y es facil de entender siguiendo el flujo de trabajo del usuario, siempre y cuando siga las instrucciones del programa *
* **Evidencia:** *Inserta aquí 1 o 2 pantallazos (![Ejecución](./img/consola1.png)) mostrando la terminal donde se vea:*
*El ingreso manual de datos.*
*El reporte final impreso en pantalla con las piezas que requieren mantenimiento.*

### Criterio 5: Preparación para Sustentación (Valor: 15%)
*Aunque esta nota la dará el profesor en la entrevista oral, autoevalúen su nivel de preparación y comprensión del código que entregaron.*

* **Nivel de Confianza (Bajo / Medio / Alto):** [Alto]
* **Justificación:**
    > *[Reflexionen como equipo: Ambos entendemos linea por lineal lo que hace el codigo, podemos explicarlo de forma fluida junto con la logica detras de cada proceso]*
* **Evidencia de preparación: Describan brevemente qué estrategia usaron para asegurar que ambos dominan el código ("basicamente se trabajo en conjunto de forma presencial para que cualquier duda se pueda solucionar al momento sin dar lugar a dudas de ambiguedades").**

### 📈 3. Cálculo de Nota Definitiva Esperada
Multipliquen la nota asignada en cada criterio por su porcentaje respectivo y sumen los resultados para obtener su nota final esperada.

|Criterio	|Nota |Asignada	|Peso	|Subtotal |(Nota * Peso) |
|---|---|---|---|---|---|
|1. Diagrama y Lógica	|[5]	|20% |(0.2)	|[Resultado]|
|2. Uso de Estructuras	|[5]	|30% |(0.3)	|[Resultado]|
|3. Cumplimiento Restricciones|	[5]	|20% |(0.2)	|[Resultado]|
|4. Funcionalidad	|[4.5]	|15% |(0.15)	|[Resultado]|
|5. Sustentación (Estimado)|	[4]|	15%| (0.15)|	[Resultado]|

NOTA FINAL ESPERADA		100%	[4,775]

✨ ""La educación es para el carácter, no solo para la mente"." ✨