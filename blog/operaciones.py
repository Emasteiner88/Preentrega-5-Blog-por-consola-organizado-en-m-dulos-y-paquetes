
def listar_posts(lista):
    """Bloque 1: recorre y muestra la lista de Posts."""
    if not lista:
        print("\nNo hay posts para mostrar.")
        return

    print("\nListado de Posts:")
    for numero, post in enumerate(lista, start=1):
        titulo = post.get("titulo") or "[Sin título]"
        autor = post.get("autor")
        
        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "Desconocido")
        else:
            nombre_autor = "Desconocido"

        print(f"{numero}. {titulo} - Autor: {nombre_autor}")


def buscar_por_titulo(lista, termino):
    """Bloque 2: realiza una busqueda por título."""
    resultados = []
    termino_lower = termino.strip().lower()
    
    for post in lista:
        titulo = post.get("titulo", "")
        # Se verifica que sea un string y aplicamos .lower()
        if isinstance(titulo, str) and termino_lower in titulo.lower():
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    """Bloque 3: realiza una busqueda por tags."""
    resultados = []
    tag_lower = tag.strip().lower()
    
    for post in lista:
        tags = post.get("tags", [])
        #Verificamos que sea realmente una lista antes de usar "".join()
        if isinstance(tags, list):
            # Usamos "".join() para convertir la lista en una cadena de texto y aplicamos .lower()
            tags_texto = " ".join(tags).lower()
            if tag_lower in tags_texto:
                resultados.append(post)

    return resultados
