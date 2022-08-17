import sqlite3
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivymd.uix.list import OneLineIconListItem

Builder.load_file("libs/uix/kv/screen_home.kv")

class DonneEtudianList(OneLineIconListItem):
    pass
class ScreenHome(Screen):
    """ L'ecran home """
    def rechercher(self,r,t):
        r.data = []
        con = sqlite3.connect("model/engister.db")
        curseur = con.cursor()
        curseur.execute("SELECT * FROM etudiants")
        donnees = curseur.fetchall()

        for donnee in donnees:
            if t in str(donnee):
                r.data.append(
                    {
                        'viewclass': "DonneEtudianList",
                        'markup': True,
                        'text': " trouver: " + f"{str(donnee[1]).lower()} {str(donnee[2])} {str(donnee[3])}"
                    }
                )





