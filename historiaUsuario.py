programa = 0

while programa != 2:
    try:
        print("Registro de productos\n 1 - Registrar producto\n 2 - Salir")
        programa = int(input("Que quieres? "))
        print("")
    except:
        print("Agrega una opción valida\n")
    if programa < 1 or programa > 2:
        print("Ingresa un valor valido\n")
    if programa == 1:
        try: 
            nombre = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad del producto que tienes: "))
            print("\n")
        except:    
                print("Ingresa correctamente los valores (letras, decimal y entero)")
        costo_total = precio * cantidad
        print(f"Nombre del producto: {nombre}\nPrecio unitario: {precio}\nCantidad: {cantidad}\nCosto total calculado: {costo_total}\n")