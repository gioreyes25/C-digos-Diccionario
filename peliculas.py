from heapq import nlargest
datos={}
promedios=[]
while True:
    print("1. Agregar Pelicula")
    print("2. Ver Lista De Peliculas")
    print("3. Buscar Pelicula Por Nombre")
    print("4. Agregar Calificacion a la pelicula")
    print("5. Mostrar Top 3 peliculas mejor calificadas")
    print("6. Listar Peliculas Por Genero")
    op=int(input("Ingrese una opciom: "))
    match op:
        case 1:
            pelicula=input("Ingrese nombre de la pelicula: ").capitalize()
            año=int(input("Ingrese año de la pelicula: "))
            print("1. Ciencia Ficcion")
            print("2. Romantica")
            print("3. Animacion")
            op=int(input("Ingrese genero de la pelicula: "))
            if op==1:
                genero="Ciencia Ficcion"
            elif op==2:
                genero="Romantica"
            elif op==3:
                genero="Animacion"
            datos[pelicula]={"año":año,"genero":genero,"conteo":0,"cali":0}
        case 2:
            for n,i in datos.items():
                print(f"Pelicula: {n}\nAño: {i["año"]}\nGenero: {i["genero"]}\nCalificacion: {i["cali"]}")
                print()
        case 3:
            nombre=input("Ingrese nombre de pelicula que desea buscar: ").capitalize()
            for n,i in datos.items():
                if nombre==n:
                    print(f"Pelicula: {n}\nAño: {i["año"]}\nGenero: {i["genero"]}\nCalificacion: {i["cali"]}")
                    print()
        case 4:
            for n,i in datos.items():
                print(f"Pelicula: {n}\nAño: {i["año"]}\nGenero: {i["genero"]}\nCalificacion: {i["cali"]}")
                print()
            name=input("Ingrese pelicula que va a calificar: ").capitalize()
            for n,i in datos.items():
                if name==n:
                    cali=int(input("Ingrese calificacion de 1 a 10"))
                    if cali >10 or cali<1:
                        print("Ingrese Bien")
                    i["conteo"]+=1
                    i["cali"]+=cali
                    if i["conteo"]>=2:
                        califi=i["cali"]/2
                        i["cali"]=califi
        case 5:
            print()
        case 6:
            print("1. Ciencia Ficcion")
            print("2. Romantica")
            print("3. Animacion")
            op=int(input("Ingrese genero de la pelicula: "))
            if op==1:
                genero="Ciencia Ficcion"
            elif op==2:
                genero="Romantica"
            elif op==3:
                genero="Animacion"
            for n,i in datos.items():
                if genero==i["genero"]:
                    print(f"Pelicula: {n}\nAño: {i["año"]}\nGenero: {i["genero"]}\nCalificacion: {i["cali"]}")
                    print()