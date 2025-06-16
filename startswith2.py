datos={}
while True:
    print("1. Registar Comidas")
    print("2. Ver")
    print("3. Filtrar Resultados")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de cliente: ")
            comida=input("Ingrese comida: ")
            datos[nombre]={"comida":comida}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nComida Fav: {i["comida"]}")
        case 3:
            l=input("Ingrese letra que desea filtrar comidas: ")
            for n,i in datos.items():
                if i["comida"].lower().startswith(l):
                    print(f"Nombre: {n}\nComida Fav: {i["comida"]}")
        
            