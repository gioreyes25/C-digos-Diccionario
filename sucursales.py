datos={}
ventas={}
v=0
while True:
    print("1. Agregar Productos")
    print("2. Comprar")
    print("3. Ver Producto Mas Rentable")
    print("4. Ver Historial De Ventas:")
    print("5. Ver Ventas Por Sucursal")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de producto: ").title()
            precio=int(input("Ingrese precio: "))
            datos[nombre]={"precio":precio,"cantidad":0}
        case 2:
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}")
            producto=input("Ingrese producto que desea comprar: ").title()
            for n,i in datos.items():
                if producto==n:
                    print("-Santiago Centro")
                    print("-Providencia")
                    print("-Las Condes")
                    sucursal=input("Ingrese Sucursal De Cual Compra: ").title()
                    cantidad=int(input("Ingrese cantidad que desea: "))
                    total=i["precio"]*cantidad
                    i["cantidad"]+=cantidad
                    v+=1
                    ventas[v]={"producto":producto,"sucursal":sucursal,"cantidad":cantidad,"total":total}
        case 3:
            mayor=max(datos,key=lambda nombre:datos[nombre]["cantidad"])
            print(f"El Producto {mayor} Es el mas rentable con {datos[mayor]["cantidad"]} Ventas")
        case 4:
            print(f"Ventas Totales: {len(ventas)}")
            for n,i in ventas.items():
                print(f"Sucursal: {i["sucursal"]}\nProducto: {i["producto"]}\nCompra {i["cantidad"]}u\nTotal: {i["total"]}")
                print()
        case 5:
            sucu=input("Ingrese sucursal que desea buscar: ").title()
            for n,i in ventas.items():
                if sucu==i["sucursal"]:
                    print(f"Sucursal: {i["sucursal"]}\nProducto: {i["producto"]}\nCompra {i["cantidad"]}u\nTotal: {i["total"]}")
                    print()