datos=[]
import heapq
while True:
    print("1. Agregar Producto")
    print("2. ver")
    op=int(input("Ingrese op: "))
    match op:
        case 1:
            produ=input("Ingrese producto: ").capitalize()
            precio=int(input("Ingrtese precio: "))
            datos.append((produ,precio))
        case 2:
            top=heapq.nlargest(3,datos,key= lambda x:x[1])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i} {n} {v:.0f}")