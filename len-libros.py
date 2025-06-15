datos={}
while True:
    print("1. Agregar Libro: ")
    print("2. Ver Libros")
    print("3. Pedir Libros")
    print("4. Ver Libros Prestados")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingres enombre de el libro: ")
            año=input("Ingrese año de el libro: ")
            dispo=True
            datos[nombre]={"año":año,"dispo":dispo}
        case 2:
            print(f"Cantidad de libros: {len(datos)}")
            for nombre,i in datos.items():
                print(f"Nombre: {nombre}\nAño: {i["año"]}")
                print()
        case 3:
            for nombre,i in datos.items():
                if i["dispo"]==True:
                    si="Si"
                    print(f"Nombre: {nombre}\nAño: {i["año"]}\nDisponible: {si}")
                    print()
            pedir=input("Ingrese nombre de el libro: ")
            for nombre,i in datos.items():
                if pedir==nombre:
                    print(f"Aqui tiene su libro: {nombre}")
                    i["dispo"]=False
        case 4:
            for nombre,i in datos.items():
                if i["dispo"]==False:
                    no="No"
                    print(f"Nombre: {nombre}\nAño: {i["año"]}\nDisponible: {no}")
                    print()