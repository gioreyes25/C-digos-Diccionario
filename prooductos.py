datos={}
ventas={
    "Panaderia":{"total":0},
    "Fruteria":{"total":0},
    "Carniceria":{"total":0},
}
while True:
    print("1. Agregar Productos")
    print("2. Ver Productos")
    print("3. Vender")
    print("4. Ver Mejor Area de Ventas")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            print("1. Panaderia")
            print("2. Fruteria")
            print("3. Carniceria")
            op=int(input("Ingrese Tipo De Producto Que Va A Agregar: "))
            if op==1:
                op="Panaderia"
            elif op==2:
                op="Fruteria"
            elif op==3:
                op="Carniceria"
            producto=input("Ingrese nombre de el producto: ").capitalize()
            precio=int(input("Ingrese precio de el producto: "))
            cantidad=10
            datos[producto]={"area":op,"precio":precio,"cantidad":cantidad}
        case 2:
            print("1. Ver Todos Los Productos")
            print("2. Filtrar Productos Por Area")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                for n,i in datos.items():
                    print(f"Area: {i["area"]}\nProducto: {n}\nPrecio: {i["precio"]}\nCantidad: {i["cantidad"]}")
                    print()
            elif op==2:
                print("1. Panaderia")
                print("2. Fruteria")
                print("3. Carniceria")
                op=int(input("Ingrese area que desea ver: "))
                if op==1:
                    op="Panaderia"
                elif op==2:
                    op="Fruteria"
                elif op==3:
                    op="Carniceria"
                print(f"PRODUCTOS DE {op}")
                for n,i in datos.items():
                    if op==i["area"]:
                        print(f"Producto: {n}\nPrecio: {i["precio"]}\nCantidad: {i["cantidad"]}")
                        print()
        case 3:
            print("1. Panaderia")
            print("2. Fruteria")
            print("3. Carniceria")
            op=int(input("Ingrese area que desea vender: "))
            if op==1:
                op="Panaderia"
            elif op==2:
                op="Fruteria"
            elif op==3:
                op="Carniceria"
            print(f"PRODUCTOS DE {op}")
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}\nCantidad: {i["cantidad"]}")
            vender=input("Ingrese producto que vendera: ").capitalize()
            for n,i in datos.items():
                if vender==n:
                    print(f"Producto Seleccionado: {n}")
                    canti=int(input("Ingrese cantidad que vendera: "))
                    total=i["precio"]*canti
                    i["cantidad"]-=canti
                    print(f"Se han vendido {canti}u de {n}, Total {total}")
                    if vender not in ventas[op]:
                        ventas[op][vender]=0
                    else:
                        ventas[op][vender]+=total
                    for n,i in ventas.items():
                        i["total"]+=total
        case 4:
            mayor=max(ventas,key=lambda op:ventas[op]["total"])
            print(f"La mejor area en ventas es {mayor} con un total de ${ventas[mayor]["total"]}")