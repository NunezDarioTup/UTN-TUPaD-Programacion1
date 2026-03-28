# Juego de alarma, se evita usar tildes para evitar error de UNICODE

energia=100
tiempo=12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
agente= ""
anti_spam=0                           #usado para que no forzar cerradura 3 veces seguidas
bloqueo = False                     

while True:
    print("Ingrese su nombre agentico\n")
    agente=input().title()
    if agente.isalpha() and agente !="":
        print(f"Bienvenido agente {agente}, abra las cerraduras antes que acabe el tiempo")     
        break
    else:
        print("Ingrese un nombre de agente valido")
        
opcion=""

while energia > 0 and tiempo >0 and cerraduras_abiertas < 3 and not bloqueo:
    while True:      #while para validar que solo se ingrese los numeros 123 y nada mas
        print("Elijas las opciones que desea hacer:\n1-Forzar Cerradura\n2-Hackear Panel\n3-Descansar\n")
        opcion=input()
        if opcion.isdigit():
            opcion=int(opcion)
            if opcion in (1,2,3):
                break
        print("Entrada inválida, solo ingrese los valores 1, 2 o 3")

    match opcion :
        case 1 :                      #Forzar cerradura
            energia -= 20
            tiempo -= 2
            anti_spam +=1
        
            if energia < 40:
                print("Riesgo de alarma")
                num =""
                while not num.isdigit() or int(num) not in (1, 2, 3):           #si ingresa 3 bloquea, el resto continua el juego
                    print("Para desactivarla ingrese\n1\n2\n3")
                    num=int(input())
                if num ==3:
                    alarma = True
                    print("Alarma encendida")
                    break
                else:
                    cerraduras_abiertas +=1
                    print(f"Se ha abierto una cerradura, ha abierto {cerraduras_abiertas}")
            elif anti_spam < 3 :
                cerraduras_abiertas +=1
                print(f"Se ha abierto una cerradura, ha abierto {cerraduras_abiertas}")
            elif anti_spam == 3:                                                       #Al llegar al antispam directamente se pierde por bloqueo
                break
            
        case 2 :                   #Hackear
            energia -=10
            tiempo -= 3
            anti_spam = 0
            for x in range(4):
                print("Codigo", x+1)
                codigo_parcial +=  "X"
                print(x)
            if len(codigo_parcial) >=8 and cerraduras_abiertas < 3:
                cerraduras_abiertas +=1
                print(f"Se ha abierto una cerradura, con el codigo {codigo_parcial}, ha abierto {cerraduras_abiertas}")
        
        case 3 :                  #Descansar
            energia = min( energia +15, 100) #nunca supera los 100, ya que si pasa devuelve le valor mas chico
            tiempo -=1
            if alarma ==True:
                energia -= 10
        
        case _:
            print("Opcion invalida, intente nuevamente")
            
    if alarma == True:
        energia -= 10

        
if alarma == True and tiempo <= 3:
    bloqueo = True
    print(f"Agente {agente} ha sido derrotado, sistema bloqueado")
elif anti_spam == 3:
    alarma = True
    bloqueo = True
    print("Usted ha perdido. Sistema anti-spam activado")
elif energia <= 0:
    print(f"Agente {agente} usted ha perdido por falta de energía")
elif tiempo <= 0:
    print(f"Agente {agente} usted ha perdido por falta de tiempo")
elif cerraduras_abiertas >= 3:
    print(f"Agente {agente} usted ha logrado abrir las cerraduras")


print("Gracias por participar by ND!!!")
