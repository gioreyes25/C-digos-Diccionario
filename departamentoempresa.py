datos={
    "Finanzas":{"sueldo":0,"equipo":0,"mantencion":0,"total":0},
    "Marketing":{"sueldo":0,"equipo":0,"mantencion":0,"total":0},
    "Sofware":{"sueldo":0,"equipo":0,"mantencion":0,"total":0}
}
while True:
    print("1. Agregar Gastos")
    print("2. Ver Gastos")
    print("3. Ver Area que mas gasta")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            sueldo=int(input("Ingrese total de sueldos: "))
            equipo=int(input("Ingrese gastos de equipo: "))
            manten=int(input("Ingerese gastos de mantencion: "))
            print("-Finanzas")
            print("-Marketing")
            print("-Sofware")
            op=input("Ingrese una opcion: ").capitalize()
            for n,i in datos.items():
                if op==n:
                    datos[op]["sueldo"]=sueldo
                    datos[op]["equipo"]=equipo
                    datos[op]["mantencion"]=manten
                    total=sueldo+equipo+manten
                    datos[op]["total"]=total
                    print(f"Se han añadido gastos ha {op}")
        case 2:
            for n,i in datos.items():
                print(f"Area: {n}\nSueldos: {i["sueldo"]}\nEquipos: {i["equipo"]}\nMantencion: {i["mantencion"]}\nGasto total: {i["total"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda op:datos[op]["total"])
            gastos={total:g for total,g in datos[mayor].items() if total != "total"}
            gastonum=max(gastos,key=gastos.get)
            nombregasto=gastos[gastonum]
            total=datos[mayor]["total"]
            porcentaje=(nombregasto/datos[mayor]["total"])*100
            porcentaje=round(porcentaje,2)
            print(f"La area que mas gasta es {mayor} con un total de {datos[mayor]["total"]}\nEl Gasto que mas influye es {gastonum} con ${nombregasto}, cubre el {porcentaje}% de el total")