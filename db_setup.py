import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Leer el archivo .sql
with open('script.sql', 'r') as file:
    script = file.read()

# Ejecutar el script SQL
cursor.executescript(script)

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()