datos={}
while True:
    print("\n1. Agregar Jugador")
    print("2. Ver Jugadores")
    print("3. Jugar")
    print("4. Ver Top")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            jugador=input("Ingrese nombre de jugador: ").title()
            datos[jugador]={"asistencia":0,"gol":0}
        case 2:
            for n,i in datos.items():
                print(f"Jugador: {n}\nAsistencias: {i["asistencia"]}\nGoles: {i["gol"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Jugador: {n}\nAsistencias: {i["asistencia"]}\nGoles: {i["gol"]}")
                print()
            elegir=input("Ingrese jugador: ").title()
            if elegir in datos:
                goles=int(input("Ingrese goles "))
                asi=int(input("Ingrese asistencias: "))
                for n,i in datos.items():
                    if elegir==n:
                        i["gol"]+=goles
                        i["asistencia"]+=asi
                print(f"El jugador {elegir} anoto {goles} goles y dio {asi} Asistencias")
        case 4:
            import heapq
            print("1. Ver Top 3 Con Mas Goles")
            print("2. Ver Top 3 Con Mas Asistencias")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["gol"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} Cantidad de Goles: {v["gol"]}")
                case 2:
                    top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["asistencia"])
                    for i,(n,v) in enumerate(top,start=1):
                        print(f"{i}- {n} Cantidad de Asistencias: {v["asistencia"]}")