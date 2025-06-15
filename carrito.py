carro={}
while True:
    print("1. Agregar Producto")
    print("2. Modificar Cantidad de producto")
    print("3. Eliminar Producto")
    print("4. Calcular Total A Pagar")
    print("5. Mostar Detalle de el carrito")
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
        case "3":
            buscar=input("Ingrese elemento: ")
            for nombre, datos in carro.items():
                if buscar==nombre:
                    print(f"Nombre: {nombre}\nPrecio: {datos["precio"]}\nCantidad: {datos["cantidad"]}")