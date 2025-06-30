datos={}
numn="1234567890"
while True:
    print("1. Agregar Usuario")
    print("2. Buscar Usuario")
    print("3. Eliminar Usuario")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            usuario=input("Ingrese usuario").capitalize()
            if usuario not in datos:
                sexo=input("Ingrese sexo (F o M)").capitalize()
                if sexo == "F" or sexo=="M":
                    print("bien")
                    contraseña=input("Ingrese contraseña min 8 caracteres").capitalize()
                    if len(contraseña)>=8:
                        if contraseña == "1234567890":
                            print("Numeros bien")
                        else:
                            print("Debe tener al menos un numero")
                    else:
                        print("La contraseña tiene menos de 8 caracteres")
                else:
                    print("Solo puede ingresar Letra F o M")
            else:
                print("EL USUARIO YA SE ENCUENTRA REGISTRADO")