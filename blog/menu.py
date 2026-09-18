
def mostrar_menu():
    """Muestra el menú interactivo y maneja errores si el usuario ingresa letras."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")  
    print("5. Salir")          

    try:
        opcion = int(input("Elegí una opción: "))
        return opcion
    except ValueError:
        return -1
