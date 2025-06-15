datos={}
while True:
    print("1. Jugar")
    print("2. Salir")
    op=int(input("Ingrese una opcion: "))
    match op:
        case 1:
            print("Solo Vamos A Ver Palabras que comienzen con G")
            frase=input("Ingrese una palabra: ")
            if frase.lower().startswith("g"):
                print(f"Felicidades sumas un punto porque la letra g es la primera")
                con=frase.count("g")
                print(f"La letra g aparece {con} veces")
                for indice,letra in enumerate(frase):
                    if letra=="g":
                        print(f"Numero: {indice} {letra}")
            else:
                print("lA LETRA G NO APARECE EN LA FRASE")
            