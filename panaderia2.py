datos={}
import heapq
while True:
    print(datos)
    print("1. Agregar Producto")
    print("2. Ver Lista de productos")
    print("3. Comprar")
    print("4. Ver Mejores")
    op=int(input("Ingrese auuna op: "))
    match op:
        case 1:
            producto=input("Ingrese nombre de producto: ").capitalize()
            precio=int(input("Ingrese precio de el producto: "))
            area=input("Ingrese area: ").capitalize()
            datos[producto]={"precio":precio,"total":0,"cantidad":0,"area":area,"c":0}
        case 2:
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}\nArea: {i["area"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Producto: {n}\nPrecio: {i["precio"]}\nArea: {i["area"]}")
                print()
            elegir=input("Ingrese producto que comprara: ").capitalize()
            cantidad=int(input("Ingrese la cantidad: "))
            for n,i in datos.items():
                if elegir==n:
                    print(f"Ha comprado {cantidad}u de {elegir}")
                    total=i["precio"]*cantidad
                    i["total"]+=total
                    i["cantidad"]+=cantidad
        case 4:                
            for n,i in datos.items():
                if i["c"]==0:
                    print(f"Area: {i["area"]}")
                    if i["area"]:
                        i["c"]+=1
                    filtrados = [(k, v) for k, v in datos.items() if v["area"] == i["area"]]
                    top=heapq.nlargest(3,filtrados,key=lambda x:x[1]["total"])
                    for i,(name,v) in enumerate(top,start=1):
                        print(f"{i} {name} {v["cantidad"]} {v["total"]}")
            for n,i in datos.items():
                i["c"]=0