datos={}
nombres=[]
while True:
    print("1. Añadir Nombres")
    print("2. Mostrar Nombres")
    print("3. Mostrar Nombre Mas corto")
    print("4. Mostar Nombre Con mas de 6 letras")
    print("5. Mostrar Nombres Que Empiezen Con A")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre: ")
            datos[nombre]={}
            nombres.append(nombre)
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}")
                print()
        case 3:
            Corto=min(nombres,key=len)
            print(f"El nombre Mas Corto es: {Corto}")
        case 4:
            print(f"Nombres Con Mas de 6 letras: ")
            for nombre,i in datos.items():
                Mas6=len(nombre)
                if Mas6>6:
                    print(f"Nombre: {nombre}")
        case 5:
            for nombre in nombres:
                if datos[nombre][0]=="a":
                    print(f"Nombre: {nombre}")