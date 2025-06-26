datos={}
while True:
    print(datos)
    print("1. Agregar Comuna")
    print("2. Ver Ingresos De Comunas")
    print("3. Agregar Ingresos")
    print("4. Ver Top Comunas")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            comuna=input("Ingrese nombre de la comuna: ").title()
            print("1. Santiago")
            print("2. Concepcion")
            print("3. Valparaiso")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                region="Santiago"
            elif op==2:
                region="Concepcion"
            elif op==3:
                region="Valparaiso"
            datos[comuna]={"region":region,"educacion":0,"cultura":0,"comercio":0,"total":0}
        case 2:
            for n,i in datos.items():
                print(f"Region {i["region"]}\nComuna: {n}\nEducacion: ${i["educacion"]}\nCultura: ${i["cultura"]}\nComercio: ${i["comercio"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Region {i["region"]}\nComuna: {n}\nEducacion: ${i["educacion"]}\nCultura: ${i["cultura"]}\nComercio: ${i["comercio"]}")
                print()
            elegir=input("Ingrese comuna que desea: ").title()
            for n,i in datos.items():
                if elegir==n:
                    print("1. Educacion")
                    print("2. Cultura")
                    print("3. Comercio")
                    op=int(input("Ingrese una opcion: "))
                    if op==1:
                        ingreso=int(input("Ingrese cuanto agregara de ingresos: "))
                        i["educacion"]+=ingreso
                        i["total"]+=ingreso
                    if op==2:
                        ingreso=int(input("Ingrese cuanto agregara de ingresos: "))
                        i["cultura"]+=ingreso
                        i["total"]+=ingreso
                    if op==3:
                        ingreso=int(input("Ingrese cuanto agregara de ingresos: "))
                        i["comercio"]+=ingreso
                        i["total"]+=ingreso
        case 4:
            import heapq
            print("1. Ver Comunas TOP 3 Con Mas Ingresos")
            print("2. Ver La Region Y Su Top 3")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["total"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- Region: {v["region"]},Comuna: {n} Ingresos Totales {v["total"]}")
                case 2:
                    print("1. Region Santiago")
                    print("2. Region Valparaiso")
                    print("3. Region Concepcion")
                    op=int(input("Ingrese una opcion: "))
                    if op==1:
                        r="Santiago"
                    elif op==2:
                        r="Valparaiso"
                    elif op==3:
                        r="Concepcion"
                    print(f"Top 3 De Region {r}")
                    filtrados=[(k,v) for k,v in datos.items() if v["region"]==r]
                    top2=heapq.nlargest(3,filtrados,key= lambda x:x[1]["total"])
                    for i,(n,v) in enumerate(top2,start=1):
                        print(f"{i}- Comuna: {n} Ingresos Totales {v["total"]}")