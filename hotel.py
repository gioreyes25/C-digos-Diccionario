datos=[]
hotel={}
while True:
    print("1. Reservar Habitacion: ")
    print("2. Clientes Registrados")
    print("3. Salir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de el cliente: ")
            dias=int(input("Ingrese Dias de estadia: "))
            print()
            print("1. Simple $50 X Dia")
            print("2. Doble $90 X Dia")
            print("3. Suites $150 X Dia")
            habitacion=int(input("Ingrese habitacion: "))
            if habitacion==1:
                habitacion="Simple"
                costohabi=50*dias
            elif habitacion==2:
                habitacion="Doble"
                costohabi=90*dias
            elif habitacion==3:
                habitacion="Suite"
                costohabi=150*dias
            hotel={
                "nombre":nombre,
                "dias":dias,
                "habitacion":habitacion,
                "costo":costohabi
            }
            datos.append(hotel)
        case 2:
            for i in datos:
                print(f"Nombre: {i["nombre"]}\n-Estadia: {i["dias"]} Dias\n-Habitacion: {i["habitacion"]}\n-Costo Total: {i["costo"]}")
                print()
        case 3:
            print("Hasta Pronto")
            break