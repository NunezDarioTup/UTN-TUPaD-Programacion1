a = {"usuario": "alumno",
     "contraseña": "python123"}

intentos = 0
while intentos < 3:
    sudo=input("Ingrese su usuario: ").strip()
    psw=input("Ingrese su contraseña: ").strip()

    if sudo == a["usuario"] and psw == a["contraseña"]:
        print("Acceso concedido")
        eleccion = ""
        while eleccion != "4":
            print("Ingrese una opcion \n")
            print(" 1-Ver estado de Inscripcion\n 2-Cambiar Clave\n 3-Mostrar mensaje motivacional\n 4-Salir\n")
            eleccion = input("Usted elige: ").strip()
            if eleccion.isdigit() or aleccion != "":
                if eleccion == "1":
                    print(f"{sudo} esta inscripto")
                elif eleccion == "2":
                    psw1 , psw2 =""," "
                    while psw1 != psw2:
                        print("Ingrese la contraseña\n")
                        psw1=input()
                        if len(psw1) >= 6:
                            print("Ingrese la contraseña nuevamente\n")
                            psw2=input()
                        else:
                            print("La contraseña debe tener 6 caracteres minimo")
                    print(f"{sudo} ha cambiado la contraseña")
                elif eleccion =="3":
                    print("Todo lo puedo en Cristo que me fortalece, Filipenses 4:13\n")
                elif eleccion =="4":
                    break
                else:
                    print("Ingrese 1, 2 , 3 o 4")
        break
    else:
        print("Usuario y/o contraseña incorrectos")
        intentos += 1

if intentos == 3:
    print("Ingreso bloqueado")
print("Gracias por visitarnos")

