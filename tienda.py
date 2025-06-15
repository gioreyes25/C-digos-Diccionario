tienda={}
historial={}
ventastotales=0
while True:
    print("1. Agregar Producto")
    print("2. Ver Catalogo")
    print("3. Realizar Venta")
    print("4. Ver Historial De Ventas")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese nombre: ")
            producto=producto.capitalize()
            precio=int(input("Ingrese precio: "))
            cantidad=int(input("Ingrese cantidad: "))
            tienda[producto]={"precio":precio,"cantidad":cantidad}
        case 2:
            for nombre,i in tienda.items():
                print(f"Nombre: {nombre}\nPrecio: {i["precio"]}\nCantidad: {i["cantidad"]}")
                print()
        case 3:
            for nombre,i in tienda.items():
                print(f"Nombre: {nombre}\nPrecio: {i["precio"]}\nCantidad: {i["cantidad"]}")
                print()
            venta=input("Ingrese nombre de producto: ")
            venta=venta.capitalize()
            for nombre,i in tienda.items():
                if venta in nombre:
                    if i["cantidad"]==0:
                        print("NO TIENE STOCK")
                        break
                    print("PRODUCTO SELECCIONADO: ")
                    print(f"Nombre: {nombre}\nPrecio: {i["precio"]}\nCantidad: {i["cantidad"]}")
                    print()
                    cantidad=int(input("Ingrese cantidad que desea: "))
                    i["cantidad"]-=cantidad
                    subtotal=i["precio"]*cantidad
                    print(f"El Total de esta compra es: {subtotal}")
                    historial[venta]={"cantidad":cantidad,"subtotal":subtotal}
                    ventastotales+=1
        case 4:
            print("HISTORIAL DE VENTAS")
            print(f"Total se han hecho {ventastotales} Ventas ")
            for nombre,i in historial.items():
                print(f"Producto: {nombre}\nCantidad: {i["cantidad"]}\nTotal: {i["subtotal"]}")
                print()
    