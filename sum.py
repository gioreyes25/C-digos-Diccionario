datos={
    "Panaderia":[],
    "Carniceria":[],
    "Fruteria":[]
    }
while True:
    print("1. Agrgear ingresos")
    print("2. Verlos")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            plata=int(input("Ingrese plata"))
            print("1. Panaderia")
            print("2. Carniceria")
            print("3. Fruteria")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                area="Panaderia"
            elif op==2:
                area="Carniceria"
            elif op==3:
                area="Fruteria"
            datos[area].append(plata)
        case 2:
            for n,i in datos.items():
                    print(f"{n} {sum(datos[n])}")                