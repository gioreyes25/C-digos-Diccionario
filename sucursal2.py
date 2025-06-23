ventas = {
    "Sur": {"total":0},
    "Centro": {"total":0},
    "Norte": {"total":0}
}
sucursal = {
    "Sur": {},
    "Centro": {},
    "Norte": {}
}
datos=[]
import heapq
while True:
    print(ventas)
    print(datos)
    print("1. Agregar Producto")
    print("2. Ver Lista De Productos")
    print("3. Comprar")
    print("4. Ver Top")
    op = int(input("Ingrese una opcion: "))
    
    match op:
        case 1:
            producto=input("Ingrese nombre de producto: ").capitalize()
            precio=int(input("Ingrese precio: "))
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            op=int(input("Ingrese area que desea agregar producto: "))
            if op==1:
                region="Sur"
            elif op==2:
                region="Centro"
            elif op==3:
                region="Norte"
            info={"producto":producto,"total":0}
            datos.append(info)
            if producto not in sucursal[region]:
                sucursal[region][producto]=precio
            else:
                print("Producto Ya Existe")
        case 2:
            for region, productos in sucursal.items():
                print(f"Region: {region}")
                for name,precio in productos.items():
                    if name!="total":
                        print(f"-{name} {precio}")
        case 3:
            for region, productos in sucursal.items():
                print(f"Region: {region}")
                if not productos:
                    print()
                for name,precio in productos.items():
                    print(f"-{name} {precio}")
            sucu=input("Ingrese Sucursal en la que desea Comprar: ").capitalize()
            for region, productos in sucursal.items():
                if sucu==region:
                    print(f"Region: {region}")
                    for name,precio in productos.items():
                        print(f"-{name} {precio}")
                    elegir=input("Ingrese producto que va a comprar: ").capitalize()
                    if elegir in sucursal[region]:
                        print(f"Producto Elegido: {elegir}")
                        cantidad=int(input("Ingrese cantidad que comprara: "))
                        for name,precio in productos.items():
                            if elegir==name:
                                total=precio*cantidad
                        if elegir not in ventas[sucu]:
                            ventas[sucu][elegir]=total
                            ventas[sucu]["total"]+=total
                        else:
                            ventas[sucu][elegir]+=total
                            ventas[sucu]["total"]+=total
        case 4:
                top=heapq.nlargest(3,ventas.items(),key=lambda x:x[1]["total"])
                for i,(name,valor) in enumerate(top,start=1):
                    print(f"{i} {name} {valor["total"]}")
                    producto={total:g for total,g in ventas.items() if total != "total"}
                    top2=heapq.nlargest(3,producto,key=lambda x:x[1])
                    for i,(b,v) in enumerate(top2,start=1):
                        print(f"{i} {name} {v:.0f}")
        case 5:
            pan=input("Ingrese un pan. ").capitalize()
            for i in datos:
                if pan==i["producto"]:
                    print("JAJ")