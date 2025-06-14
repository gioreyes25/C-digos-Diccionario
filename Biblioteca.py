codigo=0
datos=[]
while True:
    print("1. Agregar Libros")
    print("2. Buscar Libro")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Eliminar Libro")
    op=input("Ingrese una opcion: ")
    match op:
        case "1":
            nombre=input("Ingrese el nombre: ")
            nombre=nombre.capitalize()
            while True:
                try:
                    año=int(input("Ingrese año de el libro: "))
                    break
                except: ValueError
                print()
                print("Solo se permiten Numeros")
            codigo+=1
            info={
                "codigo":codigo,
                "nombre":nombre,
                "año":año,
                "disponible":True
            }
            datos.append(info)
            print(datos)
        case "2":
            contar=0
            if codigo>=1:
                print(f"En total hay {codigo} Libros")
                while True:
                    try:
                        buscar=int(input("Ingrese el codigo de el libro: "))
                        break
                    except: ValueError
                    print()
                    print("Solo se permiten Numeros")
                for i in datos:
                    if buscar==i["codigo"]:
                        print(f"Nombre: {i["nombre"]}\nAño: {i["año"]}")
                        print()
                    elif buscar>codigo:
                        print("No hay coincidencias")
                        print()
                        break
            else:
                print("NO EXISTEN LIBROS")
        case "3":
            contar=0
            for i in datos:
                contar+=1
                if i["disponible"]==True:
                    dispo="Si"
                else:
                    dispo="No"
                print(f"Codigo: {i["codigo"]}\nNombre: {i["nombre"]}\nAño: {i["año"]}\nDisponible: {dispo}")
                print()
            while True:
                try:
                    buscar=int(input("Ingrese codigo de el libro que desea: "))
                    break 
                except: ValueError
                print()
                print("Solo se permiten numeros") 
            for i in datos:
                if buscar==i["codigo"]:
                    if i["disponible"]==True:
                        print(f"Aqui Tiene Su Libro: {i["nombre"]}")
                        i["disponible"]=False
                    else:
                        print(f"El libro {i["nombre"]} Se encuentra prestado, Lo Siento")
        case "4":
            contar=0
            for i in datos:
                contar+=1
                if i["disponible"]==False:
                    dispo="No"
                    print(f"Codigo: {i["codigo"]}\nNombre: {i["nombre"]}\nAño: {i["año"]}\nDisponible: {dispo}")
                    print()
                    if contar==codigo:
                        while True:
                            try:
                                
                                devolver=int(input("Ingrese codigo de el libro que desea devolver: "))
                                break
                            except: ValueError
                            print()
                            print("Solo se permiten numeros")
                        if devolver<=codigo:
                            for i in datos:
                                if devolver==i["codigo"]:
                                    print(f"Gracias por devolver el libro: {i["nombre"]}")
                                    i["disponible"]=True
                        else:
                            print("NO HAY COINCIDENCIAS")
                else:
                    print("No tiene libros que devolver")
                    break
        case "5":
            if codigo==0:
                print("NO EXISTEN LIBROS")
                print()
            else:
                print
            contar=0
            for i in datos:
                contar+=1
                if i["disponible"]==True:
                    dispo="Si"
                else:
                    dispo="No"
                print(f"Codigo: {i["codigo"]}\nNombre: {i["nombre"]}\nAño: {i["año"]}\nDisponible: {dispo}")
                for i in datos:
                    if contar==codigo:
                        while True:
                            try:
                                eliminar=int(input("Ingrese el codigo de libro que desea eliminar: "))
                                break
                            except: ValueError
                            print()
                            print("Solo se permiten numeros")
                        if eliminar<=codigo:
                            eliminar-=1
                            if datos:
                                del datos[eliminar]
                                print(f"Se acaba de eliminar El Libro: {i["nombre"]}")
                                codigo-=1
                                for i in datos:
                                    i["codigo"]-=1
                            else:
                                print("No Hay Coincidencias")
                                print()
                        else:
                            print("NO HAY COINCIDENCIAS")            
            