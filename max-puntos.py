datos={}
while True:
    print("1. Registrar Jugador")
    print("2. Ver Jugadores")
    print("3. Ver Jugador Con Mas Puntos")
    print("4. Ver Jugador Con Menos Puntos")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese su nombre: ")
            puntos=int(input("Ingrese puntos: "))
            datos[nombre]={"puntos":puntos}
        case 2:
            print(f"Jugadores Totales: {len(datos)}")
            for n,i in datos.items():
                print(f"Nombre: {n}\nPuntos: {i["puntos"]}")
        case 3:
            mayor=max(datos,key=lambda nombre:datos[nombre]["puntos"])
            print(f"El jugador {mayor} Es El Que Tiene Mas Puntos: {datos[mayor]["puntos"]}")
            print()
        case 4:
            menor = min(datos, key=lambda nombre: datos[nombre]["puntos"])
            print(f"El jugador {menor} es el que tiene menos puntos: {datos[menor]['puntos']}")
            print()