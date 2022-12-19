# SpotiDownloader_OpenSource

SpotiDownloader nasce da un bisogno, sviluppato individualmente, può diventare un progetto **collettivo** (grazie al contributo dei volontari), usufruendo dell'approccio **open source**.

# Cos'è?
In questa repository sono riportate le componenti **essenziali** di SpotiDownloader, un progetto nato con lo scopo di scaricare Playlist da Spotify per poi **ascoltarle** offline (funzione a pagamento nella nota applicazione). 
A differenza di altri programmi disponibili sul web, SpotiDownloader offre, grazia al codice disponibile **pubblicamente**, una garanzia di **sicurezza**.
In seguito sono riportati i passaggi per avviare l'applicazione e le dipendenze necessarie, è possibile evitare questi passaggi scaricando le repository, sempre su questo utente, con gli eseguibili (Linux e Windows). 

*N.B. Gli eseguibili potrebbero non essere compatibili con la versione del sistema operativo in uso, in tal caso è necessario fare riferimento a questa cartella.*


# Istruzioni (Python, Linux):
    
    **[Comandi per principianti]**
    1. Installare Python con il comando: *sudo apt-get update* e *sudo apt-get install python3*. 
    2. Installere PIP utilizzando il comando: *sudo apt-get install python3-pip*

    **[Comandi per tutti]**
    1) Copiare la cartella di Github in locale scrivendo, sempre nel terminale: *git clone https://github.com/persona1234/SpotiDownloader_OpenSource.git* (Si considera git già installato, in caso di errori installarlo con il comando: *sudo apt-get install git*)
    2) Aprire la cartella appena scaricata e da lì un terminale.
    3) Scaricare le dipendenze necessarie all'applicazione: *pip install -r requirements.txt*
    4) Avviare l'applicazione "main.py" digitando: *python3 main.py*.
    5) Fine.
   
Qui sono riportate le immagini dei passaggi su Linux:
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/update.png) [Aggiornamento sorgenti software]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/python.png) [Installazione Python]

![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/pip.png) [Installazione Pip]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/git.png) [Installazione Git]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/clone.png) [Copia repository]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/requirements.png) [Installazione dipendenze]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/home1.png) [Funzioni applicazione]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/avvio.png) [Avvio applicazione]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/download.png) [Download canzoni, viene mostrata una notifica con il nome della canzone]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/cartella1.png) [Mostra, cliccando sulla funzione 1 dell'immagine **Funzioni applicazione**, la playlist scaricata, utile per la copia dei brani su altri dispositivi]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Linux_edit/login.png) [Cambio utente. È possibile, cliccando sulla **funzione 2**, inserire il proprio id utente al posto di quello preimpostato. Per ulteriori indicazioni vedere in calce l'immagine **ID Utente**]



# Istruzioni (Python, Windows 64bit):

    **[Comandi per principianti]**
    1) Installare Python dal sito ufficiale: *https://www.python.org/downloads/*
    
    **[Comandi per tutti]**
    1) Copiare la cartella di Github in locale collegandosi al seguente link: *https://github.com/persona1234/SpotiDownloader_OpenSource.git* e nella sezione **Code** cliccare su **Download ZIP**
    2) Estrarre il file scaricato in una cartella ed aprirla, da lì aprire una finestra dei comandi (cmd).
    3) Scaricare le dipendenze necessarie all'applicazione: *pip install -r requirements.txt* (o utilizzando: *python -m pip install -r requirements.txt *, in caso di errore potrebbe essere necessario sostituire "python" con "py")
    4) Avviare l'applicazione "main.py" digitando: *python main.py* (o py main.py).
    5) Fine.

Qui le istruzione illustrate per Windows:
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/Python_download.png) [Installazione Python per Windows]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/Git_Cartella.png) [Download ZIP programma]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/Cmd_cartella.png) [Chiamare cmd nella cartella estratta dello ZIP, notare il percorso con il prefisso "cmd"]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/Pip_install.png) [Installazione dipendenze]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/App_home1.png) [Avvio applicazione]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/App_avvio.png) [Notifica di inizio lettura Playlist]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/App_scarica.png) [Notifica canzone scaricata]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/Play_letta.png) [Notifica conclusione download canzoni, il numero indica le canzoni presenti nella playlist]

# Extra:
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/Link.png) [Mostra, cliccando sulla *funzione 1* dell'immagine **Avvio applicazione**, la playlist scaricata, utile per la copia dei brani su altri dispositivi]
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/IMG_Windows/Nome_utente.png) [ID Utente, necessario, nella **funzione 2**, se si vuole utilizzare una configurazione diversa da quella preimpostata.]





# Glossario:
    -SpotiDownloader: Il nome del progetto è il risultato della crasi tra Spotify e Downloader, esso sintetizza il suo compito: scaricare serie di canzoni da Spotify.
    -OpenSource: Indica un approccio alla programmazione nel quale si rende il codice sorgente disponibile ad altri.
    -Repository: Il luogo dove vengono conservati i files di un progetto pubblicato su github, ogni repository ha un proprio codice identificativo univoco.
    -Offline: Letteralmente "fuori dalla rete", un utilizzo offline non ha bisogno del collegamento ad Internet.
    -Github: Piattaforma che ospita progetti OpenSource.
    -Playlist: Insieme di brani presenti su Spotify.
    -Download: Tradotto in italiano con "scaricare", rappresenta la copia di un documento da una macchina remota ad una locale.
    -ZIP: Estensione di un archivio compresso.
    -CMD (Command Prompt Commands): Finestra di interazione con il Sistema Operativo.

# Ringraziamenti:
Si ringrazia per l'aiuto, la disponibilità e i suggerimenti Giulia Met.
![alt text](https://github.com/persona1234/SpotiDownloader_OpenSource/blob/main/pinguino.png) 

**N.B**. La velocità di scaricamento delle canzoni dipende dalla connessione ad Internet e dal numero di brani nella Playlist selezionata. È **importante** che il **link** della Playlist sia indicato per **intero** e che essa sia **pubblica**. Inoltre, una volta concluso il download delle canzoni verrà mostrata una notifica di avviso in caso di canzoni duplicate.

*- Andrea Ubaldo Buscetto.*
