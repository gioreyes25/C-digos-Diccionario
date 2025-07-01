datos={}
while True:
    print("1. Agregar Pelicula")
    print("2. Ver Peliculas")
    print("3. Comprar Entradas")
    print("4. Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            peli=input("Ingrese nombre de la pelicula: ").title()
            precio=int(input("Ingrese precio de entrada: "))
            datos[peli]={"precio":precio,"total":0,"vendidas":0}
        case 2:
            for n,i in datos.items():
                print(f"Pelicula: {n}\nPrecio De Entrada: {i["precio"]}\nEntradas Vendidas: {i["vendidas"]}\nGanancias Totales: {i["total"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Pelicula: {n}\nPrecio De Entrada: {i["precio"]}")
                print()
            elegir=input("Ingrese pelicula que desea ver: ").title()
            if elegir in datos:
                cantidad=int(input("Ingrese cantidad de entradas: "))
                for n,i in datos.items():
                    if elegir==n:
                        total=cantidad*i["precio"]
                        i["total"]+=total
                        i["vendidas"]+=cantidad
                print(f"Ha comprado {cantidad} Entradas Para {elegir}")
        case 4:
            import heapq
            print("1. Ver Top Pelicula Con Mas Ganancias")
            print("2. Ver Top Peliculas Con Entradas Vendidas")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["total"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} Ganancias Totales: {v["total"]}")
                case 2:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["vendidas"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} Entradas Vendidas: {v["vendidas"]}")