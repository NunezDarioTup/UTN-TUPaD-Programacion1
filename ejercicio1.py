while True:
    nombre = input("Ingre su nombre: \n").strip().title()
    if nombre.isalpha() and nombre != "":
        print(f"Su nombre es {nombre}")
        break
    else:
        print("Ingrese un nombre valido")

while True:
    cantidad = input("Ingrese la cantidad de productos a comprar\n")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        print(f"Usted va a comprar {cantidad}")
        break
    else:
        print("Ingrese un numero entero mayor a 0")

total_con_descuento = 0
total_sin_descuento = 0
productos = []

for i in range(1, cantidad+1):
    while True:
        precio = input(f"Ingrese el precio de {i}:\n")
        if precio.isdigit() and int(precio) > 0:
            precio = int(precio)
            break
        else:
            print("El precio debe ser un número entero.")

    while True:
        descuento=input("Tiene descuento?\n Si\n No\n\n").lower()
        if descuento == "si" or descuento == "no":
           break
        else:
            print("Solamente indique SI o NO")

    total_sin_descuento += precio
            
    if descuento == "si":
        precio_descuento = precio * 0.9
        print(f"El precio de {i} es {precio_descuento:.2f}")
    elif descuento == "no":
        precio_descuento = precio
        print(f"El precio de {i} se mantiene")
    else:
        pass
    total_con_descuento += precio_descuento
    productos.append((i, precio, descuento))   #agrega a la lista

        
ahorro = total_sin_descuento - total_con_descuento
porcentaje_ahorro = (ahorro / total_sin_descuento) * 100
promedio = total_con_descuento / cantidad



print("\n--- RESUMEN  ---")
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
for x in productos:
    print(f"Producto {x[0]} - Precio: {x[1]} Descuento (S/N): {x[2]}")

print(f"El precio que pagaria sin descuentos: $ {total_sin_descuento}")
print(f"El precio con descuentos: $ {total_con_descuento}")
print(f"Ahorro total: $ {ahorro:.2f}, se desconto {porcentaje_ahorro:.2f}%")
print(f"Promedio de precio por producto: {promedio:.2f}")
