datos={}
while True:
    print("1. Agregar Empleado")
    print("2. Ver Analiticas")
    print("3. Ver Mejor Empleado")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre")
            edad=input("Ingrese edad: ")
            puntu=int(input("Ingrese Puntualidad 1-10"))
            Produ=int(input("Ingrese Productividad 1-10"))
            equipo=int(input("Ingrese Trabajo En Equipo 1-10"))
            porcen=(puntu+Produ+equipo)/30*100
            porcen=round(porcen,1)
            datos[nombre]={"edad":edad,"puntu":puntu,"produ":Produ,"equipo":equipo,"porcen":porcen}
        case 2:
            print(f"Total Empleados: {len(datos)}")
            for n, i in datos.items():
                print(f"Nombre: {n} Edad: {i["edad"]}\nPuntualidad: {i["puntu"]}\nProductividad: {i["produ"]}\nTrabajo En Equipo: {i["equipo"]}\nPorcentaje: {i["porcen"]}%")
                print()
        case 3:
            mayor=max(datos,key=lambda x:datos[x]["porcen"])
            print(f"El Empleado Con Mejor Porcentaje Es: {mayor}\n{datos[mayor]["porcen"]}")