datos={}
registros={}
while True:
    print("1. Trabajar ")
    print("2. Ver Regiones ")
    print("3. Ver Mejores Regiones")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            print("1. Venta De Armas")
            print("2. Venta De Cobre")
            print("3. Venta De Uvas")
            op=int(input("Ingrese area: "))
            match op:
                case 1:
                    area="Venta De Armas"
                    print("1. AK-47 $500u")
                    print("2. Scar-15 $455u")
                    print("3. MP5 $375u")
                    op=int(input("Ingrese una opcion: "))
                    cantidad=int(input("Ingrese cantidad: "))
                    if op==1:
                        arma="AK-47"
                        total=cantidad*500
                        precio=500
                    elif op==2:
                        arma="Scar-15"
                        total=cantidad*455
                        precio=455
                    elif op==3:
                        arma="MP5"
                        total=cantidad*375
                        precio=375
                    if arma not in datos:
                        datos[arma]={"area":area,"total":0,"precio":precio,"cantidad":cantidad}
                        for n,i in datos.items():
                            if arma ==n:
                                i["total"]=total
                    else:
                        for n,i in datos.items():
                            if arma==n:
                                i["total"]+=total
                                i["cantidad"]+=cantidad
                case 2:
                    area="Venta De Cobre"
                    print("1. 1000KG $2300")
                    cobre="Cobre 1000KG"
                    precio=2300
                    cantidad=int(input("Ingrese cantidad: "))
                    total=cantidad*2300
                    if cobre not in datos:
                        datos[cobre]={"area":area,"total":0,"precio":precio,"cantidad":cantidad}
                        for n,i in datos.items():
                            if cobre==n:
                                i["total"]=total
                    else:
                        for n,i in datos.items():
                            if cobre==n:
                                i["total"]+=total
                                i["cantidad"]+=cantidad
                case 3:
                    area="Venta De Uvas"
                    print("1. Uva Rosh $70u")
                    print("2. Uva Kajika $55u")
                    print("3. Uva Belma $95u")
                    op=int(input("Ingrese una opcion: "))
                    cantidad=int(input("Ingrese cantidad: "))
                    if op==1:
                        uva="Uva Rosh"
                        total=cantidad*70
                        precio=70
                    elif op==2:
                        uva="Uva Kajika"
                        total=cantidad*55
                        precio=55
                    elif op==3:
                        uva="Uva Belma"
                        total=cantidad*95
                        precio=95
                    if uva not in datos:
                        datos[uva]={"area":area,"total":0,"precio":precio,"cantidad":cantidad}
                        for n,i in datos.items():
                            if uva==n:
                                i["total"]=total
                    else:
                        for n,i in datos.items():
                            if uva==n:
                                i["total"]+=total
                                i["cantidad"]+=cantidad
        case 2:
            print("-Venta De Armas")
            print("-Venta De Cobre")
            print("-Venta De Uvas")
            op=input("Ingrese area: ").title()
            print(op)
            for n,i in datos.items():
                if op==i["area"]:
                    print(f"Producto: {n}\nPrecio: {i["precio"]}u\nGanancias: {i["total"]}")
                    print()
        case 3:
            print("1. Ver Las Productos Con mas Ganacias")
            print("2. Ver Area En Especifico")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    import heapq
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["total"])
                    for i,(n,v) in enumerate (top,start=1):
                        print(f"{i}- Area: {n} Ganancias: ${v["total"]} Ventas Totales: {v["cantidad"]}")
                case 2:
                    print("-Venta De Armas")
                    print("-Venta De Cobre")
                    print("-Venta De Uvas")
                    fil=input("Ingrese un area: ").title()
                    fil1=[(k, v) for k, v in datos.items() if v["area"] == fil]
                    print(f"Mejores 3 Productos De {fil}")
                    top2=heapq.nlargest(3,fil1,key= lambda x:x[1]["total"])
                    for i,(n,v) in enumerate(top2,start=1):
                        print(f"{i}- Producto: {n} Ganancias: ${v["total"]} Ventas Totales: {v["cantidad"]}")