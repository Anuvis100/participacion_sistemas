import sqlite3

conexion = sqlite3.connect('database.db')
print("Conexión exitosa a la base de datos SQLite")


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
