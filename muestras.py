datos={}
while True:
    print(datos)
    print("1. Agregar Muestras")
    print("2. Ver Laboratorios")
    print("3. Vender Muestras")
    print("4. Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            print("-Sangre")
            print("-ADN")
            print("-Embarazo")
            muestra=input("Ingrese una opcion: ").capitalize()
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            op=int(input("Ingrese laboratorio"))
            if op==1:
                labo="Sur"
            elif op==2:
                labo="Centro"
            elif op==3:
                labo="Norte"
            datos[muestra]={"total":0,"labo":labo}
        case 2:
            print("1. Sur")
            print("2. Norte")
            print("3. Centro")
            lab=input("Ingrese laboratorio que dese ver: ").capitalize()
            print(F"Laboratorio {lab}")
            for n,i in datos.items():
                if lab==i["labo"]:
                    print(f"Muestra: {n}\nCantidad: {i["total"]}")
        case 3:
            print("1. Sur")
            print("2. Norte")
            print("3. Centro")
            lab=input("Ingrese laboratorio que desea agregar muestras: ").capitalize()
            print(F"Laboratorio {lab}")
            for n,i in datos.items():
                if lab==i["labo"]:
                    print(f"Muestra: {n}\nCantida: {i["total"]}")
            elegir=input("Ingrese muestra que comprara: ").capitalize()
            for n,i in datos.items():
                if elegir==n:
                    cantidad=int(input("Ingrese cantidad: "))
                    i["total"]+=cantidad
        case 4:
            import heapq
            print("1. Ver Los Mas Alos En General")
            print("2. Ver Por Laboratorio")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["total"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} {v["total"]} {v["labo"]}")
                case 2:
                    print("1. Sur")
                    print("2. Norte")
                    print("3. Centro")
                    lab=input("Ingrese laboratorio que desea buscar: ").capitalize()
                    fil=[(k,v) for k,v in datos.items() if v["labo"]==lab]
                    top1=heapq.nlargest(3,fil,key=lambda x:x[1]["total"])
                    print(f"Muestras de Laboratorio {lab}")
                    for i,(n,v) in enumerate(top1,start=1):
                       print(f"{i}- {n} {v["total"]}")
                    