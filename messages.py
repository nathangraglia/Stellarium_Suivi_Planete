import tkinter as tk
from tkinter import messagebox

def attendre_lancement_stellarium():
    # Création de la fenêtre principale (masquée)
    root = tk.Tk()
    root.withdraw()
    # Affichage de la boîte de dialogue
    messagebox.showinfo(
        title="Lancement de Stellarium",
        message="Veuillez lancer Stellarium puis appuyez sur OK une fois qu'il sera complètement lancé."
    )
    # Une fois OK cliqué
    root.destroy()
    return 0
