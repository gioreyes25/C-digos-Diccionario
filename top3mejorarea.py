datos={
    "Panaderia":{"total":0},
    "Carniceria":{"total":0},
    "Fruteria":{"total":0},
}
catalogo={}
import heapq
while True:
    print(datos)
    print()
    print(catalogo)
    print("1. Agregar Producto")
    print("2. Ver listas de productos")
    print("3. Comprar")
    print("4. Ver Top 3 Mejores Areas")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese nombre de producto: ").capitalize()
            precio=int(input("Ingrese precio: "))
            print("1. Panaderia")
            print("2. Carniceria")
            print("3. Fruteria")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                area="Panaderia"
            elif op==2:
                area="Carniceria"
            elif op==3:
                area="Fruteria"
            datos[area][producto]=0
            catalogo[producto]={"precio":precio,"ventas":0,"area":area,"producto":0}
        case 2:
            for n,i in catalogo.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}\nArea: {i["area"]}")
                print()
        case 3:
            for n,i in catalogo.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}\nArea: {i["area"]}")
                print()
            elegir=input("Ingrese producto: ").capitalize()
            if elegir in catalogo:
                canti=int(input("Ingrese cantidad: "))
                total=i["precio"]*canti
                #datos[elegir]["total"]+=total
                catalogo[elegir]["ventas"]+=canti
                print(f"Ha comprado {canti}u de {elegir}")
                datos[i["area"]][elegir]+=total
                datos[i["area"]]["total"]+=total
                catalogo[elegir]["producto"]+=total
        case 4:
            top=heapq.nlargest(3,datos.items(),key=lambda x:x[1]["total"])
            print(top)
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i} {n} {v["total"]}")
                top2=heapq.nlargest(3,catalogo.items(),key=lambda x:x[1]["producto"])
                for i,(n,v) in enumerate(top2,start=1):
                    if v["producto"] in datos[area].values():
                        print(f"- {n} {v["producto"]}")
                