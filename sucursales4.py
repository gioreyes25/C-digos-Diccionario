datos={}
ventas={}
v=0
import heapq
while True:
    print(datos)
    print("1. Agregar Producto")
    print("2. Ver Registro De Ventas")
    print("3. Comprar")
    print("4. Ver Top 3 Productos")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese nombre: ").title()
            precio=int(input("Ingrese precio de producto: "))
            print("1. Carniceria")
            print("2. Fruteria")
            print("3. Panaderia")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                area="Carniceria"
            elif op==2:
                area="Fruteria"
            elif op==3:
                area="Panaderia"
            datos[producto]={"precio":precio,"area":area,"cantidad":0,"total":0,"dia":0}
        case 2:
            for n,i in ventas.items():
                print(f"Venta N° {n}\nProducto: {i["producto"]}\nArea: {i["area"]}\nUnidades Vendidas: {i["cantidad"]}\nGanacias Totales: ${i["total"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}\nArea: {i["area"]}\nUnidades Vendidas: {i["cantidad"]}\nGanacias Totales: ${i["total"]}")
                print()
            elegir=input("Ingresr producto Que Comprara: ").title()
            for n,i in datos.items():
                if elegir==n:
                    canti=int(input("Ingrese cantidad que comprara: "))
                    print(f"Ha comprado {canti}u de {elegir}")
                    total=canti*i["precio"]
                    i["total"]+=total
                    i["cantidad"]+=canti
                    v+=1
                    ventas[v]={"producto":producto,"area":area,"cantidad":canti,"total":total}
        case 4:
            print("1. Ver Productos Mas Vendidos General")
            print("2. Ver Areas Con Top 3 Productos ")
            op=int(input("iNGRESE UNA OPCION: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["total"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} ${v["total"]} Unidades Vendidas: {v["cantidad"]}")
                case 2:
                    print("1. Carniceria")
                    print("2. Fruteria")
                    print("3. Panaderia")
                    op=input("Ingrese una op: ").title()
                    filtrados=[(k,v) for k,v in datos.items() if v["area"]==op]
                    top2=heapq.nlargest(3,filtrados,key=lambda x:x[1]["total"])
                    print(f"PRODUCTOS TOP 3 DE AREA {op}")
                    for i,(n,v) in enumerate(top2,start=1):
                        print(f"{i} {n} {v["total"]}")

                        
