datos={}
while True:
    print("1. Comprar Maquina")
    print("2. Ver Tabla")
    print("3. Ver Maquina Que Mas Genera")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            maquina=input("Ingrese nombre de la maquina: ")
            t=int(input("Ingresa la cantidad que tornillos produce por dia: "))
            c=int(input("Ingresa la cantidad que clavos produce por dia: "))
            total=c+t
            datos[maquina]={"tornillos":t,"clavos":c,"total":total}
        case 2:
            for n,i in datos.items():
                print(F"Nombre: {n}\nProduccion x Dia: {i["cantidad"]}")
                print()
        case 3:
            print(datos)
            mayor=max(datos,key=lambda maquina:datos[maquina]["total"])
            produ={total : pro for total,pro in datos[mayor].items() if total != "total"}
            produccion=max(produ,key=produ.get)
            nameprodu=produ[produccion]
            print(f"La mejor maquina es: {mayor} y el producto que mas\n aporta es: {produccion} con {nameprodu}")
            
            