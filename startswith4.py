datos={}
while True:
    print("1. Registrar Productos: ")
    print("2. Ver Productos")
    print("3. Filtrar Productos")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de el producto: ")
            precio=int(input("Ingrese precio de el producto: "))
            datos[nombre]={"precio":precio}
        case 2:
            print(f"Productos Totales: {len(datos)}")
            for n,i in datos.items():
                print(f"Nombre: {n}\nPrecio: {i["precio"]}")
                print()
        case 3:
            fil=input("Ingrese letra para filtar productos que comienzen con ella: ")
            for n,i in datos.items():
                if n.lower().startswith(fil):
                    print(f"Nombre: {n}\nPrecio: {i["precio"]}")
                    print()