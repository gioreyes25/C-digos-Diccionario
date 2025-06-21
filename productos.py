datos=[]
while True:
    print(datos)
    print("1. Agregar Productos")
    print("2. Ver tabla de productos")
    print("3. Ver Producto mas caro")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese nombre de el producto: ").capitalize()
            precio=int(input("Ingrese precio de el producto: "))
            info={"producto":producto,"precio":precio}
            datos.append(info)
        case 2:
            for i in datos:
                print(f"Producto: {i["producto"]}\nPrecio: {i["precio"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda x:x["precio"])
            print(f"El producto mas caro es {mayor["producto"]}, su precio es {mayor["precio"]}")