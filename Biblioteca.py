codigo=0

while True:
    print("1. Agregar Libro")
    print("2. Buscar Libro")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Eliminar Libro")
    print("6. Mostar Todos Los Libros")
    op=input("Ingrese una opcion: ")
    match op:
        case "1":
            codigo+=1
            nombre=input("Ingrese nombre de el libro: ")
            año=input("Ingrese año de el libro: ")
            libros={
                codigo:{
                    "nombre":nombre,
                    "año":año,
                    "disponible":1
                }
            }
        case "2":
            print(f"Libros Totales: {codigo}")
            b=int(input("Ingrese codigo de el libro: "))
            if b in libros:
                print(f"Libro: {libros[b]["nombre"]}\nAño: {libros[b]["año"]}")
            else:
                print("Codigo Incorrecto")
        case "3":
            contar=0
            for i in libros:
                contar+=1
                if libros[i]["disponible"]==1:
                    dispo = "Si"
                elif libros[i]["disponible"]==0:
                    dispo = "No"
                print(f"Codigo: {contar} Libro: {libros[i]['nombre']}\nAño: {libros[i]['año']}\nDisponible: {dispo}")
            e=int(input("Ingrese codigo de libro que quiere: "))
            if e in libros:
                if dispo=="Si":
                    print(F"Aqui tiene su libro:\nLibro: {libros[e]["nombre"]} {libros[e]["año"]}")
                    libros[i]["disponible"]-=1
                else:
                    print("Libro Se Encuentra Prestado")
                    print()
            else:
                print("No se encuentra el libro")
        case "4":
            if i in libros:
                if libros[i]["disponible"]==0:
                    print(f"Codigo: {contar} Libro: {libros[i]['nombre']}\nAño: {libros[i]['año']}\nDisponible: {dispo}")
                i=int(input("Ingrese Codigo de libro que desea devolver: "))
                for i in libros:
                    print(f"Se ha devuelto el libro: {libros[i]["nombre"]}")
                    libros[i]["disponible"]+=1