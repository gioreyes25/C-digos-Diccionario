agenda={}
datos=[]
while True:
    print("1. Agregar Contacto: ")
    print("2. Consultar Contactos: ")
    print("3. Buscar Contactos Por Nombre: ")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese el nombre: ")
            numero=int(input("Ingrese numero de telefono: "))
            agenda={
                "nombre":nombre,
                "numero":numero
            }
            datos.append(agenda)
        case 2:
            if not datos:
                print("NO TIENE CONTACTOS AGREGADOS")
            for i in datos:
                print(f"Nombre: {i["nombre"]}\nNumero: {i["numero"]}")
        case 3:
            if not datos:
                print("No tiene ningun contacto agregado a su telefono ")
            else:
                for i in datos:
                    (f"Nombre: {i["nombre"]}\nNumero: {i["numero"]}")
                    nombre=input("Ingrese el nombre de el contacto: ")
                    nombre=nombre.capitalize()
                    if nombre==i["nombre"]:
                        print(f"Numero: {i["numero"]}")
                    else:
                        print("No Tiene ningun contacto con ese nombre o se equivoco al ingresar el nombre")