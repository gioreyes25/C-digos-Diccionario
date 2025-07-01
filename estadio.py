datos={}
while True:
    print("1. Agregar Vendedor")
    print("2. Ver Vendedor")
    print("3. Dar Ganancias")
    print("4. Ver Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de vendedor: ").title()
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                region="Sur"
            elif op==2:
                region="Centro"
            elif op==3:
                region="Norte"
            datos[nombre]={"region":region,"ganancias":0}
        case 2:
            for n,i in datos.items():
                print(f"Vendedor: {n}\nRegion: {i["region"]}\nGanancias: {i["ganancias"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Vendedor: {n}\nRegion: {i["region"]}")
                print()
            elegir=input("Ingrese nombre de el vendedor: ").title()
            if elegir in datos:
                ingresos=int(input(f"Ingrese cantidad de dinero que dara a {elegir}"))
                for n,i in datos.items():
                    if elegir==n:
                        i["ganancias"]+=ingresos
        case 4:
            import heapq
            print("1. Ver Top 3 Vendedores General")
            print("2. Ver Top 3 Por Region")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["ganancias"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} Ganancias Totales: {v["ganancias"]}")
                case 2:
                    print("1. Sur")
                    print("2. Centro")
                    print("3. Norte")
                    reg=input("Ingrese region que filtrara: ").title()
                    fil=[(k,v) for k,v in datos.items() if v["region"]==reg]
                    top=heapq.nlargest(3,fil,key=lambda x:x[1]["ganancias"])
                    print(f"Top 3 Vendedores de La Region {reg}")
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} Ganancias Totales: {v["ganancias"]}")