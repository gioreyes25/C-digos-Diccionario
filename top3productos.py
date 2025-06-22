datos={}
ventas={
    "Sur":{"total":0,},
    "Centro":{"total":0},
    "Norte":{"total":0},
}
mejorvendido=[]
while True:
    print(mejorvendido)
    print("1. Agregar Producto")
    print("2. Comprar Producto")
    print("3. Ver Mejor Region")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese producto: ").capitalize()
            precio=int(input("Ingrese precio: "))
            datos[producto]={"precio":precio,"cantidad":0}
        case 2:
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}")
                print()
            comprar=input("Ingrese nombre del producto: ").capitalize()
            for n,i in datos.items():
                if comprar==n:
                    print("-Sur")
                    print("-Centro")
                    print("-Norte")
                    sucu=input("Ingrese sucursal: ").capitalize()
                    print()
                    print(f"Sucursal: {sucu}\nProducto Elegido: {comprar}")
                    cantidad=int(input("Ingrese Cantidad que desea: "))
                    i["cantidad"]+=cantidad
                    total=i["precio"]*cantidad
                    if comprar not in ventas[sucu]:
                        ventas[sucu][comprar]=0
                    for n,i in ventas.items():
                        if sucu==n:
                            i[comprar]+=total
                            i["total"]+=total
                    if comprar not in mejorvendido:
                        mejorvendido[comprar]=cantidad
                    else:
                        mejorvendido[comprar]+=cantidad
        case 3:
            mayor=max(ventas,key=lambda sucu:[ventas[sucu]["total"]])
            print(f"La region con mas mejores ventas es {mayor} ${ventas[mayor]["total"]}")
            produs={total:g for total,g in ventas[mayor].items() if total != "total"}
            productomayor=max(produs,key=produs.get)
            produmayornum=produs[productomayor]
            print(f"El producto que mas aporta es {productomayor} con ${produmayornum}")
            
            