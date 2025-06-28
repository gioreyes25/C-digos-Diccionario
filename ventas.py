ventas = [
    {"fecha": "2025-06-01", "producto": "Laptop", "cantidad": 2, "ingreso": 2000},
    {"fecha": "2025-06-01", "producto": "Mouse", "cantidad": 5, "ingreso": 125},
    {"fecha": "2025-06-02", "producto": "Laptop", "cantidad": 1, "ingreso": 1000},
    {"fecha": "2025-06-02", "producto": "Teclado", "cantidad": 3, "ingreso": 300},
    {"fecha": "2025-06-03", "producto": "Laptop", "cantidad": 1, "ingreso": 1000},
    {"fecha": "2025-06-03", "producto": "Mouse", "cantidad": 2, "ingreso": 50},
    {"fecha": "2025-06-03", "producto": "Teclado", "cantidad": 1, "ingreso": 100}
]
datos=[]
totala=[]
while True:
    print(datos)
    print(totala)
    print("1. Ver")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for i in ventas:
                if i["fecha"]=="2025-06-01":
                    total=0
                    total+=i["ingreso"]
                    if i["fecha"] not in datos:
                        datos[i["fecha"]]={"producto":i["producto"],"total":total,"fecha":i["fecha"]}
                    else:
                        for n,i in datos.items():
                            if n=="2025-06-01":
                                i["total"]+=total
                elif i["fecha"]=="2025-06-02":
                    total=0
                    total+=i["ingreso"]
                    if i["fecha"] not in datos:
                        dat={"fecha":i["fecha"],"producto":i["producto"],"total":total,"fecha":i["fecha"]}
                        datos.append(dat)
                    else:
                        for n,i in datos.items():
                            if n=="2025-06-02":
                                i["total"]+=total
                elif i["fecha"]=="2025-06-03":
                    total=0
                    total+=i["ingreso"]
                    if i["fecha"] not in datos:
                        datos[i["fecha"]]={"producto":i["producto"],"total":total,"fecha":i["fecha"]}
                    else:
                        for n,i in datos.items():
                            if n=="2025-06-03":
                                i["total"]+=total
            for n,i in datos.items():
                if i["producto"] not in totala:
                    info={"producto":i["producto"],"total":i["total"]}
                    totala.append(info)
                else:
                    for i in totala:
                        if i["producto"]==n:
                            i["total"]+=total
            mayor=max(datos,key=lambda x:datos[x]["total"])
            print(f"La fecha con mas ingresos es {datos[mayor]["fecha"]} ${datos[mayor]["total"]}")
                    