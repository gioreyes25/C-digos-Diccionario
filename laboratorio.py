datos={
    "Sur":{"total":0,"sangre":0,"orina":0,"adn":0},
    "Centro":{"total":0,"sangre":0,"orina":0,"adn":0},
    "Norte":{"total":0,"sangre":0,"orina":0,"adn":0}
}
while True:
    print("1. Tomar Muestras")
    print("2. Ver Laboratorios")
    print("3. Ver Mejor Labotarotio")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            sangre=int(input("Ingrese cantidad de muestras de sangre: "))
            orina=int(input("Ingrese cantidad de muestras de orina: "))
            adn=int(input("Ingrese cantidad de muestras de ADN: "))
            print("1. Sur")
            print("2. Centro")
            print("3. Norte")
            labo=input("Ingrese laboratorio al que se iran estas muestras")
            for n,i in datos.items():
                if labo==n:
                    datos[labo]["sangre"]+=sangre
                    datos[labo]["orina"]+=orina
                    datos[labo]["adn"]+=adn
                    total=sangre+orina+adn
                    datos[labo]["total"]+=total
        case 2:
            print(datos)
            for n,i in datos.items():
                total=i["total"]
                print(f"Laboratorio: {n}\nMuestras SANGRE: {i["sangre"]}\nMuestras ORINA: {i["orina"]}\nMuestras ADN: {i["adn"]}\nTotal: {i["total"]}")
                print()
        case 3:
            mayor=max(datos,key=lambda x:datos[x]["total"])
            muestras={total:m for total,m in datos[mayor].items() if total != "total"}
            mejormuestra=max(muestras,key=muestras.get)
            porcen=(muestras[mejormuestra]/datos[mayor]["total"])*100
            porcen=round(porcen,1)
            print(f"El mejor Laboratorio es: {mayor} Con Un total de {datos[mayor]["total"]} De Muestras\nLa muestra que mas aporta es: {mejormuestra} con {muestras[mejormuestra]} que es el {porcen}% del total")