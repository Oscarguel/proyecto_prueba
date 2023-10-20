import sqlite3

def consultar_usuarios():
    try:
        with sqlite3.connect("34.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM Usuarios;")
            usuarios = mi_cursor.fetchall()
            
            if usuarios:
                print("Clave\tNombre")
                for usuario in usuarios:
                    clave, nombre = usuario
                    print(f"{clave}\t{nombre}")
            else:
                print("No se encontraron registros en la tabla Usuarios.")
    except sqlite3.Error as e:
        print(e)
    except Exception as ex:
        print(f"Se produjo el siguiente error: {ex}")
    finally:
        if conn:
            conn.close()

consultar_usuarios()