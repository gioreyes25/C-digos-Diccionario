datos=[]
info={}
clave=-1
total=0
while True:
    op=int(input("Ingrese una opcion:l "))
    match op:
        case 1:
            canti=int(input("Ingrese cantidad: "))
            for i in range(canti):
                nombre=input("Ingrese nombre")
                voto=0
                clave+=1
                porcen=0
                info={
                "clave":clave,
                "nombre":nombre,
                "votos":voto,
                "porcen":porcen
                }
                datos.append(info)
        case 2:
            for i in datos:
                print(f"Clave: {i["clave"]} Nombre: {i["nombre"]}\nVotos: {i["votos"]}")
            r=0
            ope=0
            for i in datos:
                r+=1
                (f"Clave: {i["clave"]} Nombre: {i["nombre"]}\nVotos: {i["votos"]}")
                if r==1:
                    codigo=int(input("Ingrese la clave: "))
                if codigo==i["clave"]:
                    votar=int(input("Ingrese la cantidad de votos: "))
                    print(i["votos"])
                    print()
                    print(total)
                    print()
                    i["votos"]+=votar
                    i["porcen"]=0
                    total+=votar
                    print(f"votos totales: {total}")
                    for i in datos:
                        i["porcen"]=(i["votos"]/total)*100
                        i["porcen"]=round(i["porcen"],1)
                    print(i["porcen"])
                    print()
                    print(datos)
                    break
        case 3:
            
            for i in datos:
                    (f"Nombre: {i["nombre"]}\nVotos: {i["votos"]}")
                    ganador = max(datos, key=lambda x: x["votos"])
                    porcen = max(datos,key=lambda x: x["porcen"])
            print(f"El ganador es {ganador["nombre"]} con {ganador["votos"]} votos {porcen["porcen"]}")