import heapq
datos={}
while True:
    print("1. Agregar Producto")
    print("2. Ver List De Productos")
    print("3. Comprar")
    print("4. Ver Mejores 3 Productos")
    op=int(input("Ingrese op: "))
    match op:
        case 1:
            name=input("Ingerse nombre de producto: ").capitalize()
            precio=int(input("Ingrese precio: "))
            datos[name]={"precio":precio,"ventas":0,"total":0}
        case 2:
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}")
                print()
            compar=input("Ingrese nombre de producto que comprara: ").capitalize()
            if compar in datos:
                print(f"Producto Seleccionado: {compar}")
                canti=int(input("Ingrese cantidad: "))
                total=datos[compar]["precio"]*canti
                datos[compar]["ventas"]+=canti
                datos[compar]["total"]+=total
        case 4:
            top=heapq.nlargest(3,datos.items(),key=lambda x:x[1]["total"])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- Producto: {n} Ventas: {v["ventas"]} Total {v["total"]}")