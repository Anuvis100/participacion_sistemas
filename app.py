import sqlite3

# ============================================
# 1. CONEXION Y CREACION DE LA BASE DE DATOS
# ============================================
conexion = sqlite3.connect("database.db")
print("Conexion exitosa a la base de datos SQLite")

# ============================================
# 2. TABLA LIBROS
# ============================================
conexion.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        anio_publicacion INTEGER NOT NULL
    )
""")
conexion.commit()
print("Tabla 'libros' creada exitosamente")

# ============================================
# 3. TABLA SOCIOS
# ============================================
conexion.execute("""
    CREATE TABLE IF NOT EXISTS socios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")
conexion.commit()
print("Tabla 'socios' creada exitosamente")

# ============================================
# 4. TABLA PRESTAMOS (con llaves foraneas)
# ============================================
conexion.execute("""
    CREATE TABLE IF NOT EXISTS prestamos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_prestamo TEXT NOT NULL,
        libro_id INTEGER NOT NULL,
        socio_id INTEGER NOT NULL,
        FOREIGN KEY (libro_id) REFERENCES libros(id),
        FOREIGN KEY (socio_id) REFERENCES socios(id)
    )
""")
conexion.commit()
print("Tabla 'prestamos' creada exitosamente")
