import sqlite3

def consultar_salas():
    try:
        with sqlite3.connect("34.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM Salas;")
            salas = mi_cursor.fetchall()
            
            if salas:
                print("Clave\tNombre\tCapacidad")
                for sala in salas:
                    clave, nombre, capacidad = sala
                    print(f"{clave}\t{nombre}\t{capacidad}")
            else:
                print("No se encontraron registros en la tabla Salas.")
    except sqlite3.Error as e:
        print(e)
    except Exception as ex:
        print(f"Se produjo el siguiente error: {ex}")
    finally:
        if conn:
            conn.close()

consultar_salas()