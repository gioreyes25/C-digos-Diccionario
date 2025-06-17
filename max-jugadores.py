datos={}
while True:
    print("1. Agregar Jugadores")
    print("2. Ver Tabla De Jugadores")
    print("3. Ver Jugador Con Mayor Rendimiento")
    print("4. Ver Jugador Con Peor Rendimiento")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre: ")
            puntos=int(input("Ingrese puntos: "))
            asistencia=int(input("Ingrese Asistencias: "))
            rebotes=int(input("Ingrese Rebotes: "))
            rendi=(puntos*2)+(asistencia*1.5)+(rebotes*1.2)
            datos[nombre]={"puntos":puntos,"asistencia":asistencia,"rebotes":rebotes,"rendi":rendi}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nPuntos: {i["puntos"]}\nAsistencia: {i["asistencia"]}\nRebotes: {i["rebotes"]}\nRendimiento: {i["rendi"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda nombre:datos[nombre]["rendi"])
            print(f"El Jugador {mayor} Es Quien Tiene El Mayor Rendimiento: {datos[mayor]["rendi"]}")
        case 4:
            menor=min(datos,key=lambda nombre:datos[nombre]["rendi"])
            print(f"El Jugador {menor} Es Quien Tiene El Peor Rendimiento: {datos[menor]["rendi"]}")