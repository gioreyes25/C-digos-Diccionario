datos={}
while True:
    print("1. Agregar Carreras Universitarias")
    print("2. Ver Tabla De Carreras")
    print("3. Ver Carrera Con Mejor Indice")
    print("4. Ver Carrera Con El Peor Indice")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de la carrera: ")
            egreso=int(input("Ingrese egreso de la carrera: "))
            emple=int(input("Ingrese empleabilidad de la carrera: "))
            sueldo=int(input("Ingrese sueldo de la carrera: "))
            indice=(egreso*0.3)+(emple*0.4)+((sueldo/20)*0.3)
            datos[nombre]={"egreso":egreso,"emple":emple,"sueldo":sueldo,"indice":indice}
        case 2:
            for n,i in datos.items():
                print(f"Carrera: {n}\nEgreso: {i["egreso"]}\nEmpleabilidad: {i["emple"]}\nSueldo: {i["sueldo"]}\nIndice: {i["indice"]}")
                print()
        case 3:
            mayor=max(datos,key= lambda nombre:datos[nombre]["indice"])
            print(f"La Carrera {mayor} Es La Mas Alta Con Un Indice De {datos[mayor]["indice"]}")
        case 4:
            menor=min(datos,key= lambda nombre:datos[nombre]["indice"])
            print(f"La Carrera {menor} Es La Mas Baja Con Un Indice De {datos[menor]["indice"]}")