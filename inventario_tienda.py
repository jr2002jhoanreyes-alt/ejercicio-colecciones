"""
Programa: Sistema de Registro e Inventario de Productos
"""

def mostrar_inventario(inventario):
    """Recorre la colección y muestra todos los productos almacenados."""
    if not inventario:
        print("\n[!] El inventario está vacío actualmente.")
        return

    print("\n--- INVENTARIO ACTUAL ---")
    print(f"{'Código':<10} | {'Nombre':<25} | {'Precio ($)':<12} | {'Cantidad':<10}")
    print("-" * 65)
    for codigo, datos in inventario.items():
        print(f"{codigo:<10} | {datos['nombre']:<25} | {datos['precio']:<12.2f} | {datos['cantidad']:<10}")
    print("-" * 65)


def agregar_producto(inventario):
    """Inserta un nuevo elemento a la colección si el código no existe."""
    print("\n--- AGREGAR PRODUCTO ---")
    codigo = input("Ingrese el código único del producto: ").strip().upper()

    if codigo in inventario:
        print(f"[!] El producto con código {codigo} ya se encuentra registrado.")
        return

    nombre = input("Ingrese el nombre/descripción del producto: ").strip()
    try:
        precio = float(input("Ingrese el precio unitario: "))
        cantidad = int(input("Ingrese el stock inicial: "))
        
        # Almacenamiento en el diccionario
        inventario[codigo] = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        print(f"[✓] Producto '{nombre}' registrado exitosamente.")
    except ValueError:
        print("[X] Error: El precio y la cantidad deben ser valores numéricos válidos.")


def buscar_producto(inventario):
    """Busca un producto por su clave en el diccionario."""
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a buscar: ").strip().upper()

    producto = inventario.get(codigo)
    if producto:
        print("\n[✓] Producto encontrado:")
        print(f"  Código:   {codigo}")
        print(f"  Nombre:   {producto['nombre']}")
        print(f"  Precio:   ${producto['precio']:.2f}")
        print(f"  Stock:    {producto['cantidad']} unidades")
    else:
        print(f"[!] No existe ningún producto con el código {codigo}.")


def eliminar_producto(inventario):
    """Elimina un producto del diccionario utilizando su clave."""
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto que desea eliminar: ").strip().upper()

    if codigo in inventario:
        eliminado = inventario.pop(codigo)
        print(f"[✓] El producto '{eliminado['nombre']}' (Código: {codigo}) ha sido eliminado del sistema.")
    else:
        print(f"[!] No se encontró el código {codigo} para eliminar.")


def main():
    # Inicialización de la colección de datos (diccionario principal con datos base)
    inventario = {
        "MOD-01": {"nombre": "Módulo Sensor Ultrasónico", "precio": 3.50, "cantidad": 25},
        "RES-02": {"nombre": "Pack Resistencias 10k", "precio": 1.20, "cantidad": 100},
        "PLA-03": {"nombre": "Protoboard 830 puntos", "precio": 5.00, "cantidad": 15}
    }

    while True:
        print("\n==============================")
        print("  SISTEMA DE GESTIÓN DE TIENDA")
        print("==============================")
        print("1. Mostrar inventario completo")
        print("2. Registrar nuevo producto")
        print("3. Buscar producto por código")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            agregar_producto(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            eliminar_producto(inventario)
        elif opcion == "5":
            print("\nCerrando el sistema. ¡Hasta luego!")
            break
        else:
            print("\n[X] Opción inválida. Ingrese un número del 1 al 5.")


if __name__ == "__main__":
    main()