datos=[]
while True:
    numero=input("Ingrese numero: ")
    datos=list(map(float,numero.split(",")))
    reves=sorted(datos,reverse=True)
    print(reves)
    