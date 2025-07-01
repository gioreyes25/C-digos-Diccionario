datos={}
contraseña=0
if contraseña not in datos:
    contraseña=input("Cree una contraseña: ").title()
    datos[contraseña]={}
while True:
    pas=input("Ingrese nuevamente contraseña: ").title()
    if pas in datos:
        print(f"Acceso concedido")
    else:
        print(f"Contraseña Incorrecta o no existe")