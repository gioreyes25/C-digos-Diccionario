datos={}
repeticiones=[]
while True:
    print("1. Encuestar ")
    print("2. Ver Total Encuestados")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese su nombre: ")
            print("1. Manzana")
            print("2. Naranja")
            print("3. Platano")
            op=int(input("Ingrese una opcion: "))
            if op==1:
                comida="Manzana"
            elif op==2:
                comida="Naranja"
            elif op==3:
                comida="Platano"
            datos[nombre]={"comida":comida}
            repeticiones.append(comida)
        case 2:
            print(f"Cantidad De Encuestados: {len(datos)}")
            for nombre,i in datos.items():
                print(f"Nombre: {nombre}\nComida Fav: {i["comida"]}")
            manza=repeticiones.count("Manzana")
            nar=repeticiones.count("Naranja")
            pla=repeticiones.count("Platano")
            print("---------------------------------")
            print(f"La manzana se repite {manza}")
            print(f"La Naranja se repite {nar}")
            print(f"El Platano se repite {pla}")
                