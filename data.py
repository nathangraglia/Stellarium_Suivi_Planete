from sqlite3 import *
import csv

db_path = "positions.db"

def add_db(date, longitude, vitesse, code, zone):
    con = connect(db_path)
    cur = con.cursor()
    cur.execute(f"""INSERT INTO pos(date, longitude, vitesse, code, zone) VALUES(?, ?, ?, ?, ?)""", (date, longitude, vitesse, code, zone))
    con.commit()
    con.close()

def reset_table():
    """
    Réinitialise la table de la BDD pour recommencer à 0
    """
    con = connect(db_path)
    cur = con.cursor()
    cur.execute(f"""DELETE FROM pos""")
    con.commit()
    con.close()

def update(date, zone, code):
    con = connect(db_path)
    cur = con.cursor()
    cur.execute(f"""UPDATE pos SET zone = ?, code = ? WHERE date = ?""", (zone, code, date))
    con.commit()
    con.close()

def get_all():
    """
    Sélectionne l'entièreté de la BDD
    """
    con = connect(db_path)
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM pos""")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def reset_code():
    """
    Réinitialise la valeur de tous les codes
    Évite les erreurs de calculs
    """
    con = connect(db_path)
    cur = con.cursor()
    cur.execute(f"""UPDATE pos SET code = 0, zone = 0""")
    con.commit()
    con.close()

def db_to_csv():
    """
    Convertit la BDD SQL en CSV pour plus de lisibilité
    """
    conn = connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM pos")
    rows = cursor.fetchall()
    # Récupération des noms de colonnes
    col_names = [description[0] for description in cursor.description]
    # Écriture du CSV
    with open("observation.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(col_names)
        writer.writerows(rows)
    conn.close()
