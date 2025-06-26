datos={}
while True:
    print("1. Agregar Ingresos")
    print("2. Agregar Ingresos")
    print("3. Ver Top 3")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            comuna=input("Ingrese comuna: ").title()
            print("1. Santiago")
            print("2. Concepcion")
            print("3. Valparaiso")
            op=int(input("Ingrese region: "))
            if op==1:
                region="Santiago"
            elif op==2:
                region="Concepcion"
            elif op==3:
                region="Valparaiso"
            
            datos[comuna]={"region":region,"total":0,"educacion":0,"comercio":0,"cultura":0}
        case 2:
            for n,i in datos.items():
                print(f"Region: {i["region"]}\nComuna: {n}\nTotal Ingresos: {i["total"]}")
                print()
            elegir=input("Ingrese comuna: ").title()
            for n,i in datos.items():
                if elegir==n:
                    print("1. Educacion")
                    print("2. Cultura")
                    print("3. Comercio")
                    op=int(input("Ingrese una opcion: "))
                    if op==1:
                        area="Educacion"
                        ingresos=int(input("Ingrese ingresos: "))
                        i["educacion"]+=ingresos
                        i["total"]+=ingresos
                    elif op==2:
                        area="Cultura"
                        ingresos=int(input("Ingrese ingresos: "))
                        i["cultura"]+=ingresos
                        i["total"]+=ingresos
                    elif op==3:
                        area="Comercio"
                        ingresos=int(input("Ingrese ingresos: "))
                        i["comercio"]+=ingresos
                        i["total"]+=ingresos
        case 3:
            import heapq
            print("1. Santiago")
            print("2. Concepcion")
            print("3. Valparaiso")
            op=input("Ingrese region que desea ver: ").title()
            fil=[(k,v) for k,v in datos.items() if v["region"]==op]
            top=heapq.nlargest(3,fil,key=lambda x:x[1]["total"])
            for i,(n,v) in enumerate(top,start=1):
                print(f"{i}- {n} \nEducacion: ${v["educacion"]}\nCultura: ${v["cultura"]}\nComercio: ${v["comercio"]}\nTotal Ingresos{v["total"]}")
                print()
            