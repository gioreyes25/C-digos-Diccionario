datos=[]
total=0
pelis=0
pelib=0
pelim=0
while True:
    print("1. Encuesta de pelicula")
    print("2. Ver encuesta")
    print("3. Salir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            total+=1
            nombre=input("Ingrese su nombre: ")
            edad=int(input("Ingrese su edad: "))
            print("1. Spiderman")
            print("2. Monsters INC")
            print("3. Barbie")
            op=int(input("Ingrese la pelicula de su preferencia:"))
            if op==1:
                peli="Spiderman"
                pelis+=1
            elif op==2:
                peli="Monsters INC"
                pelim+=1
            elif op==3:
                peli="Barbie"
                pelib+=1
            peli={
                "nombre":nombre,
                "edad":edad,
                "peli":peli
            }
            datos.append(peli)
        case 2:
            for i in datos:
                print(f"-Nombre: {i["nombre"]}\n-Edad: {i["edad"]}\n-Pelicula Favorita: {i["peli"]}")
            print(f"El total de los encuestados que fueron en total: {total}, Eligieron:\n-Pelicula Spiderman: {pelis}\n-Pelicula Monsters INC: {pelim}\n-Pelicula Barbie: {pelib}")