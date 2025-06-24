datos={}
ventas={
    "Sur":{"total":0},
    "Centro":{"total":0},
    "Norte":{"total":0}
}
registro={}
while True:
    print("\n1. Agregar Producto")
    print("2. Ver Lista De Productos")
    print("3. Comprar")
    print("4. Ver Mejor")
    op=int(input("Ingrese una op: "))
    match op:
        case 1:
            producto=input("Ingrese nombre de el producto: ").capitalize()
            precio=int(input("Ingrese precio de producto: "))
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                sucursal="Sur"
            elif op==2:
                sucursal="Centro"
            elif op==3:
                sucursal="Norte"
            print("1. Panaderia")
            print("2. Carniceria")
            print("3. Fruteria")
            op2=int(input("Ingrese una opcion: "))
            if op2==1:
                area="Panaderia"
            elif op2==2:
                area="Carniceria"
            elif op2==3:
                area="Fruteria"
            datos[producto]={"area":area,"sucursal":sucursal,"precio":precio}
        case 2:
            print("1. Panaderia")
            print("2. Carniceria")
            print("3. Fruteria")
            fil=input("Ingrese area que desea filtrar: ").capitalize()
            for n,i in datos.items():
                if i["area"]==fil:
                    print(f"Producto: {n}\nPrecio: {i["precio"]}\nSucursal: {i["sucursal"]}\nArea: {i["area"]}")
                    print()
        case 3:
            print("1. Panaderia")
            print("2. Carniceria")
            print("3. Fruteria")
            fil=input("Ingrese area que desea filtrar: ").capitalize()
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            sucu=input("Ingrese sucursal que desea filtrar: ").capitalize()
            for n,i in datos.items():
                if i["area"]==fil and i["sucursal"]==sucu:
                    print(f"Producto: {n}\nPrecio: {i["precio"]}\nSucursal: {i["sucursal"]}\nArea: {i["area"]}")
                    print()
            elegir=input("Ingrese producto que desea comprar: ").capitalize()
            for n,i in datos.items():
                if elegir==n:
                    cantidad=int(input("Ingrese cantidad: "))
                    print(f"Ha comprado {cantidad}u de {elegir}")
                    total=i["precio"]*cantidad
                    if elegir not in ventas[sucu]:
                        ventas[sucu][elegir]=total
                        ventas[sucu]["total"]+=total
                    else:
                        ventas[sucu][elegir]+=total
                        ventas[sucu]["total"]+=total
                    if elegir not in registro:
                        registro[elegir]={"producto":elegir,"total":total,"area":fil,"sucursal":sucu}
                    else:
                        for n,i in registro.items():
                            if elegir==n:
                                i["total"]+=total
        case 4:
            import heapq
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            ele=input("Ingrese sucursal que desea filtrar: ").capitalize()
            print("1. Panaderia")
            print("2. Carniceria")
            print("3. Fruteria")
            ala=input("Ingrese area que filtrara: ").capitalize()
            print(f"TOP 3 PRODUCTOS DE SUCURSAL {ele}, AREA: {ala}")
            filtrados = [(k, v) for k, v in registro.items() if v["sucursal"] == ele]
            filtrados2 = [(k, v) for k, v in filtrados if v["area"] == ala]
            top=heapq.nlargest(3,filtrados2,key=lambda x:x[1]["total"])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {n}-{v["sucursal"]}-{v["area"]}-{v["total"]}")

                
            
            