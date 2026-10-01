import sqlite3

conexion = sqlite3.connect('database.db')
print("Conexión exitosa a la base de datos SQLite")




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