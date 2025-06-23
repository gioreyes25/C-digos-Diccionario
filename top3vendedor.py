datos={}
mejor=[]


import heapq
while True:
    print("1. Agregar Vendedor")
    print("2. Ver Lista de vendedores")
    print("3. Borrar Vendedor")
    print("4. Ver Mejores 3 ")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            name=input("Ingrese nombre: ").capitalize()
            ventas=int(input("Ingrese ventas que obtuvo este mes: "))
            datos[name]={"ventas":ventas}
            mejor.append((name,ventas))
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nVentas Mensuales: {i["ventas"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Nombre: {n}\nVentas Mensuales: {i["ventas"]}")
                print()
            eliminar=input("Ingrese nombre que desa eliminar: ").capitalize()
            if eliminar in datos:
                del datos[eliminar]
                print(f"Se ha eliminado a vendedor {eliminar}")
        case 4:
            top=heapq.nlargest(3,mejor,key=lambda x:x[1])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {n} {v:.0f}")