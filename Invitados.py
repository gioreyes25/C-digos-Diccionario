datos={}
nombres=[]
while True:
    print("1. Registar Invitados")
    print("2. Mostar Invitados")
    print("3. Mostrar Nombre Mas Largo")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de el invitado: ")
            edad=int(input("Ingrese edad de el invitado: "))
            datos[nombre]={"edad":edad}
            nombres.append(nombre)
        case 2:
            print(f"Invitados Totales: {len(datos)}")
            for nombre,i in datos.items():
                print(f"Nombre: {nombre}\nEdad: {i["edad"]}")
                print()
        case 3:
            for nombre,i in datos.items():
                mas6=len(nombre)
                if mas6>6:
                    print("Nombres Con Mas De 6 Letras: ")
                    print(f"Nombre: {nombre}\nEdad: {i["edad"]}")
            largo=max(nombres, key=len)
            print(f"El Nombre mas largo es: {largo}")