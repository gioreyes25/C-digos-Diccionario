datos=[]
while True:
    print("1. Registrar Temperatura")
    print("2. Ver Temperatura Mas Alta")
    print("3. Ver Temperatura Mas Baja")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            temperatura=int(input("Ingrese temperatura: "))
            datos.append(temperatura)
        case 2:
            mayor=max(datos)
            print("La Temperatura Mas Alta es: ",mayor)
        case 3:
            menor=min(datos)
            print("La Temperatura Mas Baja es: ",menor)