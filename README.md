# SpotiDownloader_OpenSource
In questa repository sono riportati i programmi essenziali di SpotiDownloader, un progetto nato con lo scopo di scaricare Playlist da Spotify per ascoltare anche offline (funzione a pagamento nella nota applicazione). 
A differenza di altri programmi disponibili sul web, SpotiDownloader offre, grazia al codice disponibile pubblicamente, una garanzia di sicurezza.
In seguito sono riportati i passaggi per avviare il programma e le dipendenze necessarie, è possibile evitare questi passaggi scaricando le repository, sempre su questo utente, con gli eseguibili (Linux e Windows). 

*N.B. Gli eseguibili potrebbero non essere compatibili con la versione del sistema operativo in uso, in tal caso è necessario fare riferimento a questa cartella.*


**Istruzioni (Python, Linux):**
    
    **[Comandi per novizi]**
    1. Installare Python con il comando: *sudo apt-get update* e *sudo apt-get install python3*.
    2. Installere PIP utilizzando il comando: *sudo apt-get install python3-pip*

    **[Comandi per tutti]**
    1) Copiare la cartella di Github in locale scrivendo, sempre nel terminale: *git clone https://github.com/persona1234/SpotiDownloader_OpenSource.git* (Si considera git già installato, in caso di errori installarlo con il comando: *sudo apt-get install git*)
    2) Aprire la cartella appena scaricata e da lì un terminale.
    3) Scaricare le dipendenze necessarie all'applicazione: *pip install -r requirements.txt*
    4) Avviare l'applicazione "main.py" digitando: *python3 main.py*.
    5) Fine.

**Istruzioni (Python, Windows):**

    **[Comandi per novizi]**
    1) Installare Python dal sito ufficiale: *https://www.python.org/downloads/*
    2) Installere PIP (fare riferimento alle guide online)

    **[Comandi per tutti]**
    1) Copiare la cartella di Github in locale collegandosi al seguente link: *https://github.com/persona1234/SpotiDownloader_OpenSource.git* e nella sezione **Code** cliccare su **Download ZIP**
    2) Estrarre il file scaricato in una cartella ed aprirla, da lì aprire una finestra dei comandi (cmd).
    3) Scaricare le dipendenze necessarie all'applicazione: *pip install -r requirements.txt* (o utilizzando: *python -m pip install -r requirements.txt *)
    4) Avviare l'applicazione "main.py" digitando: *python main.py*.
    5) Fine.

**N.B**. La velocità di scaricamento delle canzoni dipende dalla connessione ad Internet e dal numero di brani nella Playlist selezionata. È **importante** che il **link** della Playlist sia indicato per **intero** e che essa sia **pubblica**.
