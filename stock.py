datos=[]
Produ={}
codigo=-1
while True:
    print("1. Agregar Productos: ")
    print("2. Comprar Stock")
    print("3. Vender Stock")
    print("4. Salir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            cantidad=int(input("Ingrese cantiddad de porductos"))
            for i in range(cantidad):
                codigo+=1
                nombre=input("Ingrese nombre:")
                precio=int(input("Ingrese precio de el producto: "))
                stock=int(input("Ingrese stock: "))
                produ={
                    "codigo":codigo,
                    "nombre":nombre,
                    "precio":precio,
                    "stock":stock
                }
                datos.append(produ)
        case 2:
            for i in datos:
                print(f"Codigo: {i["codigo"]} Nombre: {i["nombre"]} Cantidad: {i["stock"]}")
            agregar=int(input("Ingrese el codigo de producto que desea "))
            for i in datos:
                (f"Codigo: {i["codigo"]} Nombre: {i["nombre"]} Cantidad: {i["stock"]}")
                if i["codigo"]==agregar:
                    suma=int(input("Ingrese cantidad: "))
                    i["stock"]+=suma
                    print(f"Ahora tiene un stock de {i["stock"]}")
        case 3:
            for i in datos:
                print(f"Codigo: {i["codigo"]} Nombre: {i["nombre"]} Cantidad: {i["stock"]}")
            vender=int(input("Ingrese el codigo de producto que desea vender: "))
            for i in datos:
                (f"Codigo: {i["codigo"]} Nombre: {i["nombre"]} Cantidad: {i["stock"]}")
                if i["codigo"]==vender:
                    resta=int(input("Ingrese cantidad que desea vender"))
                    i["stock"]-=resta
                    print(f"Ahora tiene un stock de {i["stock"]}")
        case 4:
            break