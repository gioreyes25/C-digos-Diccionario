datos={}
while True:
    print("1. Agregar Contacto")
    print("2. Ver Todos Los Contactos")
    print("3. Filtrar Contactos")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de contacto: ").capitalize()
            grupo=input("Ingrese grupo al que lo añadira: ").capitalize()
            numero=input("Ingrese numero: ")
            datos[nombre]={"grupo":grupo,"numero":numero}
        case 2:
            for n,i in datos.items():
                print(f"Grupo: {i["grupo"]}\nNombre: {n}\nNumero: {i["numero"]}")
                print()
        case 3:
            f=input("Ingrese grupo de contactos que desea filtrar: ").capitalize()
            for n,i in datos.items():
                if f==i["grupo"]:
                    print(f"Grupo: {i["grupo"]}\nNombre: {n}\nNumero: {i["numero"]}")
                    print()