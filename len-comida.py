datos={}
comidas=[]
while True:
    print("1. Agregar Comida")
    print("2. Contar Comidas")
    op=int(input("Ingreseminma opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese una opcion: ")
            datos[nombre]={}
            comidas.append(nombre)
        case 2:
            mas5=0
            print(f"Total de comidas: {len(datos)}")
            for nombre,i in datos.items():
                print(f"Nombre: {nombre}")
                contar=len(nombre)
                if contar>5:
                    mas5+=1
            print(f"{mas5} Comida Tienen mas de 5 palabras")
            maslarga=max(comidas,key=len)
            print(f"La comida mas larga es: {maslarga}")