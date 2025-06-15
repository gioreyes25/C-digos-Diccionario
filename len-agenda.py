datos={}
while True:
    print("1. Agregar Contacto")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre")
            telefono=input("Ingrese numero de ntelefono: ")
            datos[nombre]={"telefono":telefono}
        case 2:
            print(len(datos))