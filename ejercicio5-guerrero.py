#La Arena del gladiador
vida_gladiador= 100 
vida_enemigo= 100 
pociones= 3 
dano_base_AP= 15
dano_critico = dano_base_AP * 1.5      #se cambia la variable aca, por limpieza del codigo
dano_base_enemigo= 12 
turno_gladiador = True 
nombre_gladiador=""

print("*******BIENVENIDO A LA ARENA DE COMBATE*******")
while True:
    print("Ingrese el nombre del gladiador")
    nombre_gladiador = input().title()
    if nombre_gladiador.isalpha() and nombre_gladiador != "":     #isalpha solo permite ingreso de letras para nombre
        print(f"A la arena ha ingresado {nombre_gladiador} el carnicero de Blaviken")
        break
    else:
        print("Error: solo se permiten letras")
nombre_enemigo= f"Dark {nombre_gladiador} "       #concateno cadenas, para el nombre, haciendo un antagonista
print(f"Se va a enfrentar a {nombre_enemigo}")
print("*******INICIO DE COMBATE*******")
while vida_gladiador > 0 and vida_enemigo > 0:                                                    #si cualquiera de las dos es 0 cierra el circulo
    print(f"{nombre_gladiador} (HP: {vida_gladiador}) | Pociones: {pociones}")
    print(f"{nombre_enemigo} (HP:{vida_enemigo}) | Pociones : 0")
    while turno_gladiador == True:
        turno = 1                                                        #Se coloca la variable  turno para saber que ronda va
        print(f"*******TURNO N* {turno}*******")
        opcion = input("Elije accion:\n 1-Ataque Pesado\n 2-Rafaga Veloz\n 3-Curar\n")
        if opcion.isdigit():                     #valida que la opcion ingresada sea un numero
            opcion = int(opcion)
            if opcion in (1,2,3):     #dentro de los numeros solo puede ser 1,2,3
                break
        print("Entrada inválida, solo ingrese los valores 1, 2 o 3")
            
    match opcion:                               #uso de match
        case 1:
            if vida_enemigo < 20:
                vida_enemigo = max(vida_enemigo - dano_critico, 0)
                print(f"¡Daño Critico atacaste al enemigo por {dano_critico: .2f} puntos de daño!")            
                
            elif vida_enemigo >= 20 :
                vida_enemigo = max(vida_enemigo - dano_base_AP, 0)
                print(f"¡Ataque pesado atacaste al enemigo por {dano_base_AP} puntos de daño!") 
            print(f"Vida enemigo {vida_enemigo} HP")
            turno_gladiador = False
            turno +=1                                                #se suma +1 a la ronda
        case 2:
            for x in range (3):
               vida_enemigo = max(vida_enemigo - 5, 0)    #funcion max, devuelve el valor mayor entre vida_enemigo y 0
               print(f"Ataque Rapido {x+1} ha surtido efecto")
               print(f"Golpe conectado por 5 de daño")
               if vida_enemigo ==0:                                    # evalua si la vida = 0 finaliza el ataque rapido
                   print("No es necesario continuar ya lo hemos derrotado")
                   break                   
               
            print(f"Vida enemigo {vida_enemigo} HP")
            turno_gladiador = False
            turno +=1
        case 3:
            if 0< pociones <=3:
                vida_gladiador = min(vida_gladiador + 30, 100)         #funcion min() hace que la vida no se pueda curar mas que el 100
                pociones -=1
                print(f"Te has curado +30 puntos, tu vida actual es {vida_gladiador}")
            elif pociones == 0:
                print("No quedan pociones!!!")
            turno_gladiador = False
            turno +=1
    if turno_gladiador == False and vida_enemigo > 0:      #turno es para cambiar quien va, si es true elejimos, si es false va el enemigo
        print(f"{nombre_enemigo} ha atacado!!!")
        vida_gladiador = max(vida_gladiador - dano_base_enemigo, 0)
        print(f"¡{nombre_enemigo} te atacó por 12 puntos de daño!")
        turno_gladiador = True

if vida_enemigo > 0:
    print("Derrota has caido en batalla")
elif vida_gladiador > 0:
    print(f"VICTORIA!!! {nombre_gladiador} has ganado la batalla")
           
