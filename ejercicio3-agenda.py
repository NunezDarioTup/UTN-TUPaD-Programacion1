# se omiten las tildes a los fines de no generar errorres con UNICODE
operador=""      #nombre operador
lunes0900 = ""      #ya que no se pueden usar listas, diccionarios, sets, ni tuplas, se usa variables por cada turno
lunes0930 = ""
lunes1000 = ""
lunes1030 = ""

martes0900 = ""
martes0930 = ""
martes1000 = ""

while True:
    print("Ingrese el nombre del operador: ")   
    operador=input().title()
    if operador.isalpha() and operador != "":       #para que operador sea solo letras y no sea vacio, tambien se podria haber usado variables, usuario1, usuario2 y asi
        break
    else:
        print("Operador invalido")
        
print(f"Hola operador {operador}, que desea hacer")

opcion=""
while opcion != 5:                      #while menu gral, sale con 5, se usa match case
    print("\nIngrese una opcion\n")       #\n antes y despues del print es solo a los fines esteticos
    print(f"1-Reservar turno:\n2-Cancelar turno (por nombre)\n3-Ver agenda del día\n4-Ver resumen general\n5-Cerrar sistema\n")
    opcion= input().lower()   # es a los fines que el usuario ingrese el numero de opcion o el str
    match opcion:
        case "1" | "reservar turno":
            print(f"¿Que dia necesita reservar el turno?\n1-Lunes\n2-Martes\n")
            dia = input().strip().lower()
            match dia:
                case "1" | "lunes":       #es el match dentro de reserva, se puede elegir lunes o martes
                    paciente=input(f"Ingrese el nombre del paciente\n")
                    if not paciente.isalpha():                    #compara que el paciente sea letras
                        print("El nombre debe contener solo letras.\n")
                    elif paciente in (lunes0900, lunes0930, lunes1000, lunes1030):  #compara que el paciente exista dentro de las variables, sino existe los guarda
                        print("Ese paciente ya tiene turno el dia lunes")
                    else:
                        if lunes0900 == "":
                            lunes0900 = paciente
                            print("Turno reservado el lunes 09:00")
                        elif lunes0930 =="":
                            lunes0930 = paciente
                            print("Turno reservado el lunes 09:30")
                        elif lunes1000 =="":
                            lunes1000 = paciente
                            print("Turno reservado el lunes 10:00")
                        elif lunes1030 =="":
                            lunes1030= paciente
                            print("Turno reservado el lunes 10:30")
                        else:
                            print("No queda turnos libres el lunes")
                            
                case "2" | "martes":
                    paciente=input(f"Ingrese el nombre del paciente\n")
                    if not paciente.isalpha():
                        print("El nombre debe contener solo letras.\n")
                    elif paciente in (martes0900, martes0930, martes1000):  #compara que este el nombre dentro de las variables, sino las guarda
                        print("Ese paciente ya tiene turno el dia martes")
                    else:
                        if martes0900 == "":
                            martes0900 = paciente
                            print("Turno reservado el martes 09:00")
                        elif martes0930 =="":
                            martes0930 = paciente
                            print("Turno reservado el martes 09:30")
                        elif martes1000 =="":
                            martes1000 = paciente
                            print("Turno reservado el martes 10:00")
                        else:
                            print("No queda turnos libres el martes")
                case _:
                    print("Dia Invalido, ingrese lunes o martes")
                    continue
            
        case "2" | "cancelar":   #primero corrobora que haya turnos para cancelar, si todas son vacias vuelve al menu

            if lunes0900 =="" and lunes0930=="" and lunes1000 =="" and lunes1030 == "" and martes0900 =="" and martes0930 ==""  and martes1000 == "":
                print("No hay turnos reservados para cancelar")
                continue
            print("Que dia desea cancelar el turno\n")
            print("1-Lunes\n2-Martes\n")
            dia = input().strip().lower()
            paciente=input(f"Ingrese el nombre del paciente que desea cancelar\n")
            if not paciente.isalpha():
                print("El nombre debe contener solo letras.\n")
            elif paciente in (lunes0900, lunes0930, lunes1000, lunes1030):
                if lunes0900 == paciente:
                      lunes0900 = ""
                      print("Turno dia lunes 09:00 cancelado")
                elif lunes0930 == paciente:
                    lunes0930 == ""
                    print("Turno dia lunes 09:30 cancelado")
                elif lunes1000 == paciente:
                    lunes1000 = ""
                    print("Turno dia lunes 10:00 cancelado")
                elif lunes1030 == paciente:
                    lunes1030= ""
                    print("Turno dia lunes 10:30 cancelado")
            elif paciente in (martes0900, martes0930, martes1000):
                print("Turno dia martes cancelado")
                if  martes0900 == paciente:
                    martes0900 = ""
                    print("Turno dia martes 09:00 cancelado")
                elif martes0930 == paciente:
                    martes0930 = ""
                    print("Turno dia martes 09:30 cancelado")
                elif martes1000 == paciente:
                    martes1000 = ""
                    print("Turno dia martes 10:00 cancelado")
            else:
                pass
                  
        case "3" | "ver agenda del dia":      #imprime por pantalla las condicionales en una sola linea
            print("Agenda Lunes:")
            print("Turno 09:00:", lunes0900 if lunes0900 != "" else "(libre)")
            print("Turno 09:30:", lunes0930 if lunes0930 != "" else "(libre)")
            print("Turno 10:00:", lunes1000 if lunes1000 != "" else "(libre)")
            print("Turno 10:30:", lunes1030 if lunes1030 != "" else "(libre)")

            print("Agenda Martes:")
            print("Turno 09:00:", martes0900 if martes0900 != "" else "(libre)")
            print("Turno 09:30:", martes0930 if martes0930 != "" else "(libre)")
            print("Turno 10:00:", martes1000 if martes1000 != "" else "(libre)")


        case "4" | "ver resumen general":   #suma +1 cada variable NO vacia
            ocupados_lunes = 0
            if lunes0900 != "": ocupados_lunes += 1
            if lunes0930 != "": ocupados_lunes += 1
            if lunes1000 != "": ocupados_lunes += 1
            if lunes1030 != "": ocupados_lunes += 1
            libres_lunes = 4 - ocupados_lunes

            ocupados_martes = 0
            if martes0900 != "": ocupados_martes += 1
            if martes0930 != "": ocupados_martes += 1
            if martes1000 != "": ocupados_martes += 1
            libres_martes = 3 - ocupados_martes
                           
            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: Martes")
            else:
                print(f"Ambos dias tiene misma  cantidad de turnos {ocupados_lunes}")

            print("=== Resumen General ===")
            print(f"Operador {operador}")
            print(f"Dia lunes: {ocupados_lunes} turnos ocupados, {libres_lunes}  turnos libres")
            print(f"Dia martes: {ocupados_martes} turnos ocupados, {libres_martes} turnos libres")


        case "5":   #cierra el sistema, se imprime solo por estetica
            print(f"Operador {operador}, aguarde mientras se cierra el sistema")
            print("Sistema Cerrado")
            break
