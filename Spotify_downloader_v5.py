"""
Scopo: Leggere una playlist spotify e scaricare le canzoni da Youtube Music. 
Lo script verrà chiamato dal main.
"""



id_play="" 
client_ID = ""
client_SECRET = ""
redirect_Uri = "http://127.0.0.1"
username = ""

#Variabili generali
tracce = [] #Titoli canzoni lette
l = [] #Numero tracce salvate, quando è uguale a quello della playlist vuol dire che non ci sono più canzoni
link = [] #Link youtube trovati
mancanti = [] #Canzoni non trovate
da_scaricare = False


def start():

    import spotipy
    from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials 
    import spotipy.util as util
    import json
    from youtubesearchpython import VideosSearch #Per la ricerca video su youtube
    from pytube import YouTube
    from pytube.cli import on_progress
    import sys
    import os
    from ytmusicapi import YTMusic
    from difflib import SequenceMatcher #Cerca somiglianze
    import yt_dlp
    import wget
    from plyer import notification

   
    
    percorso_base =  os.getcwd()
    percorso_base = percorso_base+"/Risorse/"

    #Token permanente
    print(f"USERNAME:{username}")

    #Autorizzazione senza interazione con utente. Non accesso ad informazioni private ;)
    client_credentials_manager = SpotifyClientCredentials(client_id="c20fdc6291024e0a9471857616b680fe",client_secret="fca62c736e12481e8f2794c58a65ddf5")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    ytmusic = YTMusic()

    notification.notify(title = 'SpotiDownloader',message = 'Avvio Script',app_name="SpotiDownloader",ticker="SpotiDownloader",timeout = 5)

    #File di output

    ria = []

    
    nome_playlist = sp.playlist(id_play) #Info playlist
    
    autore = nome_playlist["owner"]
    autore = autore["display_name"]
    autore = ''.join(caratteri for caratteri in autore if caratteri.isalnum())
    print(autore)
    
    try:
        img_playlist = nome_playlist["images"]
        img_playlist = img_playlist[0]
        img_playlist = img_playlist["url"]
        print(img_playlist)

        img_utente = sp.current_user()
        img_utente = img_utente["images"]
        img_utente = img_utente[0]
        img_utente = img_utente["url"]
        print(img_utente, "UTENTE INFo")
    except Exception as err_img:
        print("Errore con Immagini Playlist e utente",err_img)
    

    destinazione = percorso_base+nome_playlist["name"]+"/"
    destinazione = "".join(destinazione.split())
    


    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': destinazione+'%(title)s-YSkip.{ext}',
    }


    print(destinazione)

    if os.path.isdir(destinazione):
        destinazione = destinazione
        print("La destinazione esiste già")
        pass
    else:
        os.mkdir(destinazione)
        autore_path = destinazione+"autore_file.txt"
        autore_file=open(autore_path,"w")
        autore_file.write(autore)
        autore_file.close()

        print("Destinazione creata")

    
    
    
    
    #Ottenere una lista di canzoni presenti nella playlist con: titolo,cantante,durata
    def lettura_playlist():

        for i in range(0,100000,100): #Leggi fin quando non finisci
            results = sp.user_playlist_tracks(username,playlist_id=id_play,limit=100,offset=i)  #Offset=i; Legge tutto
            
            for n,info in enumerate(results["items"]): #Int,Dict

                #Metadati canzoni
                t = info["track"]
                cantante_info = t["artists"]
                cantanti = []
                #Cerca possibili featuring nella canzone
                try:
                    for i in range(100):
                        cantanti.append(cantante_info[i]["name"])
                except:
                    pass
                
                #Salva la canzone nella lista
                tracce.append(t["name"])
                raccolta_finale = {"Nome":t["name"],"Cantanti":str(cantanti),"Durata":str(t["duration_ms"])}
                cerca(t["name"],str(cantanti),str(t["duration_ms"]),len(tracce))
                ria.append(t["name"]+str(cantanti))
                            
            

            if len(tracce) in l:
                dup = set([x for x in ria if ria.count(x) > 1])
                print("Playlist letta completamente",len(tracce)) 
                messaggio = "Playlist letta completamente"+str(len(tracce))

                notification.notify(title = 'SpotiDownloader',message = messaggio,app_name="SpotiDownloader",ticker="SpotiDownloader",timeout = 5)
                print(f"Canzoni duplicate: {dup}, {len(dup)}") #Cerca canzoni duplicate

                messaggio = "Canzoni duplicate:"+str(dup)+ str(len(dup))
                notification.notify(title = 'SpotiDownloader',message = messaggio,app_name="SpotiDownloader",ticker="SpotiDownloader",timeout = 5)
                
                aggiungi_canzoni()

                break #Lettura finita
            else:
                l.append(len(tracce)) #Salva la lunghezza della lista
            

    def cerca(nome,cantanti,durata,segnaposto):
        global mancanti
        
        cantanti = cantanti[2:]
        cantanti = cantanti[:-2]

        durata = float(durata)

        titolo_ricerca = nome

        nome = nome+"-"+cantanti+".mp3"
        nome = "".join(nome.split()) #Rimuove spazi
        salta = False

        if "/" in nome: #Lo / nei titolo porta ad un errore nel download
            nome = nome.replace("/","_YSkip")
        
   

        for nome_file in os.listdir(destinazione):

            
            if nome in nome_file:
                salta = True
            
            if "-YSkip" in nome_file:
                nome_nuovo = nome_file.replace("-YSkip","")
                if "".join((cantanti+"-"+titolo_ricerca).split()) in "".join(nome_nuovo.split()):
                    print("YSKIP Trovato",nome_nuovo,nome_file,segnaposto)
                    salta = True
                    
        if salta != True:
            try:
                while True:
                    print(f"Ricerca {titolo_ricerca}:{cantanti} su Youtube Music {segnaposto}")
                    search_results = ytmusic.search(titolo_ricerca+cantanti)
                    print("RICEFCAT")
                    out= open("out_ricerca.json","w")
                    json.dump(search_results,out)
                    out.close()
                    break
                out= open("out_ricerca.json","r")
                d = json.load(out)

                n = 0
                for chiave in d:
                    n+=1
                
                #Se non viene trovato nulla
                if n==0:
                    print("File vuoto")
                    mancanti.append(nome)

                #Analisi ricerca YTMusic
                for i in range(n):
                
                    if d[i]["resultType"] == "song" or d[i]["resultType"] == "video": 
                        titolo = d[i]["title"]
                        id_canzone = d[i]["videoId"]
                        durata_canzone = d[i]["duration"]

                        try:
                            min,sec = durata_canzone.split(":")
                        except:
                            pass

                        #Converti la durata del video in millisecondi
                        min = int(min)
                        sec = int(sec)
                        min = min*60
                        durata_canzone = (min+sec)*1000
                        
                        unione = titolo_ricerca+cantanti
                        prob1 = SequenceMatcher(None, titolo,unione).ratio()

                        if titolo_ricerca.lower() in titolo.lower() or prob1 >=0.15 and abs(durata_canzone-durata) < 20000:              

                            r = {"Nome":titolo_ricerca,"Cantanti":cantanti,"Durata":durata,"Link":id_canzone}
                            print(r)
                            
                            notification.notify(title = 'SpotiDownloader',message = titolo_ricerca,app_name="SpotiDownloader",ticker="SpotiDownloader",timeout = 3)

                            scarica_canzoni(id_canzone, nome)
                            try:
                                mancanti = [*set(mancanti)] #Rimuove duplicati
                                mancanti.remove(nome)
                            except:
                                pass
                            break
                        else:
                            print(f"No:{titolo_ricerca},{titolo}")
                            mancanti.append(nome)
            except Exception as errore_ricerca:
                print(f"Errore nel contattare il server con la canzone: {titolo_ricerca}:{cantanti}, {errore_ricerca}")

                messaggio = "Errore nel contattare il server con la canzone:"+titolo_ricerca+":"+cantanti
                notification.notify(title = 'SpotiDownloader',message = messaggio,app_name="SpotiDownloader",ticker="SpotiDownloader",timeout = 3)

            

        


    #Nel caso di un errore nel download prova con un'altra libreria
    def errore_download(link_impossibile):
        print("Apertura errore download....")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link_impossibile]) #Si possono inserire anche più url 
                print(f"Scaricata canzone impossibile {link_impossibile}")
                
                messaggio = "Scaricata canzone impossibile"+ link_impossibile
                notification.notify(title = 'SpotiDownloader',message = messaggio,app_name="SpotiDownloader",ticker="SpotiDownloader",timeout = 5)
        except:
            canzoni_non_scaricate = open("Canzoni_impossibili.txt","w")
            canzoni_non_scaricate.write(link_impossibile)
            canzoni_non_scaricate.write("\n")

    def progress(s, chunk, bytes_remaining): #Se il file è di piccole dimensione non mostra nulla
        download_percent = int((s.filesize-bytes_remaining)/s.filesize*100)
        sys.stdout.write(f'\rProgress: {download_percent} %')
        sys.stdout.flush()

    def completato(s,percorso):
        print(f"Download completo {s.title}")
        
        messaggio = "Download completo"+s.title

    def scarica_canzoni(link_1,nome_1):
        
        print("Avvio download...")
        
        try:
            if "https://" in link_1:
                link = link_1
                pass
            else:
                link = "https://music.youtube.com/watch?v="+link_1
            
            print(f"Cercando {link}")

            messaggio = "Cercando"+link

            yt = YouTube(link,on_progress_callback=progress,on_complete_callback=completato) #Cerca il video su Youtube
            audio = yt.streams.get_audio_only() #qualità migliore possibile #Codec default=mp
            dim_bytes = audio.filesize
            dim_mb = dim_bytes/1048576 #Proporzione: 1Mb=1048576Bytes. 
            print(f"Scaricando {nome_1} {dim_mb}")

            messaggio = "Scaricando"+str(nome_1)+str(dim_mb)

            audio.download(destinazione,filename=nome_1) #Scarica mp3 
            

        except Exception as er:
            print(f"Impossibile scaricare il video {link}",er)
            errore_download(link)
            pass
            
            
    def aggiungi_canzoni():

        if len(mancanti) != 0:
            messaggio = "Non è stato possibile scaricare alcune canzoni: "+ str(mancanti)
            print(messaggio)
            notification.notify(title = 'SpotiDownloader',message = messaggio,app_name="SpotiDownloader",ticker="SpotiDownloader",timeout = 10)


    lettura_playlist()

