from constantes import *
from os import system

def set_zone(vitesse):
    # Zone
    if vitesse < 0: # Zone 
        zone = 2
    elif vitesse > 0:
        zone = 3
    elif vitesse == 0:
        zone = 0
    return zone

def set_intervalle(vitesse):
    vitesse = abs(vitesse)
    if vitesse >= seuil_1:
        return intervalle_1
    elif vitesse >= seuil_2:
        return intervalle_2
    elif vitesse >= seuil_3:
        return intervalle_3
    elif vitesse >= seuil_4:
        return intervalle_4
    elif vitesse >= seuil_5:
        return intervalle_5
    else :
        return intervalle_minimum # Plus petit intervalle possible = 1

def calc_vitesse(vitesse, intervalle, ancienne, nouvelle):
    # Vitesse[0] = Ancienne vitesse / [1] = Nouvelle vitesse
    vitesse[0] = vitesse[1]
    # Corrige la différence angulaire (évite les sauts à 360°)
    diff = (nouvelle - ancienne + 180) % 360 - 180
    vitesse[1] = round(diff / intervalle, 6)
    # Contrôle de cohérence (ex. si vitesse aberrante)
    if abs(vitesse[1]) >= 10:
        calc = ancienne + nouvelle
        diff = (nouvelle - ancienne + 180) % 360 - 180
        vitesse[1] = round(diff / intervalle, 6)
    return vitesse


def clear():
    try:
        system("cls")
    except:
        system("clear")