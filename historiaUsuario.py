print("Registro de productos\n 1 - Registrar producto\n 2 - Salir")
programa = int(input("Que quieres hacer?: "))

while programa < 1 or programa > 2:
    print("Ingresa una opción valida")
    programa = int(input("Que quieres hacer?: "))
else:
    while programa == 1:
        try: 
            nombre = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad del producto que tienes: "))
        except:    
            print("Ingresa correctamente los valores (letras, decimal y entero)")
        costo_total = precio * cantidad
        print(f"Nombre del producto: {nombre}\nPrecio unitario: {precio}\nCantidad: {cantidad}\nCosto total calculado: {costo_total}")
        print("Registro de productos\n 1 - Registrar producto\n 2 - Salir")
        programa = int(input("Que quieres hacer?: "))