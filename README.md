# Sistema de Gestión de Biblioteca - Python + SQLite

Proyecto de conexión a bases de datos con Python y SQLite
aplicando los conceptos del video "Conexión a Bases de Datos".

## 📋 Estructura de la base de datos

- **libros**: id, titulo, autor, anio_publicacion
- **socios**: id, nombre, apellido, email
- **prestamos**: id, fecha_prestamo, libro_id (FK), socio_id (FK)

## 🚀 Ejecución

```bash
python app.py