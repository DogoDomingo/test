


# Lista para guardar los estudiantes
estudiantes = []

def buscar_estudiante():
    nombre_o_codigo = input("Ingrese nombre o código de estudiante: ").strip()
    for estudiante in estudiantes:
        if estudiante['nombre'].lower() == nombre_o_codigo.lower() or estudiante['codigo'] == nombre_o_codigo:
            print("Nombre:", estudiante['nombre'])
            print("Edad:", estudiante['edad'])
            print("Género:", estudiante['genero'])
            print("Código:", estudiante['codigo'])
            print("Promedio:", estudiante['promedio'])
            return
    print("Estudiante no encontrado.")

def modificar_estudiante():
    codigo = input("Ingrese el código del estudiante a modificar: ").strip()
    for estudiante in estudiantes:
        if estudiante['codigo'] == codigo:
            try:
                nueva_edad = int(input("Nueva edad: "))
                if nueva_edad < 0:
                    print("Edad inválida.")
                    return
            except ValueError:
                print("Edad inválida.")
                return
            nuevo_genero = input("Nuevo género (M/F): ").strip().upper()
            if nuevo_genero not in ("M", "F"):
                print("Género inválido.")
                return
            try:
                nuevo_promedio = float(input("Nuevo promedio: "))
                if not (0 <= nuevo_promedio <= 10):
                    print("Promedio inválido.")
                    return
            except ValueError:
                print("Promedio inválido.")
                return
            estudiante['edad'] = nueva_edad
            estudiante['genero'] = nuevo_genero
            estudiante['promedio'] = nuevo_promedio
            print("Datos modificados con éxito.")
            return
    print("Estudiante no encontrado.")

def eliminar_estudiante():
    codigo = input("Ingrese el código del estudiante a eliminar: ").strip()
    for estudiante in estudiantes:
        if estudiante['codigo'] == codigo:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado.")
            return
    print("No se pudo eliminar.")

def mostrar_todos():
    if estudiantes == []:
        print("No hay registros.")
        return
    for estudiante in estudiantes:
        print(estudiante['codigo'], '-', estudiante['nombre'])


print("Sistema de gestión de estudiantes")
while True:
    print("\n1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Modificar datos de estudiante")
    print("4. Eliminar estudiante")
    print("5. Mostrar todos los estudiantes")
    print("6. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        nombre = input("Nombre: ").strip()
        edad = input("Edad: ").strip()
        if not edad.isdigit() or int(edad) < 0:
            print("Edad inválida.")
            continue
        genero = input("Género (M/F): ").strip().upper()
        if genero not in ("M", "F"):
            print("Género inválido.")
            continue
        codigo = input("Código: ").strip()
        existe = False
        for estudiante in estudiantes:
            if estudiante['codigo'] == codigo:
                existe = True
                break
        if existe:
            print("Código ya existe.")
            continue
        promedio = input("Promedio: ").strip()
        try:
            promedio = float(promedio)
            if promedio < 0 or promedio > 10:
                print("Promedio inválido.")
                continue
        except ValueError:
            print("Promedio inválido.")
            continue
        estudiantes.append({
            'nombre': nombre,
            'edad': int(edad),
            'genero': genero,
            'codigo': codigo,
            'promedio': promedio
        })
        print("Estudiante agregado.")
    elif opcion == "2":
        buscar_estudiante()
    elif opcion == "3":
        modificar_estudiante()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        mostrar_todos()
    elif opcion == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")