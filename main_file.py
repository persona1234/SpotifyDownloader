"""
Scopo: Leggere una playlist spotify e scaricare le canzoni da Youtube Music. Questo script è l'UI. 
Script associato al downloader.
"""

import sys
from PyQt6 import uic, QtCore, QtGui, QtWidgets
import os
import threading
import json
import webbrowser


#Ottiene il percorso dove viene eseguito per localizzare le cartelle necessarie al programma
radice_percorso = os.getcwd()
print(radice_percorso)

cartella_essenziali = radice_percorso+"/Essenziali/"

if os.path.isdir(radice_percorso+"/Risorse"):
    print("La cartella Risorse esiste")
else:
    print("La cartella Risorse non esiste")
    os.mkdir(radice_percorso+"/Risorse/")

percorso_or = radice_percorso
radice_percorso = radice_percorso+"/Risorse/"

#Controlla le playlist salvate 
playlists_salvate = os.listdir(radice_percorso)

print(radice_percorso)

print(playlists_salvate,len(playlists_salvate))

#Utile per non avere problemi con i certificati
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class MainWindow(QtWidgets.QMainWindow):
   
    #Funzione per aprire la cartella delle Playlist. Utile per la copia su disco esterno.
    def apri_cartella(self):
        print(f"Aperta {radice_percorso}")
        webbrowser.open(radice_percorso)
    
    #Se è già stato impostato un nome utente richiede solo il link alla Playlist
    def Link_Ricevuto(self):
            cred_file = open(cartella_essenziali+"file_cred.json","r")
            cred_info = json.load(cred_file)

            username_client = cred_info["username_client"]

            link_inserito = self.link_play_widget.text()

            print(link_inserito,"\n",username_client) 
            

            import Spotify_downloader_v5
            
            download_thread = threading.Thread(target=Spotify_downloader_v5.start, name="Downloader")
            download_thread.start()
            
            Spotify_downloader_v5.username = username_client
            Spotify_downloader_v5.id_play=link_inserito

    #Se non c'è un nome Utente salvato chiedilo assieme al link della Playlist
    def Info_Ricevute(self):
        cred_file = open(cartella_essenziali+"file_cred.json","w")

        link_inserito = self.link_play_widget.text()
        username_client = self.username_widget.text()

        username_client = username_client.strip()
        print(link_inserito,"\n",username_client) 
        
        informazioni_cred={"username_client":username_client}
        json.dump(informazioni_cred,cred_file)
        cred_file.close()
        import Spotify_downloader_v5
        
        download_thread = threading.Thread(target=Spotify_downloader_v5.start, name="Downloader")
        download_thread.start()
        
        Spotify_downloader_v5.username = username_client
        Spotify_downloader_v5.id_play=link_inserito

    def cambio_utente(self):
        print("Caricamento schermata iniziale")
        uic.loadUi(cartella_essenziali+"/Spot_test.ui",self)
        self.Fatto_pulsante.clicked.connect(self.Info_Ricevute)
        self.setStyleSheet("background-color: rgb(89, 32, 52);")
    def __init__(self):
        super(MainWindow, self).__init__()
        
        try:
            cred_file = open(cartella_essenziali+"file_cred.json","r") #Se ci sono delle credenziali salvate
            uic.loadUi(cartella_essenziali+"/Spot_test_intro_LogYes.ui",self)
            self.Fatto_pulsante.clicked.connect(self.Link_Ricevuto)
            self.cartella_pulsante.clicked.connect(self.apri_cartella)
            self.uscita_pulsante.clicked.connect(self.cambio_utente)
        except Exception as errore_login:
            print(f"Il file Credenziali non esiste: {errore_login}")
            uic.loadUi(cartella_essenziali+"/Spot_test.ui",self)
            self.Fatto_pulsante.clicked.connect(self.Info_Ricevute)

        self.setStyleSheet("background-color: rgb(89, 32, 52);")
        


app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainWindow = MainWindow()
widget.addWidget(mainWindow)
widget.setFixedHeight(250)
widget.setFixedWidth(800)
widget.setWindowTitle("SpotiDownloader")
widget.show()

sys.exit(app.exec())
print("Uscendo...")