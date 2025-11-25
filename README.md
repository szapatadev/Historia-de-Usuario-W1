## Sistema de Registro de Productos
Este programa en Python permite registrar productos mediante una interfaz básica por consola. El usuario puede ingresar el nombre, precio y cantidad de un producto, y el sistema calcula automáticamente el costo total.

# Características
- Menú interactivo con dos opciones:
      1. Registrar producto
      2. Salir
- Validación básica de entradas numéricas.
- Cálculo automático del costo total (precio × cantidad).
- Mensajes informativos y de error para guiar al usuario.

# ¿Cómo funciona?
1. El programa inicia en un bucle while que permanece activo mientras el usuario no elija la opción 2 (Salir).
2. Se solicita al usuario elegir una opción del menú.
3. Si se selecciona 1, se piden los datos del producto:
 - Nombre (texto)
 - Precio (decimal)
 - Cantidad (entero)
4. El sistema calcula:
   costo_total = precio * cantidad
5. Se muestran los resultados en pantalla.
6. El ciclo continúa hasta que el usuario elige salir.

# Estructura del Código
- Validación de entradas: Manejo de errores con try-except para evitar fallos por datos inválidos.
- Cálculo automático: Operación matemática simple para obtener el costo total.
- Interfaz de consola: Menú repetitivo hasta que el usuario salga voluntariamente.

# Ejemplo de ejecución
Registro de productos
 1 - Registrar producto
 2 - Salir
Que quieres? 1

Ingresa el nombre del producto: Manzanas
Ingresa el precio del producto: 2.5
Ingresa la cantidad del producto que tienes: 10

Nombre del producto: Manzanas
Precio unitario: 2.5
Cantidad: 10
Costo total calculado: 25.0
