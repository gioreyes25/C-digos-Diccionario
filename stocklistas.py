datos=[]
while True:
    print("1. Agregar Producto")
    print("2. Ver Tabla De Productos")
    print("3. Comprar Stock")
    print("4. Vender Stock")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            producto=input("Ingrese nombre de el producto: ").capitalize()
            precio=int(input("Ingrese precio: "))
            cantidad=10
            info={"producto":producto,"precio":precio,"cantidad":cantidad}
            datos.append(info)
        case 2:
            for i in datos:
                if i["cantidad"]<5:
                    print(F"Bajo stock {i["producto"]}\nPrecio: {i["precio"]}\nStock: {i["cantidad"]}")
                    print()
                else:
                    print(F"{i["producto"]}\nPrecio: {i["precio"]}\nStock: {i["cantidad"]}")
                    print()
            menor=min(datos,key=lambda x:x["cantidad"])
            print(f"El producto que menor cantidad tiene es {menor["producto"]} {menor["cantidad"]}")
        case 3:
            for i in datos:
                print(f"Producto: {i["producto"]}\nPrecio: {i["precio"]}\nStock: {i["cantidad"]}")
                print()
            buscar=input("Ingrese producto que desea comprar: ").capitalize()
            for i in datos:
                if buscar==i["producto"]:
                    canti=int(input("Ingrese cantidad que desea comprar: "))
                    i["cantidad"]+=canti
                    print(f"Ha comprado {canti}u a {i["producto"]}")
        case 4:
            for i in datos:
                print(f"Producto: {i["producto"]}\nPrecio: {i["precio"]}\nStock: {i["cantidad"]}")
                print()
            vender=input("Ingrese producto que desea vender: ").capitalize()
            for i in datos:
                if vender==i["producto"]:
                    canto=int(input("Ingrese cantidad que desea vender: "))
                    i["cantidad"]-=canto
                    print(f"Ha vendido {canto}u a {i["producto"]}")
        