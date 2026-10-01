import sqlite3

conexion = sqlite3.connect('database.db')
print("Conexión exitosa a la base de datos SQLite")




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
    VALUES ('Ana', 'Garcia', 'ana.garcia@email.com')
""")
conexion.execute("""
    INSERT INTO socios (nombre, apellido, email)
    VALUES ('Carlos', 'Rodriguez', 'carlos.rodriguez@email.com')
""")




conexion.commit()
print("3 socios insertados")

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