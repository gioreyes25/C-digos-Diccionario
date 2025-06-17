datos={}
while True:
    print("1. Agregar Producto")
    print("2. Ver Productos")
    print("3. Ver Producto con mas ventas")
    print("4. ver producto con menos ventas")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de producto: ")
            ventas=input("Ingrese ventas de el producto: ")
            datos[nombre]={"ventas":ventas}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nVentas: {i["ventas"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda nombre:datos[nombre]["ventas"])
            print(f"{mayor} Es El producto con mas ventas: {datos[mayor]["ventas"]}")
        case 4:
            menor=min(datos,key=lambda nombre:datos[nombre]["ventas"])
            print(f"{menor} Es El producto con mas ventas: {datos[menor]["ventas"]}")