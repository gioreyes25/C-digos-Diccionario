datos={}
while True:
    print("1. Agregar Album")
    print("2. Ver ")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            album=input("Ingrese nombre de cancion: ")
            año=input("Ingrese año: ")
            id=input("Ingrese id: ")
            datos={id:[album,año]}
        case 2:
            for id, valores in datos.items():
                print(f"ID: {id}")
                for valor in valores:
                    print(f" - {valor}")
