datos={}
comidas=[]
while True:
    print("1. Agregar Personas")
    print("2. Ver Cuantas 6 letras")
    print("3. Ver Nombres De Comidas de mas de 8 letras")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese un nombre: ")
            comida=input("Ingrese su comida favorita: ")
            datos[nombre]={"comida":comida}
            comidas.append(comida)
        case 2:
            son6=len(comidas)==6
            print(f"Comidas con 6 letras: {son6}")
        case 3:
            for nombre,i in datos.items():
                if len(i["comida"])>8:
                    print(f"Nombre: {nombre}\nComida: {i["comida"]}")
                