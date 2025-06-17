datos = {}

while True:
    print("\n1. Agregar Estudiantes")
    print("2. Ver Promedios Generales")
    print("3. Ver Estudiante Con La Nota Más Alta")
    print("0. Salir")
    op = int(input("Ingrese una opción: "))

    match op:
        case 1:
            nombre = input("Ingrese su nombre: ")
            nota1 = float(input("Ingrese Nota de Matemáticas: "))
            nota2 = float(input("Ingrese Nota de Historia: "))
            nota3 = float(input("Ingrese Nota de Ciencias: "))
            promedio = round((nota1 + nota2 + nota3) / 3, 1)
            datos[nombre] = {
                "mate": nota1,
                "historia": nota2,
                "ciencias": nota3,
                "promedio": promedio
            }

        case 2:
            print(f"\nCantidad de estudiantes: {len(datos)}")
            for n, i in datos.items():
                print(f"\nNombre: {n}")
                print(f"Nota Matemáticas: {i['mate']}")
                print(f"Nota Historia: {i['historia']}")
                print(f"Nota Ciencias: {i['ciencias']}")
                print(f"Promedio: {i['promedio']}")

        case 3:
            if datos:
                mayor = max(datos, key=lambda nombre: datos[nombre]["promedio"])
                mejor = datos[mayor]
                print(f"\nEl estudiante con el promedio más alto es {mayor}")
                print(f"Promedio: {datos[mayor]["promedio"]}")
            else:
                print("No hay estudiantes registrados.")

        case 0:
            print("Programa finalizado.")
            break

        case _:
            print("Opción no válida.")
