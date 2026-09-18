# Como la función necesita saber cuáles son los estados permitidos, 
# hacemos un import desde datos.py al principio del archivo.

from blog.datos import estados_post

def validar_post(post):
    """Bloque 4: Controla que el post tenga todas las claves y datos correctos."""
    if not isinstance(post, dict):
        return False, "No es un diccionario."

    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f"Falta la clave '{clave}'"

    titulo = post.get("titulo", "")
    if not isinstance(titulo, str) or not titulo.lower().strip():
        return False, "El 'titulo' está vacío"

    contenido = post.get("contenido", "")
    if not isinstance(contenido, str) or not contenido.lower().strip():
        return False, "El 'contenido' está vacío"

    autor = post.get("autor")
    if not isinstance(autor, dict) or "nombre" not in autor:
        return False, "El 'autor' debe ser un diccionario con la clave 'nombre'"

    if not isinstance(post.get("tags"), list):
        return False, "La clave 'tags' debe ser una lista"

    estado = post.get("estado")
    if estado not in estados_post:
        return False, f"El estado '{estado}' no es válido."

    return True, "válido"