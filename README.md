# Sistema de Blog Modular

Este proyecto es la Preentrega 5 del curso. Consiste en la refactorización de un sistema de blog por consola, 
pasando de un script único a una arquitectura modular dividida por responsabilidades (datos, lógica de operaciones, menú, validaciones).

## 🚀 Cómo ejecutar el proyecto

1. Abrí tu terminal o consola.
2. Posicionate en la carpeta raíz del proyecto (`blog_consola`).
3. Ejecutá el programa principal con:

```bash
python main.py
```

### ESTRUCTURA DE MODULOS

1. El proyecto está separado en un paquete principal llamado blog:

2. main.py: Punto de entrada del programa. Orquesta el bucle interactivo.

3. blog/datos.py: Contiene las estructuras de datos, perfil de autor (Ema Steiner) y los posts simulados (válidos e inválidos).

4. blog/menu.py: Encargado de imprimir el menú y manejar errores de ValueError en el input.

5. blog/operaciones.py: Está conformado por la lógica para listar posts, buscar por título y filtrar etiquetas iterando strings.

6. blog/validaciones.py: Contiene el algoritmo que verifica la integridad estructural de cada diccionario simulando un post.