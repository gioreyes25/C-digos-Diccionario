datos={}
buenas=["buena",]
while True:
    print("1. Agregar Estudiante")
    print("2. Ver Tabla")
    print("3. Ver Ganador")
    print("4. Ver Reporte")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de el estudiante: ")
            votos=int(input("Ingrese votos: "))
            comentarios=input("Ingrese un comentario: ")
            datos[nombre]={"votos":votos,"comentario":comentarios}
        case 2:
            for n,i in datos.items():
                print(f"Nombre: {n}\nVotos: {i["votos"]}\nComentarios: {i["comentario"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda nombre:datos[nombre]["votos"])
            print(f"El ganador es {mayor} Con {datos[mayor]["votos"]} Votos")
        case 4:
            for n,i in datos.items():
                cadena=str(datos)
                conteo=cadena.count("buena" or  "genial")
                print(f"El candidato {n} Tiene {conteo}")
                