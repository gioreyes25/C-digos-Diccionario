datos={}
region={
    "Sur":{"total":0},
    "Centro":{"total":0},
    "Norte":{"total":0},
}
while True:
    print(datos)
    print()
    print(region)
    print("1. Agregar Producto")
    print("2. Ver Productos")
    print("3. Comprar")
    print("4. Ver Top ")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese nombre de el producto: ").title()
            precio=int(input("Ingrese precio: "))
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                sucu="Sur"
            elif op==2:
                sucu="Centro"
            elif op==3:
                sucu="Norte"
            datos[producto]={"total":0,"precio":precio,"sucu":sucu}
        case 2:
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}\nSucursal: {i["sucu"]}\nTotal: {i["total"]}")
                print()
        case 3:
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            sucursal=input("Ingrese sucursal: ")
            for n,i in datos.items():
                if sucursal==i["sucu"]:
                    print(f"Producto: {n}\nPrecio: {i["precio"]}\nSucursal: {i["sucu"]}")
                    print()
            elegir=input("Ingrese producto que comprara: ").title()
            if elegir in datos:
                cantidad=int(input("Ingrese cantidad que comprara: "))
                for n,i in datos.items():
                    if elegir==n:
                        total=cantidad*i["precio"]
                        i["total"]+=total
                        if i["sucu"] not in region:
                            region[i["sucu"]]={"total":total}
                            
                        else:
                            for v,e in region.items():
                                if sucursal==v:
                                    e["total"]+=total
        case 4:
            import heapq
            print("1. Ver Region Con Mas Ingresos")
            print("2. Ver Los Productos Que Mas Aportan: ")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,region.items(),key= lambda x:x[1]["total"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} Ganancias Totales: {v["total"]}")
                case 2:
                    print("1. Sur")
                    print("2. Centro")
                    print("3. Norte")
                    fa=input("Ingrese sucursal para filtrar productos: ").title()
                    fil=[(k,v) for k,v in datos.items() if v["sucu"]==fa]
                    top1=heapq.nlargest(3,fil,key= lambda x:x[1]["total"])
                    print(f"Top 3 productos que mas aportan a la sucursal {fa}")
                    for i,(n,v) in enumerate(top1,start=1):
                        print(f"{i}- {n} {v["total"]}")