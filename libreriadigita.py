datos={}
while True:
    print("1. Agregar Libro")
    print("2. Prestar Libro")
    print("3. Devolver Libro")
    print("4. Ver Lista De Libros")
    print("5. Ver Libros Disponibles")
    print("6. Mostrar Libro Mas Prestaedo")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            libro=input("Ingrese nombre de libro: ").capitalize()
            año=int(input("Ingrese año de el libro: "))
            datos[libro]={"año":año,"dispo":True,"total":0}
        case 2:
            for n,i in datos.items():
                if i["dispo"]==True:
                    print(f"Libro: {n}\nAño>: {i["año"]}\nDisponible: SI")
                    print()
            elegir=input("Ingrese nombre de el libro que desea adquirir: ").capitalize()
            for n,i in datos.items():
                if elegir==n:
                    print(f"Aqui Tiene Su Libro Seleccionado: {n}")
                    i["dispo"]=False
                    i["total"]+=1
        case 3:
            for n,i in datos.items():
                if i["dispo"]==False:
                    print(f"Libro: {n}\nAño>: {i["año"]}\nDisponible: NO")
                    print()
            devolver=input("Ingrese nombre de el libro que devolvera: ").capitalize()
            for n,i in datos.items():
                if devolver==n:
                    print(f"Usted ha devuelto el libro {n}")
                i["dispo"]=True
        case 4:
            print(f"Libros Totales: {len(datos)}")
            for n,i in datos.items():
                if i["dispo"]==True:
                    print(f"Libro: {n}\nAño>: {i["año"]}\nDisponible: SI")
                    print()
                else:
                    print(f"Libro: {n}\nAño>: {i["año"]}\nDisponible: NO")
                    print()
        case 5:
            for n,i in datos.items():
                if i["dispo"]==True:
                    print(f"Libro: {n}\nAño>: {i["año"]}\nDisponible: SI")
                    print()
        case 6:
            mayor=max(datos,key= lambda libro:datos[libro]["total"])
            print(f"El LIBRO MAS PRESTADO ES {mayor} CON {datos[mayor]["total"]} VECES PEDIDO")