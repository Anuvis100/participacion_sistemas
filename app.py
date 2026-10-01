import sqlite3

conexion = sqlite3.connect('database.db')
print("Conexión exitosa a la base de datos SQLite")




conexion.execute("""
    INSERT INTO libros (titulo, autor, anio_publicacion)
    VALUES ('Cien anios de soledad', 'Gabriel Garcia Marquez', 1967)
""")

conexion.commit()
print("1 libros insertados")


conexion.execute("""
    INSERT INTO socios (nombre, apellido, email)
    VALUES ('Ana', 'Garcia', 'ana.garcia@email.com')
""")

conexion.commit()
print("1 socios insertados")

conexion.execute("""
    INSERT INTO prestamos (fecha_prestamo, libro_id, socio_id)
    VALUES ('2024-10-31', 1, 1)
""")


conexion.commit()
print("1 prestamos registrados")