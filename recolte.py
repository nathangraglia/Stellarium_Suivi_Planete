import StellariumRC # pip install stellariumrc nécessaire
from time import sleep
from constantes import *
from data import *
from utilitaire import *

def lancement_stellarium():
    # init
    s = StellariumRC.Stellarium(adresse, port) # Connexion à Stellarium - Stellarium doit être lancé

    # Lancement du suivi
    s.main.setTimeRate(0) # Figer le temps
    s.main.setTimeJD(date_debut_jul) # Fixer la date à celle du début
    s.main.setFocus(target=planete,mode='zoom') # Suivre la planète (pour vérification visuelle)

    return s

def get_data(date, s):
    x = round(float(s.objects.getInfo(planete)["elong"]), 3) # On récolte la longitude arrondie à 3 chiffre
    return (date, x)

def recolte():
    s = lancement_stellarium() # Connexion à Stellarium et initialisation
    reset_table() # Remise à zéro du tableau

    # Initialisation des variables utiles
    date = date_debut_jul # On commence par la date de début
    vitesse = [0, 0] # Initialisation des vitesse (Ancienne et nouvelle vitesse)
    min, max = -1000, -1000
    i = 0
    intervalle = intervalle_defaut

    print("Lancement de l'observation\nVeuillez patienter...")
    while date < date_fin_jul: # On récolte les données jusqu'à la date finale souhaitée
        x = get_data(date, s) # Récolte de la position à la date précise

        # Vitesse 
        if date != date_debut_jul:
            vitesse = calc_vitesse(vitesse, intervalle, x[1], longitude) # Calcul de la vitesse de l'objet
        longitude = x[1]

        # Zones
        zone = set_zone(vitesse[1]) # Définition de la zone dans laquelle se trouve l'objet
        add_db(x[0], x[1], vitesse[1], 0, zone) # Ajout au tableau
        date += intervalle # Incrémentation de la date
        s.main.setTimeJD(date) # Actualisation de la date
        i+=1
    print("Observation terminée")

