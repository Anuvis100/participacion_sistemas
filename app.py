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



conexion.execute("""
    INSERT INTO libros (titulo, autor, anio_publicacion)
    VALUES ('Cien anios de soledad', 'Gabriel Garcia Marquez', 1967)
""")

conexion.execute("""
    INSERT INTO libros (titulo, autor, anio_publicacion)
    VALUES ('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605)
""")
conexion.execute("""
    INSERT INTO libros (titulo, autor, anio_publicacion)
    VALUES ('La casa de los espiritus', 'Isabel Allende', 1982)
""")


conexion.commit()
print("3 libros insertados")


conexion.execute("""
    INSERT INTO socios (nombre, apellido, email)
    VALUES ('Ana', 'Garcia', 'ana.garcia@email.com')
""")

conexion.execute("""
    INSERT INTO socios (nombre, apellido, email)
    VALUES ('Carlos', 'Rodriguez', 'carlos.rodriguez@email.com')
""")

conexion.commit()
print("2 socios insertados")


conexion.execute("""
    INSERT INTO prestamos (fecha_prestamo, libro_id, socio_id)
    VALUES ('2024-10-31', 1, 1)
""")

conexion.execute("""
    INSERT INTO prestamos (fecha_prestamo, libro_id, socio_id)
    VALUES ('2024-10-31', 2, 1)
""")
conexion.execute("""
    INSERT INTO prestamos (fecha_prestamo, libro_id, socio_id)
    VALUES ('2024-11-01', 3, 2)
""")

conexion.commit()
print("3 prestamos registrados")



cursor = conexion.cursor()

print("\n" + "=" * 50)
print("LISTADO DE LIBROS")
print("=" * 50)
cursor.execute("SELECT * FROM libros")
for fila in cursor.fetchall():
    print(f"ID: {fila[0]} | {fila[1]} - {fila[2]} ({fila[3]})")



