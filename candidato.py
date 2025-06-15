datos=[]
codigo=0
while True:
    print("1. Registrar Candidato")
    print("2. Votar Por Candidato")
    print("3. Mostrar Candidato")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            codigo+=1
            nombre=input("Ingrese nombre: ")
            edad=int(input("Ingrese edad"))
            votos=0
            info={
                "codigo":codigo,
                "nombre":nombre,
                "edad":edad,
                "votos":votos
            }
            datos.append(info)
        case 2:
            contar=0
            for i in datos:
                contar+=1
                print(f"Codigo: {i["codigo"]}\nNombre: {i["nombre"]}\nEdad: {i["edad"]}\nVotos: {i["votos"]}")
                print()
                if contar==codigo:
                    votar=int(input("Ingrese codigo de el candidato: "))
                    for i in datos:
                        if votar==i["codigo"]:
                            cantidad=int(input("Ingrese cantidad de votos: "))
                            i["votos"]+=cantidad
                            break
        case 3:
            ganador = max(datos, key=lambda x: x["votos"])
            print(f"El ganador es: {ganador["nombre"]} Con {ganador["votos"]}")
                
        
            