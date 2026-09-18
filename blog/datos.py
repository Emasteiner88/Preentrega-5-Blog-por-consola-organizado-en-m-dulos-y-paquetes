# ==========================================
# 1. DATOS INICIALES Y ESTRUCTURAS
# ==========================================

perfil_autor = {
    "nombre": "Ema Steiner",
    "bio": "Estudiante de Desarrollo Web",
    "especialidad": "Python y Django",
    "redes_sociales": ["ema_dev", "@ema_django", "linkedin.com/in/ema_dev"]
}

estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Django", "Web", "Backend"}

# Lista de publicaciones (incluye datos válidos e inválidos para pruebas)
posts = [
    {
        "id": 1,
        "titulo": "Python desde cero",
        "contenido": "Introducción a Python y Funciones",
        "autor": perfil_autor,
        "tags": ["Python", "Principiante", "beginners"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Introducción a Django",
        "contenido": "Crear aplicaciones web completas en Python",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Framework"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "",  # Inválido: título vacío
        # Inválido: falta la clave "contenido"
        "autor": perfil_autor,
        "tags": "python",  # Inválido: debe ser una lista, no un string
        "estado": "revision"  # Inválido: no pertenece a estados_post
    }   
]
