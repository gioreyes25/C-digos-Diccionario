datos={}
import heapq
while True:
    print(datos)
    print("1. Agregar  Comidas")
    print("2. Ver Listas de comidas")
    print("3. Comer")
    print("4. Ver Mejor Area")
    op=int(input("Ingrese una op: "))
    match op:
        case 1:
            comida=input("Ingrese comida: ").capitalize()
            precio=int(input("Ingrese preci: "))
            total=0
            datos[comida]={"precio":precio,"total":0,"cantidad":0}
        case 2:
            for n,i in datos.items():
                print(f"Comida {n}\nPrecio: {i["precio"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Comida {n}\nPrecio: {i["precio"]}")
                print()
            elegir=input("Ingrese plato de comida de comera: ").capitalize()
            cantidad=int(input("Ingrese cantidad de comensales: "))
            print(f"Ha comprado {cantidad} platos de {elegir}")
            for n,i in datos.items():
                if elegir==n:
                    total=i["precio"]*cantidad
                    i["cantidad"]+=cantidad
                    i["total"]+=total
        case 4:
            top=heapq.nlargest(3,datos.items(),key=lambda x:x[1]["total"])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {n} Cantidad: {v["cantidad"]}- Total: {v["total"]}")