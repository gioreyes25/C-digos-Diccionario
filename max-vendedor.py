datos={}
while True:
    print("1. Agregar Vendedor")
    print("2. Ver Tabla De Ventas")
    print("3. Ver Mejor Vendedor")
    print("4. Ver Peor Vendedor")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre")
            edad=input("Ingrese Edad: ")
            Ventas=input("Ingrese Ventas Mensuales: ")
            datos[nombre]={"edad":edad,"ventas":Ventas}
        case 2:
            print(f"Cantidad de Vendedores Registrados: {len(datos)}")
            for n,i in datos.items():
                print(f"Nombre: {n}\nEdad: {i["edad"]}\nVentas Mensuales: {i["ventas"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda x:datos[x]["ventas"])
            print(f"{mayor} Es el Mejor Vendedor Con {datos[mayor]["ventas"]} Ventas Mensuales")
        case 4:
            menor=min(datos,key=lambda x:datos[x]["ventas"])
            print(f"{menor} Es el Peor Vendedor Con {datos[menor]["ventas"]} Ventas Mensuales")