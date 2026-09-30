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
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL
    """
    )


conn.execute(
    """
    INSERT INTO cursos (descripcion,horas)
    VALUES('pithon de 0 a experto',40)

    """
)

conn.commit()
