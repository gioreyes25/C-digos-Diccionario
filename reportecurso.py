datos=[]
regiones={
    "Sur":{"total":0},
    "Centro":{"total":0},
    "Norte":{"total":0}
}
productostop={}
while True:
    print(regiones)
    print("1. Agregar Producto")
    print("2. Ver Productos")
    print("3. Comprar Producto")
    print("4. Ver Region Mas Rentable")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese producto: ").capitalize()
            precio=int(input("Ingrese precio: "))
            productos={"producto":producto,"precio":precio}
            datos.append(productos)
        case 2:
            for i in datos:
                print(f"Nombre: {i["producto"]}\nPrecio: {i["precio"]}")
                print()
        case 3:
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            sucursal=input("Ingrese sucursal desde cual va a comprar: ").capitalize()
            for i in datos:
                print(f"Nombre: {i["producto"]}\nPrecio: {i["precio"]}")
                print()
            comprar=input("Ingrese nombre de producto que va a comprar: ").capitalize()
            for i in datos:
                if comprar==i["producto"]:
                    print(f"Producto Seleccionado: {i["producto"]}")
                    cantidad=int(input("Ingrese Cantidad que desea: "))
                    total=i["precio"]*cantidad
                    if comprar not in regiones[sucursal]:
                        regiones[sucursal][comprar]=0
                    for n,i in regiones.items():
                        if sucursal==n:
                            i[comprar]+=total
                            i["total"]+=total
                    if comprar not in productostop:
                        productostop[comprar]={"total":0}
                    for n,i in productostop.items():
                        if comprar==n:
                            i["total"]+=total
        case 4:
            mayor=max(regiones,key=lambda region:regiones[region]["total"])
            print(f"La mayor es: {mayor}")
            productos = {total: produ for total, produ in regiones[mayor].items() if total != 'total'}
            print(productos)
            producto_max = max(productos, key=productos.get)
            print(producto_max)
            cantidad_aporte = productos[producto_max]
            print(cantidad_aporte)
            regiontotal=regiones[mayor]["total"]
            print(regiontotal)
            print(f"La región con más ganancias es: {mayor} (${regiontotal})")
            print(f"El producto que más aporta es: {producto_max} (${cantidad_aporte})")