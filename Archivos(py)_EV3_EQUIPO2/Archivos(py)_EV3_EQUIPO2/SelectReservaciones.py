import sqlite3

def consultar_reservaciones():
    try:
        with sqlite3.connect("34.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM Reservaciones;")
            reservaciones = mi_cursor.fetchall()
            
            if reservaciones:
                print("Folio\tNombre\tHorario\tFecha")
                for reservacion in reservaciones:
                    folio, nombre, horario, fecha = reservacion
                    print(f"{folio}\t{nombre}\t{horario}\t{fecha}")
            else:
                print("No se encontraron registros en la tabla Reservaciones.")
    except sqlite3.Error as e:
        print(e)
    except Exception as ex:
        print(f"Se produjo el siguiente error: {ex}")
    finally:
        if conn:
            conn.close()

consultar_reservaciones()




