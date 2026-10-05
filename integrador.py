
while True:
    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        if cantidad_estudiantes > 0:
            break
        else:
            print("La cantidad debe ser mayor a cero.")
    except ValueError:
        print("Debe ingresar un número entero.")
        
suma_promedio = 0
aprobados = 0
reprobados = 0

# Corregido: "estudiante" para que coincida con el print de abajo
for estudiante in range(1, cantidad_estudiantes + 1):
    print("\n--- Estudiante", estudiante, "---")
    nombre = input("Nombre: ") # Corregida la indentación de aquí en adelante
    
    while True:
        try:
            nota1 = float(input("Primera Nota (0-5): "))
            if 0 <= nota1 <= 5:
                break
            else:
                print("La nota debe ser entre 0 y 5.")
        except ValueError:      
            print("Debe ingresar un número válido.")
                
    while True:
        try:
            nota2 = float(input("Segunda Nota (0-5): ")) # Cambiado a Segunda
            if 0 <= nota2 <= 5:
                break
            else:
                print("La nota debe ser entre 0 y 5.")
        except ValueError:      
            print("Debe ingresar un número válido.")
                
    while True:
        try:
            nota3 = float(input("Tercera Nota (0-5): ")) # Cambiado a Tercera
            if 0 <= nota3 <= 5:
                break
            else:
                print("La nota debe ser entre 0 y 5.")
        except ValueError:      
            print("Debe ingresar un número válido.")
                
    # Corregido: El cálculo y los estados ahora están DENTRO del ciclo for
    promedio = (nota1 + nota2 + nota3) / 3 
    
    if promedio >= 3:
        print("Promedio:", round(promedio, 2))
        print("Estado: Aprobado")
        aprobados = aprobados + 1
    else:
        print("Promedio:", round(promedio, 2))
        print("Estado: Reprobado")
        reprobados = reprobados + 1
    
    suma_promedio = suma_promedio + promedio

# Opcional: Aquí podrías imprimir las estadísticas finales (totales de aprobados, etc.)

                