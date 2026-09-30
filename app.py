import sqlite3

conn = sqlite3.connect("instituto.db")

conn.execute(
    """
    CREATE TABLE IF NOT EXISTS cursos(
    id INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    horas INTEGER NOT NULL 
    )

    """
)
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS estudiantes(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL
    )
    
    """
    )

cursor = conn.
