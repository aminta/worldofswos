"""DRAFT, not built yet: the 'How to install' page (Regia 2026-10-20, after a user found installing too hard).
Main path: the patcher's one-click "Choose the game folder" (Chrome / Edge, coming in 3.3.6's patcher); the old
drag-and-drop method stays as the fallback. [SHOT name] = a patcher / folder screenshot to come from the Regia.
[CHECK] = a fact to confirm before publishing (GOG Mac path, MiSTer procedure).
"""

G = {
 'it': dict(title='Come si installa', lead='Quattro casi, pochi passi. Ti serve una tua copia di SWOS 96/97 (CD o GOG) e il browser Chrome o Edge.',
  common=['Scarica il patcher dalla pagina della release e aprilo con Chrome o Edge.',
          'Premi «Scegli la cartella del gioco» e indica la cartella del gioco (vedi sotto per ogni versione). [SHOT patcher-button]',
          'Il patcher riconosce i file, li modifica e li salva al loro posto. Fatto: avvia il gioco e inizia una nuova carriera. [SHOT patcher-done]'],
  fallback='Se non usi Chrome o Edge: trascina nel patcher l\'eseguibile della tua lingua e i file della cartella DATA, scarica i file modificati e copiali nella cartella del gioco (i TEAM in DATA), dopo averne fatto una copia di sicurezza.',
  cases=[('GOG su Windows', ['La cartella del gioco è di solito C:\\GOG Games\\Sensible World of Soccer 96-97 [CHECK]: è quella che contiene ITALIAN.EXE, ENGLISH.EXE e la cartella DATA.', 'Da GOG Galaxy: Gestisci installazione → Mostra cartella.']),
         ('GOG su Mac', ['Il gioco è dentro l\'app: in Applicazioni, clic destro su Sensible World of Soccer 96-97 → Mostra contenuto pacchetto, poi Contents/Resources/game [CHECK].', 'Nel patcher scegli quella cartella (quella con gli EXE e DATA).']),
         ('CD con DOSBox', ['Scegli la cartella dove hai installato il gioco dal CD (quella che DOSBox monta come C:, con gli EXE e DATA).', 'Avvia poi il gioco da DOSBox come sempre.']),
         ('MiSTer', ['[CHECK] Procedura da confermare: i file del gioco stanno nell\'immagine del disco del core ao486 / z486; copiali sul computer, applica il patcher e rimettili nell\'immagine.'])]),
 'en': dict(title='How to install', lead='Four cases, a few steps. You need your own copy of SWOS 96/97 (CD or GOG) and the Chrome or Edge browser.',
  common=['Download the patcher from the release page and open it in Chrome or Edge.',
          'Press "Choose the game folder" and pick the game\'s folder (see below for each version). [SHOT patcher-button]',
          'The patcher recognises the files, patches them and saves them in place. Done: start the game and begin a new career. [SHOT patcher-done]'],
  fallback='Not using Chrome or Edge? Drop your language\'s executable and the DATA files into the patcher, download the patched files and copy them into the game folder (the TEAM files into DATA), after backing it up.',
  cases=[('GOG on Windows', ['The game folder is usually C:\\GOG Games\\Sensible World of Soccer 96-97 [CHECK]: the one with ENGLISH.EXE and the DATA folder.', 'From GOG Galaxy: Manage installation → Show folder.']),
         ('GOG on Mac', ['The game is inside the app: in Applications, right-click Sensible World of Soccer 96-97 → Show Package Contents, then Contents/Resources/game [CHECK].', 'In the patcher, choose that folder (the one with the EXEs and DATA).']),
         ('CD with DOSBox', ['Choose the folder where you installed the game from the CD (the one DOSBox mounts as C:, with the EXEs and DATA).', 'Then start the game from DOSBox as always.']),
         ('MiSTer', ['[CHECK] Procedure to confirm: the game files are inside the ao486 / z486 core\'s disk image; copy them to a computer, run the patcher and put them back into the image.'])]),
 'fr': dict(title='Comment installer', lead='Quatre cas, quelques étapes. Il vous faut votre propre copie de SWOS 96/97 (CD ou GOG) et le navigateur Chrome ou Edge.',
  common=['Téléchargez le patcher depuis la page de la version et ouvrez-le dans Chrome ou Edge.',
          'Cliquez sur « Choisir le dossier du jeu » et indiquez le dossier du jeu (voir ci-dessous pour chaque version). [SHOT patcher-button]',
          'Le patcher reconnaît les fichiers, les modifie et les enregistre à leur place. C\'est fait : lancez le jeu et commencez une nouvelle carrière. [SHOT patcher-done]'],
  fallback='Sans Chrome ni Edge : déposez dans le patcher l\'exécutable de votre langue et les fichiers du dossier DATA, téléchargez les fichiers modifiés et copiez-les dans le dossier du jeu (les fichiers TEAM dans DATA), après en avoir fait une sauvegarde.',
  cases=[('GOG sur Windows', ['Le dossier du jeu est en général C:\\GOG Games\\Sensible World of Soccer 96-97 [CHECK] : celui qui contient FRENCH.EXE et le dossier DATA.', 'Depuis GOG Galaxy : Gérer l\'installation → Afficher le dossier.']),
         ('GOG sur Mac', ['Le jeu est dans l\'application : dans Applications, clic droit sur Sensible World of Soccer 96-97 → Afficher le contenu du paquet, puis Contents/Resources/game [CHECK].', 'Dans le patcher, choisissez ce dossier (celui avec les EXE et DATA).']),
         ('CD avec DOSBox', ['Choisissez le dossier où vous avez installé le jeu depuis le CD (celui que DOSBox monte comme C:, avec les EXE et DATA).', 'Lancez ensuite le jeu depuis DOSBox comme d\'habitude.']),
         ('MiSTer', ['[CHECK] Procédure à confirmer : les fichiers du jeu sont dans l\'image disque du core ao486 / z486 ; copiez-les sur un ordinateur, lancez le patcher et remettez-les dans l\'image.'])]),
 'de': dict(title='So wird installiert', lead='Vier Fälle, wenige Schritte. Du brauchst deine eigene Kopie von SWOS 96/97 (CD oder GOG) und den Browser Chrome oder Edge.',
  common=['Lade den Patcher von der Release-Seite herunter und öffne ihn in Chrome oder Edge.',
          'Klicke auf „Spielordner wählen“ und wähle den Ordner des Spiels (siehe unten für jede Version). [SHOT patcher-button]',
          'Der Patcher erkennt die Dateien, patcht sie und speichert sie an Ort und Stelle. Fertig: Starte das Spiel und beginne eine neue Karriere. [SHOT patcher-done]'],
  fallback='Ohne Chrome oder Edge: Zieh die ausführbare Datei deiner Sprache und die Dateien aus DATA in den Patcher, lade die gepatchten Dateien herunter und kopiere sie in den Spielordner (die TEAM-Dateien nach DATA), nachdem du ihn gesichert hast.',
  cases=[('GOG unter Windows', ['Der Spielordner ist meist C:\\GOG Games\\Sensible World of Soccer 96-97 [CHECK]: der mit GERMAN.EXE und dem Ordner DATA.', 'In GOG Galaxy: Installation verwalten → Ordner anzeigen.']),
         ('GOG auf dem Mac', ['Das Spiel steckt in der App: In Programme Rechtsklick auf Sensible World of Soccer 96-97 → Paketinhalt zeigen, dann Contents/Resources/game [CHECK].', 'Im Patcher diesen Ordner wählen (den mit den EXE-Dateien und DATA).']),
         ('CD mit DOSBox', ['Wähle den Ordner, in den du das Spiel von der CD installiert hast (den DOSBox als C: einbindet, mit den EXE-Dateien und DATA).', 'Starte das Spiel dann wie gewohnt aus DOSBox.']),
         ('MiSTer', ['[CHECK] Ablauf noch zu bestätigen: Die Spieldateien liegen im Disk-Image des Cores ao486 / z486; kopiere sie auf einen Computer, wende den Patcher an und lege sie zurück ins Image.'])]),
}
