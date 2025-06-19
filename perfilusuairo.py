datos={}
while True:
    print("1. Agregar Usuario")
    print("2. Ver Informacion De Usuarios")
    print("3. Cambiar Informacion")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de usuario: ")
            correo=input("Ingrese correo de usuario: ")
            numero=input("Ingrese numero de telefono: ")
            datos[nombre]={"nombre":nombre,"correo":correo,"numero":numero}
        case 2:
            for n,i in datos.items():
                print(f"Usuario: {i["nombre"]}\nCorreo: {i["correo"]}\nNumero: {i["numero"]}")
                print()
        case 3:
            buscar=input("Ingrese nombre de usuario el cual quiere modificar: ")
            for n,i in datos.items():
                if buscar==n:
                    print("-Usuario")
                    print("-Correo")
                    print("-Numero")
                    op=input("Ingrese elemento que quiere modificar: ")
                    if op=="Usuario":
                        usuarionew=input("Ingrese nuevo nombre de usuario: ")
                        i["nombre"]=usuarionew
                        print("SU USUARIO HA SIDO MODIFICADO")
                        print()
                    elif op=="Correo":
                        correonew=input("Ingrese nuevo Correo: ")
                        i["correo"]=correonew
                        print("SU CORREO HA SIDO MODIFICADO")
                        print()
                    elif op=="Numero":
                        numeronew=input("Ingrese nuevo Numero: ")
                        i["numero"]=numeronew
                        print("SU NUMERO HA SIDO MODIFICADO")
                        print()