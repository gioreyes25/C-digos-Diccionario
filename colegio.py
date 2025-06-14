
conta=0
promedio=0
datos=[]
notas={}
while True:
    print("1. Agregar Estudiante")
    print("2. Mostrar Estudiantes")
    print("3. Salir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            cantidad=int(input("Ingrese la cantidad de estudiantes wu va a registrar"))
            for i in range(cantidad):
                conta+=1
                print(f"Estudiante Numero: {conta}")
                nombre=input("Ingrese nombre de el estudiante")
                edad=int(input("Ingrese la edad de el estudiante"))
                notamate=int(input("Ingrese nota de Matematicas: "))
                notahistoria=int(input("Ingrese nota de Historia: "))
                notalenguaje=int(input("Ingrese nota de Lenguaje: "))
                notas={
                    "nombre":nombre,
                    "edad":edad,
                    "notamate":notamate,
                    "notahistoria":notahistoria,
                    "notalenguaje":notalenguaje
                }
                datos.append(notas)
        case 2:
            for i in datos:
                mate=i["notamate"]
                lengua=i["notalenguaje"]
                historia=i["notahistoria"]
                print()
                print(f"Nombre: {i["nombre"]} Edad: {i["edad"]} \n-Nota Mate:{i["notamate"]}\n-Nota Historia:{i["notahistoria"]}\n-Nota Lenguaje:{i["notalenguaje"]}")
                total=(mate+lengua+historia)/3
                total=round(total,1)
                print(f"Promedio de {i["nombre"]}:{total}")
                print()
            if total>promedio:
                print(f"El Estudiante {i["nombre"]} Tiene el promedio mas alto: {total}")