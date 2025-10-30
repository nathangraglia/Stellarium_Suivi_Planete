from recolte import recolte
from analyse import analyse
from data import db_to_csv
from utilitaire import clear
from messages import attendre_lancement_stellarium

def main():
    clear()
    attendre_lancement_stellarium()
    recolte()
    analyse()
    print("Conversion du tableau...")
    db_to_csv()
    print("""Terminé ! Toutes les informations sont sur le fichier "observation.csv" """)
    input("Tapez la touche entrée pour quitter.")

main()