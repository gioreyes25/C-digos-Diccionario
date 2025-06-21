datos=[]
total=0
while True:
    print("1. Agregar Candidato")
    print("2. Votar Por Candidato")
    print("3. Ver Candidatos")
    print("4. Ver Candidato Ganador")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de candidato: ").capitalize()
            votos=0
            info={"nombre":nombre,"votos":votos,"total":0}
            datos.append(info)
        case 2:
            for i in datos:
                print(f"Candidato: {i["nombre"]}\nVotos: {i["votos"]}")
                print()
            votar=input("Ingrese nombre de el candidato: ").capitalize()
            for i in datos:
                if votar==i["nombre"]:
                    cantidad=int(input("Ingrese cantidad de votos: "))
                    i["votos"]+=cantidad
                    total+=cantidad
        case 3:
            for i in datos:
                print(f"Candidato: {i["nombre"]}\nVotos: {i["votos"]}")
                print()
        case 4:
            mayor=max(datos,key=lambda x:x["votos"])
            porcen=(mayor["votos"])/total*100
            porcen=round(porcen,2)
            for i in datos:
                porcentaje=i["votos"]/total*100
                porcentaje=round(porcentaje,2)
                print(f"Candidato: {i["nombre"]}\nVotos: {i["votos"]}\nPorcentaje: {porcentaje}%")
                print()
            print(f"El candidato ganador es {mayor["nombre"]} con {mayor["votos"]} votos con el {porcen}% de los votoss")