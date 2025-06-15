datos={}
estu=0
tomar=0
totaldias=0
while True:
    print("1. Agregar Estudiante")
    print("2. Registar Asistencia")
    print("3. Ver porcentaje de asistencia de un estudiante")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            estu+=1
            tomar=0
            nombre=input("Ingrese nombre de el estudiante: ")
            nombre=nombre.capitalize()
            edad=int(input("Ingrese su edad: "))
            asistencia=0
            datos[nombre]={"edad":edad,"asistencia":asistencia,"tomar":tomar}
        case 2:
            totaldias+=1
            print("1. Registar uno x uno")
            print("2. Poner Presentees a todos")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    contar=0
                    for i in range(estu):
                        while True:
                            if contar==estu:
                                break
                            for nombre,i in datos.items():
                                print(f"Nombre: {nombre}\nEdad: {i["edad"]}\nAsistencia: {i["asistencia"]}")
                                print()
                            buscar=input("Ingrese estudiante que le tomara asistencia")
                            print(estu)
                            print(contar)
                            buscar=buscar.capitalize()
                            for nombre,i in datos.items():
                                    if buscar==nombre:
                                        if i["tomar"]==0:
                                            print(f"Nombre: {nombre}\nEdad: {i["edad"]}\nAsistencia: {i["asistencia"]}")
                                            tomar=input("Ingrese asistencia true/false")
                                            if tomar=="true":
                                                i["asistencia"]+=1
                                                contar+=1
                                            else:
                                                i["asistencia"]+=0
                                                contar+=1
                                            i["tomar"]+=1
                                        elif i["tomar"]==1:
                                            print("YA LE TOMO LA ASISTENCIA A ESTE ESTUDIANTE")
                case 2:
                    for nombre,i in datos.items():
                        i["asistencia"]+=1
                    for nombre,i in datos.items():
                        print(f"Nombre: {nombre}\nEdad: {i["edad"]}\nAsistencia: {i["asistencia"]}")
                        print()
        case 3:
            print(f"DIAS TOTALES: {totaldias}")
            for nombre,i in datos.items():
                estudiante=i["asistencia"]
                porcen=i["asistencia"]/totaldias*100
                porcen=round(porcen)
                print(f"Nombre: {nombre}\nEdad: {i["edad"]}\nAsistencia: {i["asistencia"]}\nPorcentaje: {porcen}%")
                print()