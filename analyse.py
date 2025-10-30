from data import update, get_all, reset_code

def set_code():
    """
    Assigne les différents codes en fonctions des valeurs
    """
    reset_code() # Réinitialisation des codes pour éviter toute erreur dûe à de précédents tests
    table = get_all() # Récupération des valeurs de l'observation
    # Initialisation des variables de parcours du tableau
    old = table[0]
    actual = table[1]
    aft = table[2]
    mode = 1 # Switch pour éviter des erreurs d'interprétation
    for i in range(4, len(table)-1):
        # MAJ des cases du tableau concernées
        old = table[i-1]
        actual = table[i]
        aft = table[i+1]
        if mode == 0 and actual[2] > aft[2]: # Si il s'agit de la vitesse maximale de la zone
            mode = 1
            update(actual[0], 0, 3) # Code 3 = Vitesse maximale
        elif mode == 1 and actual[2] < aft[2]: # Si il s'agit de la vitesse minimale de la zone
            mode = 0 
            update(actual[0], 0, 1) # Code 1 = Vitesse minimale
        if i > 1: # Si on a passé la première étape (évite erreur d'indice)
            # Mise à jour des valeurs
            old_zero = abs(old[2]) 
            act_zero = abs(actual[2])
            aft_zero = abs(aft[2])
            if act_zero <= old_zero and act_zero < aft_zero: # Si 
                update(actual[0], 0, 2) # Code 2 = Station
        
def set_zone():
    table = get_all() # Récupérations du tableau
    zone, cycle = 2, 1 # Initialisations des variables
    for elt in table: # Pour chaque ligne du tableau
        if elt[3] != 0: # Evite une recherche inutile
            # Affectations des zones en fonctions des valeurs
            if elt[3] == 3:
                zone = 1
                cycle += 1
            elif elt[3] == 2 and zone == 1:
                zone = 2
            elif elt[3] == 1:
                zone = 3
            elif elt[3] == 2 and zone == 3:
                zone = 4
        zone_cycle = f"{zone}.{cycle}" # Création de la str correspondante
        update(elt[0], zone_cycle, elt[3]) # MAJ de la table

def analyse():
    print("Début de la phase d'analyse...")
    print("Ajout des codes : Vitesse Min (1), Station (2) et Vitesse Max (3)")
    set_code()
    print("Ajout des zones")
    set_zone()
    print("Traitement terminé")