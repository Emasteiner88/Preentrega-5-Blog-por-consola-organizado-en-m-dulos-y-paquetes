# Este archivo ahora solo importa las herramientas y coordina el bucle principal.

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

def ejecutar_programa():
    # Bucle interactivo
    while True:        
        opcion = mostrar_menu()
        
        if opcion == 1:
            # Bloque 1
            listar_posts(posts)

        elif opcion == 2:
            # Bloque 2
            termino = input("\nIngresá el título o el término a buscar en el Post: ")
            resultados = buscar_por_titulo(posts, termino)
            
            if resultados:
                print("\n=== RESULTADOS ENCONTRADOS ===")
                listar_posts(resultados)
            else:
                print("No se encontraron resultados.")

        elif opcion == 3:
            # Bloque 3
            tag = input("\nIngresá un Tag del post: ")
            resultados = filtrar_por_tag(posts, tag)
            
            if resultados:
                print("\n=== POSTS CON ESE TAG ===")
                listar_posts(resultados)
            else:
                print("No se encontraron resultados.")

        elif opcion == 4:
            # Bloque 4
            print("\n=== VALIDANDO POSTS ===")
            for numero, post in enumerate(posts, start=1):
                es_valido, mensaje = validar_post(post)
                if es_valido:
                    print(f"Post {numero}: válido")
                else:
                    print(f"Post {numero}: error - {mensaje}")

        elif opcion == 5:
            # Bloque 5: Mensaje de salida y el break para terminar el bucle interactivo
            print("\nGracias por usar nuestro Blog Sistem, nos vemos pronto!")
            break 
            
        else:
            # Para opciones inválidas (incluyendo letras y lo que devuelve el except como -1)
            print("\nOpción inválida. Por favor ingrese un número entre 1 y 5.")

# El if __name__ == "__main__": organiza el código para que Python sepa dónde arrancar
if __name__ == "__main__":    
    ejecutar_programa()