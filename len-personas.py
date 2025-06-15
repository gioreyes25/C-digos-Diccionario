datos={}
while True:
    print("1. Agregar Personas")
    print("2. Verlas")
    print("3. Ver Comidas Que Empiezen Con P")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese un nombre: ")
            comida=input("Ingrese una comida")
            datos[nombre]={"comida":comida}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nComida: {i["comida"]}")
                print()
        case 3:
            for n, i in datos.items():
                if i["comida"].lower().startswith("p"):
                    print(f"Nombre: {n}\nComida: {i['comida']}")

                