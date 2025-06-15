carro={}
while True:
    print("1. Agregar Producto")
    print("2. Modificar Cantidad de producto")
    print("3. Eliminar Producto")
    print("4. Calcular Total A Pagar")
    op=input("INGRESE UNA OPCION: ")
    match op:
        case "1":
            producto=input("Ingrese nonmbre de el producto: ")
            precio=int(input("Ingrese precio de el producto: "))
            cantidad=int(input("Ingrese cantidad: "))
            if producto not in carro:
                carro[producto]={"precio":precio,"cantidad":cantidad}
        case "2":
            for nombre, datos in carro.items():
                print(f"Nombre: {nombre}\nPrecio: {datos["precio"]}\nCantidad: {datos["cantidad"]}")
                print()
            cambiar=input("Ingrese nombre de el producto que desea cambiar: ")
            for nombre, datos in carro.items():
                if cambiar in nombre:
                    cantidad=int(input("Ingrese nueva cantidad: "))
                    datos["cantidad"]=cantidad
        case "3":
            for nombre, datos in carro.items():
                print(f"Nombre: {nombre}\nPrecio: {datos["precio"]}\nCantidad: {datos["cantidad"]}")
                print()
            cambiar=input("Ingrese nombre para eliminar: ")
            for nombre, datos in carro.items():
                if cambiar in nombre:
                    del carro[nombre]
                    print(f"Se elimino: {nombre}")
                    break
        case "4":
            total=0
            for nombre, datos in carro.items():
                subtotal=datos["precio"]*datos["cantidad"]
                total+=subtotal
                print(f"Nombre: {nombre}\nPrecio: {datos["precio"]}\nCantidad: {datos["cantidad"]}\nSUBTOTAL: {subtotal}")
                print()
            print(f"El precio total es: {total}")
            