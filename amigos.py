ventas = {
    "Sur": [
        {"producto": "Laptop", "cantidad": 4, "ingreso": 4000},
        {"producto": "Mouse", "cantidad": 10, "ingreso": 250},
        {"producto": "Teclado", "cantidad": 5, "ingreso": 500}
    ],
    "Centro": [
        {"producto": "Laptop", "cantidad": 2, "ingreso": 2000},
        {"producto": "Mouse", "cantidad": 44, "ingreso": 5700}
    ],
    "Norte": [
        {"producto": "Laptop", "cantidad": 3, "ingreso": 3000},
        {"producto": "Teclado", "cantidad": 7, "ingreso": 7000}
    ]
}
ingresos={
    "Sur":{"total":0},
    "Centro":{"total":0},
    "Norte":{"total":0},
}
totales={}
while True:
    print("1. Ver Lista")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in ventas.items():
                print(f"Sucursal {n}")
                total=0
                for v in i:
                    total+=v["ingreso"]
                    print(total)
                    print(f"Producto {v["producto"]}\nCantidad: {v["cantidad"]}\nTotal: ${v["ingreso"]}")
                    print()
                    print(f"Ingreso Totales de Sucursal {n} {total}")
                    if v["producto"] not in totales:
                        totales[v["producto"]]={"cantidad":v["cantidad"],"total":total}
                    else:
                        for a,i in totales.items():
                            if v["producto"]==a:
                                i["cantidad"]+=v["cantidad"]
                                i["total"]+=total
                print("------------------------------------")
                ingresos[n]["total"]+=total
            mayor=max(ingresos,key=lambda x:ingresos[x]["total"])
            print(f"La sucursal con mas ingresos es {mayor}")
            print()
            for n,i in totales.items():
                print(f"{n} Ganancias Totales: {i["total"]}")
                print()
            mas=max(totales,key=lambda x:totales[x]["total"])
            print(f"El producto que mas genero genero ventas fue {mas} {totales[mas]["total"]}")
