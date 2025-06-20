datos={
    "1A":{"promedio":0,"conteo":0},
    "2A":{"promedio":0,"conteo":0},
    "3A":{"promedio":0,"conteo":0},
}
while True:
    print(datos)
    print("1. Agregar Estduiante: ")
    print("2. Ver Promedios Generales De Curso")
    print("3. Ver Mejor Curso")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            nota1=float(input("Ingrese Nota De Matematicas: "))
            nota2=float(input("Ingrese Nota De Historia: "))
            nota3=float(input("Ingrese Nota De Ciencias: "))
            promedio=(nota1+nota2+nota3)/3
            promedio=round(promedio,1   )
            print("1A")
            print("2A")
            print("3A")
            curso=input("Ingrese curso al que desea agregar promedio: ")
            for n,i in datos.items():
                if curso==n:
                    datos[curso]["promedio"]+=promedio
                    i["conteo"]+=1
                    if i["conteo"]==1:
                        break
                    if i["conteo"]>2:
                        pro=i["promedio"]/2
                        pro=round(pro,1)
                        datos[curso]["promedio"]=pro
                    else:
                        promedio=i["promedio"]/2
                        promedio=round(promedio,1)
                        datos[curso]["promedio"]=promedio
        case 2:
            for n,i in datos.items():
                print(f"Curso: {n}\nPromedio General: {i["promedio"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda curso:datos[curso]["promedio"])
            print(f"El mejor curso es: {mayor} con un promedio de: {datos[mayor]["promedio"]}")