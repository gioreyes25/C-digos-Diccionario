filas=["A","B","C"]
asientos={}
columnas=range(1,4)
for filas in filas:
    for col in columnas:
        asiento=f"{filas}{col}"
        asientos[asiento]={"disponible":True,"Nombre":""}
datos={}
while True:
    print("1. Ver Asientos Disponibles")
    print("2. Reservar Asiento")
    print("3. Cancelar Reserva")
    print("4. Ver Todas las reservas")
    print("5. Buscar A quien pertenece reserva")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            for n,i in asientos.items():
                if i["disponible"]==True:
                    print(f"Asiento: {n}\nDisponibilidad: Si")
                    print()
                else:
                    print
        case 2:
            for n,i in asientos.items():
                if i["disponible"]==True:
                    print(f"Asiento: {n}\nDisponibilidad: Si")
                    print()
                else:
                    print
            reserva=input("Ingrese el Asiento que desea: ")
            for n,i in asientos.items():
                if reserva==n:
                    nombre=input("Ingrese su nombre: ")
                    print(f"Aqui tiene su asiento {n} sr/a {nombre}")
                    i["disponible"]=False
                    i["nombre"]=nombre
        case 3:
            for n,i in asientos.items():
                if i["disponible"]==False:
                    print(f"Asiento: {n}\nDisponibilidad: Reservado")
                    print()
                else:
                    print
            cancelar=input("Ingrese asiento que desa cancelar: ")
            for n,i in asientos.items():
                if cancelar==n:
                    print(f"Ha Cancelado Reservacion de asiento {n}")
                    i["disponible"]=True
        case 4:
            for n,i in  asientos.items():
                if i["disponible"]==False:
                    print(f"Asiento: {n}\nDisponibilidad: Reservado")
                    print()
        case 5:
            for n,i in asientos.items():
                if i["disponible"]==False:
                    print(f"Nombre: {i["nombre"]}\nAsiento: {n}\nDisponibilidad: Reservado")
                    print()