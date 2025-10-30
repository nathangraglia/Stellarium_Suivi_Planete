"""
Les valeurs par défaut sont celles utilisées lors de mon projet portant sur saturne, il s'agit de valeur d'exemple.
Elles doivent donc être modifiées en fonctions de vos besoins et de vos choix.
"""

# Ordinateur - Fonctionnement de Stellarium
adresse = "192.xxx.xxx.xxx" # Adresse IP -> A remplacer par votre valeur
port = 1234 # Port -> A remplacer par votre valeur

# Cibles d'observation (Planète et dates)
planete = "Mercure"
date_debut_jul = 2408696.46 # Date de début - Format Julien
date_fin_jul = 2412000.42

# Paramètres d'observations (Intervalle de prise de vue, ...) - A régler en fonction de la planète observée et des choix fais

# Intervalle pardéfaut
intervalle_defaut = 6

# Intervalles dynamiques du plus grand vers le plus petit
intervalle_1 = 10 # Intervalle le plus grand - Entier
seuil_1 = 0.1 # Seuil de l'intervale (vitesse en angle/jour) 
intervalle_2 = 6
seuil_2 = 0.08
intervalle_3 = 5
seuil_3 = 0.06
intervalle_4 = 4 
seuil_4 = 0.04 
intervalle_5 = 2 # Intervalle le plus petit choisi 
seuil_5 = 0.02 # Seuil de l'intervalle
intervalle_minimum = 1 # Intervalle par défaut en cas de seuil inférieur (intervalle minimum) >= 1