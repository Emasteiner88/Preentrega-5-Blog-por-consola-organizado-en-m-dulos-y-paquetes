# Sistema de Blog Modular

Este proyecto es la Preentrega 5 del curso. Consiste en la refactorización de un sistema de blog por consola, 
pasando de un script único a una arquitectura modular dividida por responsabilidades (datos, lógica de operaciones, menú, validaciones).

## 🛠️ Requisitos del Entorno

**Python:** 3.10 o superior.
**Sistema Operativo:** Windows, macOS o Linux.
**Librerías externas:** No se requieren (utiliza la biblioteca estándar de Python).

## 🚀 Cómo ejecutar el proyecto

### Cómo ejecutar el proyecto

1. Cloná el repositorio en tu terminal o consola:

```bash
   git clone git clone https://github.com/Emasteiner88/Preentrega-5-Blog-por-consola-organizado-en-m-dulos-y-paquetes.git
   ```
2. Ingresá a la carpeta generada por el repositorio: 

```bash
    cd Preentrega-5-Blog-por-consola-organizado-en-m-dulos-y-paquetes
```
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