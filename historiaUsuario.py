#Se define la variable que va provocar entrar en una opción o no, se define con 0, para que no afecte el funcionamiento del bucle while al iniciarse
programa = 0

#Se crea un bucle while para mostrar todo el contenido del programa, y mantener al usuario mientras que no ponga la opcion 2 (Salir)
while programa != 2:
    #Se verifica que los datos de ingreso en programa correspondan a un integer
    try:
        print("Registro de productos\n 1 - Registrar producto\n 2 - Salir")
        programa = int(input("Que quieres? "))
        print("")
    except:
        print("Agrega una opción valida\n")
    #Se verifica que la opcion ingresada sea una de las opciones brindadas
    if programa < 1 or programa > 2:
        print("Ingresa un valor valido\n")
    #Se ejecuta comienza la ejecución de la opción 1 (Registrar Producto)
    if programa == 1:
        #Se verifica que los datos de ingreso en programa correspondan al solicitado
        try: 
            nombre = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad del producto que tienes: "))
            print("\n")
        except:    
            print("Ingresa correctamente los valores (letras, decimal y entero)")
        #Se hacen los calculos necesarios que solicita el programa
        costo_total = precio * cantidad
        #Se muestran los resultados
        print(f"Nombre del producto: {nombre}\nPrecio unitario: {precio}\nCantidad: {cantidad}\nCosto total calculado: {costo_total}\n")