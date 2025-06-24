datos={}
import heapq
while True:
    vo=sum(producto["votos"] for producto in datos.values())
    print("\n1. Agregar Candiadto")
    print("2. Ver Lista De Candidatos")
    print("3. Votar")
    print("4. Ver Ganador")
    op=int(input("Ingrese op: "))
    match op:
        case 1:
            nombre=input("Ingrese nombre de candidato: ").capitalize()
            edad=int(input("Ingrese edad: "))
            datos[nombre]={"edad":edad,"votos":0,"total":0}
        case 2:
            for n,i in datos.items():
                print(f"Candidato: {n}\nEdad: {i["edad"]}\nVotos: {i["votos"]}")
                print()
        case 3:
            for n,i in datos.items():
                print(f"Candidato: {n}\nEdad: {i["edad"]}\nVotos: {i["votos"]}")
                print()
            votar=input("Ingrese nombre de candidato: ").capitalize()
            for n,i in datos.items():
                if votar==n:
                    votos=int(input("Ingrese cantidad de votos: "))
                    i["votos"]+=votos
        case 4:
            filtrados = [(k, v) for k, v in datos.items() if v["area"] == i["area"]]
            top=heapq.nlargest(3,datos.items(),key= lambda x:x[1]["votos"])
            print("CANDIDATO GANADOR")
            for i,(n,v) in enumerate(top,start=1):
                porcen=(v["votos"]/vo)*100
                porcen=round(porcen,2)
                print(f"{i}- Candidato {n} Votos: {v["votos"]} {porcen}")
                print()