"""Easy-install blocks for /install/ (4.0.6): browser check banner, 'which folder?' box, Program Files steps, first-match card."""
import html

E = html.escape

L = {
 'en': dict(
  ban='This browser cannot do the one-click install (it needs Chrome or Edge, version 86 or later). You can still install by hand: use <a href="#manual">the manual method</a> below, or open this page in Chrome or Edge.',
  wh='Which folder do I pick?',
  wl='Find your case; the patcher wants the folder that contains <code>ENGLISH.EXE</code> and <code>SWOS97.dat</code>.',
  wrows=[('GOG, offline installer', r'Usually <code>C:\GOG Games\Sensible World of Soccer 96-97</code>. Pick it directly.'),
         ('GOG Galaxy (Windows)', r'<code>C:\Program Files (x86)\GOG Galaxy\Games\Sensible World of Soccer 96-97</code> is inside Program Files: Chrome and Edge refuse it. Follow <a href="#progfiles">the Program Files steps</a>.'),
         ('GOG on Mac', 'Inside the app: <a href="#gogmac">see the Mac path</a> (right-click the app, Show Package Contents, twice).'),
         ('CD with DOSBox', 'Do not pick the CD: press "From the CD: copy the game into a new folder" in the patcher.'),
         ('MiSTer', 'You patch your own copy on the computer, then put it on a hard-disk image for the MiSTer: see <a href="#mister">MiSTer</a>.'),
         ('Another DOSBox / eXoDOS', 'The folder with <code>ENGLISH.EXE</code> (the one you mount as C: in DOSBox).')],
  ph='Game in Program Files (GOG Galaxy): step by step',
  pl='Chrome and Edge do not open Program Files ("contains system files"). Work on a copy instead; it takes two minutes.',
  psteps=[r'Open <code>C:\Program Files (x86)\GOG Galaxy\Games</code> in File Explorer and <strong>copy</strong> the folder <code>Sensible World of Soccer 96-97</code> into Documents.',
          'Open the patcher in Chrome or Edge, press "Choose the game folder" and pick the copy in Documents. Wait for "Done".',
          'Open the copy in Documents, select everything inside it, <strong>copy</strong> it, and paste it over the original folder in Program Files. Windows asks for administrator permission: accept, and choose "Replace the files".',
          'Play with the "SWOS Mod - &lt;language&gt;.bat" launchers (see "Starting the game in Italian, French or German" below).'],
  ph2='Tip: the patcher can also install into a new folder, so you skip the copy back (see the new option in the patcher).',
  fh='First match: the short checklist',
  fl=['Start the game with the launcher of your language, not the GOG shortcut (that one is always English).',
      'In the main menu press <strong>CAREER</strong> (a new career: old saves keep the old squads).',
      'Pick your club and play. Controls: arrow keys and Ctrl; with a joypad see the joypad section below.',
      'Something wrong? Your original files are in <code>MOD_BACKUP</code> in the game folder; run the patcher again to update, or <a href="/en/bug/">report a bug</a>.']),
 'it': dict(
  ban='Questo browser non può fare l\'installazione con un clic (serve Chrome o Edge, versione 86 o successiva). Puoi installare a mano: usa <a href="#manual">il metodo a mano</a> qui sotto, oppure apri questa pagina con Chrome o Edge.',
  wh='Quale cartella devo scegliere?',
  wl='Trova il tuo caso; il patcher vuole la cartella che contiene <code>ENGLISH.EXE</code> e <code>SWOS97.dat</code>.',
  wrows=[('GOG, installer offline', r'Di solito <code>C:\GOG Games\Sensible World of Soccer 96-97</code>. Scegli direttamente quella.'),
         ('GOG Galaxy (Windows)', r'<code>C:\Program Files (x86)\GOG Galaxy\Games\Sensible World of Soccer 96-97</code> è dentro Program Files: Chrome ed Edge la rifiutano. Segui <a href="#progfiles">i passi per Program Files</a>.'),
         ('GOG su Mac', 'Dentro l\'app: <a href="#gogmac">vedi il percorso su Mac</a> (tasto destro sull\'app, Mostra contenuto pacchetto, due volte).'),
         ('CD con DOSBox', 'Non scegliere il CD: nel patcher premi «Dal CD: copia il gioco in una nuova cartella».'),
         ('MiSTer', 'Modifichi la tua copia sul computer, poi la metti su un\'immagine di disco per la MiSTer: vedi <a href="#mister">MiSTer</a>.'),
         ('Altro DOSBox / eXoDOS', 'La cartella con <code>ENGLISH.EXE</code> (quella che in DOSBox monti come C:).')],
  ph='Gioco in Program Files (GOG Galaxy): passo per passo',
  pl='Chrome ed Edge non aprono Program Files («contiene file di sistema»). Si lavora su una copia: bastano due minuti.',
  psteps=[r'Apri <code>C:\Program Files (x86)\GOG Galaxy\Games</code> in Esplora risorse e <strong>copia</strong> la cartella <code>Sensible World of Soccer 96-97</code> in Documenti.',
          'Apri il patcher con Chrome o Edge, premi «Scegli la cartella del gioco» e scegli la copia in Documenti. Aspetta «Fatto».',
          'Apri la copia in Documenti, seleziona tutto il contenuto, <strong>copialo</strong> e incollalo sopra la cartella originale in Program Files. Windows chiede il permesso di amministratore: accetta e scegli «Sostituisci i file».',
          'Gioca con i lanciatori «SWOS Mod - &lt;lingua&gt;.bat» (vedi «Avviare il gioco in italiano, francese o tedesco» più sotto).'],
  ph2='Consiglio: il patcher può anche installare in una cartella nuova, così eviti la ricopiatura (vedi la nuova opzione nel patcher).',
  fh='Prima partita: la lista breve',
  fl=['Avvia il gioco con il lanciatore della tua lingua, non con il collegamento di GOG (parte sempre in inglese).',
      'Nel menu principale premi <strong>CARRIERA</strong> (carriera nuova: i salvataggi vecchi tengono le vecchie squadre).',
      'Scegli la tua squadra e gioca. Comandi: frecce e Ctrl; con il joypad vedi la sezione joypad più sotto.',
      'Qualcosa non va? I tuoi file originali sono in <code>MOD_BACKUP</code> nella cartella del gioco; rilancia il patcher per aggiornare, oppure <a href="/it/bug/">segnala un bug</a>.']),
 'fr': dict(
  ban='Ce navigateur ne peut pas faire l\'installation en un clic (il faut Chrome ou Edge, version 86 ou plus récente). Vous pouvez installer à la main : utilisez <a href="#manual">la méthode manuelle</a> ci-dessous, ou ouvrez cette page dans Chrome ou Edge.',
  wh='Quel dossier choisir ?',
  wl='Trouvez votre cas ; le patcher veut le dossier qui contient <code>ENGLISH.EXE</code> et <code>SWOS97.dat</code>.',
  wrows=[('GOG, installateur hors ligne', r'En général <code>C:\GOG Games\Sensible World of Soccer 96-97</code>. Choisissez-le directement.'),
         ('GOG Galaxy (Windows)', r'<code>C:\Program Files (x86)\GOG Galaxy\Games\Sensible World of Soccer 96-97</code> est dans Program Files : Chrome et Edge le refusent. Suivez <a href="#progfiles">les étapes Program Files</a>.'),
         ('GOG sur Mac', 'Dans l\'application : <a href="#gogmac">voir le chemin sur Mac</a> (clic droit sur l\'app, Afficher le contenu du paquet, deux fois).'),
         ('CD avec DOSBox', 'Ne choisissez pas le CD : dans le patcher, appuyez sur « Depuis le CD : copier le jeu dans un nouveau dossier ».'),
         ('MiSTer', 'Vous modifiez votre copie sur l\'ordinateur, puis vous la mettez sur une image de disque pour la MiSTer : voir <a href="#mister">MiSTer</a>.'),
         ('Autre DOSBox / eXoDOS', 'Le dossier avec <code>ENGLISH.EXE</code> (celui que vous montez comme C: dans DOSBox).')],
  ph='Jeu dans Program Files (GOG Galaxy) : pas à pas',
  pl='Chrome et Edge n\'ouvrent pas Program Files (« contient des fichiers système »). On travaille sur une copie : deux minutes suffisent.',
  psteps=[r'Ouvrez <code>C:\Program Files (x86)\GOG Galaxy\Games</code> dans l\'Explorateur et <strong>copiez</strong> le dossier <code>Sensible World of Soccer 96-97</code> dans Documents.',
          'Ouvrez le patcher dans Chrome ou Edge, appuyez sur « Choisir le dossier du jeu » et choisissez la copie dans Documents. Attendez « Terminé ».',
          'Ouvrez la copie dans Documents, sélectionnez tout son contenu, <strong>copiez-le</strong> et collez-le sur le dossier d\'origine dans Program Files. Windows demande l\'autorisation d\'administrateur : acceptez et choisissez « Remplacer les fichiers ».',
          'Jouez avec les lanceurs « SWOS Mod - &lt;langue&gt;.bat » (voir « Lancer le jeu en italien, français ou allemand » plus bas).'],
  ph2='Astuce : le patcher peut aussi installer dans un nouveau dossier, ce qui évite la recopie (voir la nouvelle option du patcher).',
  fh='Premier match : la liste courte',
  fl=['Lancez le jeu avec le lanceur de votre langue, pas avec le raccourci GOG (il lance toujours l\'anglais).',
      'Dans le menu principal, appuyez sur <strong>CARRIÈRE</strong> (nouvelle carrière : les anciennes sauvegardes gardent les anciens effectifs).',
      'Choisissez votre club et jouez. Commandes : flèches et Ctrl ; avec une manette, voir la section manette plus bas.',
      'Un problème ? Vos fichiers d\'origine sont dans <code>MOD_BACKUP</code> dans le dossier du jeu ; relancez le patcher pour mettre à jour, ou <a href="/fr/bug/">signalez un bug</a>.']),
 'de': dict(
  ban='Dieser Browser kann die Ein-Klick-Installation nicht ausführen (nötig sind Chrome oder Edge ab Version 86). Sie können von Hand installieren: nutzen Sie <a href="#manual">die manuelle Methode</a> weiter unten oder öffnen Sie diese Seite in Chrome oder Edge.',
  wh='Welchen Ordner wähle ich?',
  wl='Suchen Sie Ihren Fall; der Patcher braucht den Ordner mit <code>ENGLISH.EXE</code> und <code>SWOS97.dat</code>.',
  wrows=[('GOG, Offline-Installer', r'Meist <code>C:\GOG Games\Sensible World of Soccer 96-97</code>. Wählen Sie ihn direkt.'),
         ('GOG Galaxy (Windows)', r'<code>C:\Program Files (x86)\GOG Galaxy\Games\Sensible World of Soccer 96-97</code> liegt in Program Files: Chrome und Edge lehnen ihn ab. Folgen Sie <a href="#progfiles">den Schritten für Program Files</a>.'),
         ('GOG auf dem Mac', 'In der App: <a href="#gogmac">siehe den Mac-Pfad</a> (Rechtsklick auf die App, Paketinhalt anzeigen, zweimal).'),
         ('CD mit DOSBox', 'Wählen Sie nicht die CD: Drücken Sie im Patcher „Von der CD: Spiel in einen neuen Ordner kopieren“.'),
         ('MiSTer', 'Sie ändern Ihre eigene Kopie am Computer und legen sie dann auf ein Festplatten-Image für die MiSTer: siehe <a href="#mister">MiSTer</a>.'),
         ('Anderes DOSBox / eXoDOS', 'Der Ordner mit <code>ENGLISH.EXE</code> (den Sie in DOSBox als C: einbinden).')],
  ph='Spiel in Program Files (GOG Galaxy): Schritt für Schritt',
  pl='Chrome und Edge öffnen Program Files nicht („enthält Systemdateien“). Man arbeitet an einer Kopie: zwei Minuten genügen.',
  psteps=[r'Öffnen Sie <code>C:\Program Files (x86)\GOG Galaxy\Games</code> im Explorer und <strong>kopieren</strong> Sie den Ordner <code>Sensible World of Soccer 96-97</code> nach Dokumente.',
          'Öffnen Sie den Patcher in Chrome oder Edge, drücken Sie „Spielordner wählen“ und wählen Sie die Kopie in Dokumente. Warten Sie auf „Fertig“.',
          'Öffnen Sie die Kopie in Dokumente, markieren Sie den ganzen Inhalt, <strong>kopieren</strong> Sie ihn und fügen Sie ihn über den Originalordner in Program Files ein. Windows fragt nach Administratorrechten: bestätigen Sie und wählen Sie „Dateien ersetzen“.',
          'Spielen Sie mit den Startdateien „SWOS Mod - &lt;Sprache&gt;.bat“ (siehe „Spiel auf Italienisch, Französisch oder Deutsch starten“ weiter unten).'],
  ph2='Tipp: Der Patcher kann auch in einen neuen Ordner installieren, dann entfällt das Zurückkopieren (siehe die neue Option im Patcher).',
  fh='Erstes Spiel: die kurze Liste',
  fl=['Starten Sie das Spiel mit der Startdatei Ihrer Sprache, nicht mit der GOG-Verknüpfung (sie startet immer Englisch).',
      'Drücken Sie im Hauptmenü <strong>KARRIERE</strong> (neue Karriere: alte Spielstände behalten die alten Kader).',
      'Wählen Sie Ihren Verein und spielen Sie. Steuerung: Pfeiltasten und Strg; mit Joypad siehe den Joypad-Abschnitt weiter unten.',
      'Etwas stimmt nicht? Ihre Originaldateien liegen in <code>MOD_BACKUP</code> im Spielordner; starten Sie den Patcher erneut zum Aktualisieren oder <a href="/de/bug/">melden Sie einen Fehler</a>.']),
}


def banner(lang):
    """Hidden until JS finds no showDirectoryPicker."""
    return (f'<p class="panel next" id="nopicker" hidden>{L[lang]["ban"]}</p>'
            '<script>if(!window.showDirectoryPicker){var n=document.getElementById("nopicker");if(n)n.hidden=false}</script>')


def which(lang, mister=False):
    x = L[lang]
    rows = ''.join(f'<tr><th scope="row">{E(a)}</th><td>{b}</td></tr>' for a, b in x['wrows'] if mister or '#mister' not in b)
    return (f'<h2 id="which">{E(x["wh"])}</h2><p>{x["wl"]}</p>'
            f'<table class="saves"><tbody>{rows}</tbody></table>')


def progfiles(lang, newfolder=False):
    x = L[lang]
    return (f'<h2 id="progfiles">{E(x["ph"])}</h2><p>{E(x["pl"])}</p><ol class="steps">'
            + ''.join(f'<li>{s}</li>' for s in x['psteps']) + '</ol>'
            + (f'<p class="note">{E(x["ph2"])}</p>' if newfolder else ''))


def firstmatch(lang):
    x = L[lang]
    return f'<h2 id="firstmatch">{E(x["fh"])}</h2><ol class="steps">' + ''.join(f'<li>{s}</li>' for s in x['fl']) + '</ol>'


MGL = ('<mistergamedescription>\n <rbf>_computer/z486</rbf>\n'
       ' <file delay="0" type="s" index="2" path="media/swos9697/swos9697_mod.vhd"/>\n'
       ' <reset delay="1"/>\n</mistergamedescription>')

M = {
 'en': dict(h='MiSTer (advanced)', note='Not tested by everyone yet: this is the path we use ourselves, written for people who know their way around a MiSTer. We give no game files and no ready-made disk: you use your own copy of the game and your own DOS.',
  s=['Use the DOS computer cores <strong>z486</strong> (newer, faster) or <strong>ao486</strong> (<code>_Computer</code> menu).',
     'Patch your own copy on the computer with the patcher, as in the CD case ("copy the game into a new folder", for example into a new folder that will become <code>C:\\GAME</code>).',
     'Prepare a bootable hard-disk image (<strong>.vhd</strong>, one FAT16 partition, about 150 MB) with your own DOS: your own MS-DOS, or FreeDOS (free). Copy the patched game folder into it as <code>C:\\GAME</code>. On Windows you can mount the .vhd in Disk Management; on Mac / Linux use the <code>mtools</code> tools.',
     'Put the .vhd on the MiSTer, for example in <code>games/Z486/media/swos9697/</code> (<code>games/AO486/media/...</code> for ao486), and mount it from the OSD (hard disk 0), or start it with a .mgl file in <code>_Computer/_DOS Games</code> (below).',
     'In DOS: <code>cd \\GAME</code> and start the game (the patched executable of your language). The game needs a sound card set up as Sound Blaster (<code>SET BLASTER=A220 I5 D1 H5</code> in AUTOEXEC.BAT). A CD-ROM image is only needed if you also want the game CD mounted (CD driver + MSCDEX in DOS; FreeDOS: SHSUCDX).',
     'CPU speed: we play at about 90 MHz (MiSTer sysctl tool, L1+ L2+). Tested: not yet on a FreeDOS disk.'],
  l='Limits: SWOS++ is untested on MiSTer. Saves go to <code>C:\\GAME</code> inside the .vhd: back the .vhd up. The joypad follows the core\'s own mapping.', m='Example .mgl (index 2 is the hard disk; the CD image, if you use one, is index 4):'),
 'it': dict(h='MiSTer (avanzato)', note='Non è ancora provato da tutti: è il percorso che usiamo noi, scritto per chi conosce già la MiSTer. Non diamo file del gioco né un disco già pronto: usi la tua copia del gioco e il tuo DOS.',
  s=['Usa i core DOS <strong>z486</strong> (più nuovo e veloce) o <strong>ao486</strong> (menu <code>_Computer</code>).',
     'Modifica la tua copia sul computer con il patcher, come per il CD («copia il gioco in una nuova cartella»), per esempio in una cartella nuova che poi diventa <code>C:\\GAME</code>.',
     'Prepara un\'immagine di disco avviabile (<strong>.vhd</strong>, una partizione FAT16, circa 150 MB) con il tuo DOS: il tuo MS-DOS oppure FreeDOS (gratuito). Copiaci la cartella del gioco modificata come <code>C:\\GAME</code>. Su Windows puoi montare il .vhd da Gestione disco; su Mac / Linux usa gli strumenti <code>mtools</code>.',
     'Metti il .vhd sulla MiSTer, per esempio in <code>games/Z486/media/swos9697/</code> (<code>games/AO486/media/...</code> per ao486), e montalo dall\'OSD (hard disk 0), oppure avvialo con un file .mgl in <code>_Computer/_DOS Games</code> (sotto).',
     'In DOS: <code>cd \\GAME</code> e avvia il gioco (l\'eseguibile modificato della tua lingua). Il gioco vuole una scheda audio Sound Blaster (<code>SET BLASTER=A220 I5 D1 H5</code> in AUTOEXEC.BAT). L\'immagine del CD serve solo se vuoi anche il CD del gioco montato (driver CD + MSCDEX in DOS; FreeDOS: SHSUCDX).',
     'Velocità CPU: noi giochiamo a circa 90 MHz (strumento sysctl della MiSTer, L1+ L2+). Provato: non ancora con un disco FreeDOS.'],
  l='Limiti: SWOS++ non è provato sulla MiSTer. I salvataggi finiscono in <code>C:\\GAME</code> dentro il .vhd: fai una copia del .vhd. Il joypad segue la mappatura del core.', m='Esempio di .mgl (index 2 è il disco; l\'immagine del CD, se la usi, è index 4):'),
 'fr': dict(h='MiSTer (avancé)', note='Pas encore testé par tout le monde : c\'est le chemin que nous utilisons nous-mêmes, écrit pour ceux qui connaissent déjà la MiSTer. Nous ne fournissons ni fichiers du jeu ni disque prêt à l\'emploi : vous utilisez votre propre copie du jeu et votre propre DOS.',
  s=['Utilisez les cores DOS <strong>z486</strong> (plus récent et rapide) ou <strong>ao486</strong> (menu <code>_Computer</code>).',
     'Modifiez votre copie sur l\'ordinateur avec le patcher, comme pour le CD (« copier le jeu dans un nouveau dossier »), par exemple dans un nouveau dossier qui deviendra <code>C:\\GAME</code>.',
     'Préparez une image de disque amorçable (<strong>.vhd</strong>, une partition FAT16, environ 150 Mo) avec votre propre DOS : votre MS-DOS, ou FreeDOS (gratuit). Copiez-y le dossier du jeu modifié comme <code>C:\\GAME</code>. Sous Windows, montez le .vhd dans la Gestion des disques ; sous Mac / Linux, utilisez les outils <code>mtools</code>.',
     'Mettez le .vhd sur la MiSTer, par exemple dans <code>games/Z486/media/swos9697/</code> (<code>games/AO486/media/...</code> pour ao486), et montez-le depuis l\'OSD (disque dur 0), ou lancez-le avec un fichier .mgl dans <code>_Computer/_DOS Games</code> (ci-dessous).',
     'Dans DOS : <code>cd \\GAME</code> puis lancez le jeu (l\'exécutable modifié de votre langue). Le jeu veut une carte son Sound Blaster (<code>SET BLASTER=A220 I5 D1 H5</code> dans AUTOEXEC.BAT). L\'image du CD n\'est utile que si vous voulez aussi monter le CD du jeu (pilote CD + MSCDEX sous DOS ; FreeDOS : SHSUCDX).',
     'Vitesse du processeur : nous jouons à environ 90 MHz (outil sysctl de la MiSTer, L1+ L2+). Testé : pas encore avec un disque FreeDOS.'],
  l='Limites : SWOS++ n\'est pas testé sur MiSTer. Les sauvegardes vont dans <code>C:\\GAME</code> à l\'intérieur du .vhd : sauvegardez le .vhd. La manette suit le mappage du core.', m='Exemple de .mgl (index 2 est le disque dur ; l\'image du CD, si vous en utilisez une, est l\'index 4) :'),
 'de': dict(h='MiSTer (fortgeschritten)', note='Noch nicht von allen getestet: Das ist der Weg, den wir selbst nutzen, geschrieben für Leute, die sich mit der MiSTer auskennen. Wir geben weder Spieldateien noch ein fertiges Laufwerk: Sie benutzen Ihre eigene Kopie des Spiels und Ihr eigenes DOS.',
  s=['Nutzen Sie die DOS-Cores <strong>z486</strong> (neuer, schneller) oder <strong>ao486</strong> (Menü <code>_Computer</code>).',
     'Ändern Sie Ihre eigene Kopie am Computer mit dem Patcher, wie bei der CD („Spiel in einen neuen Ordner kopieren“), zum Beispiel in einen neuen Ordner, der später <code>C:\\GAME</code> wird.',
     'Bereiten Sie ein startfähiges Festplatten-Image vor (<strong>.vhd</strong>, eine FAT16-Partition, etwa 150 MB) mit Ihrem eigenen DOS: Ihr MS-DOS oder FreeDOS (kostenlos). Kopieren Sie den geänderten Spielordner als <code>C:\\GAME</code> hinein. Unter Windows können Sie die .vhd in der Datenträgerverwaltung einbinden; auf Mac / Linux nehmen Sie die <code>mtools</code>.',
     'Legen Sie die .vhd auf die MiSTer, zum Beispiel nach <code>games/Z486/media/swos9697/</code> (<code>games/AO486/media/...</code> für ao486), und binden Sie sie im OSD ein (Festplatte 0), oder starten Sie sie mit einer .mgl-Datei in <code>_Computer/_DOS Games</code> (unten).',
     'In DOS: <code>cd \\GAME</code> und das Spiel starten (die geänderte Programmdatei Ihrer Sprache). Das Spiel braucht eine Sound-Blaster-Karte (<code>SET BLASTER=A220 I5 D1 H5</code> in AUTOEXEC.BAT). Ein CD-Image ist nur nötig, wenn auch die Spiel-CD eingebunden sein soll (CD-Treiber + MSCDEX unter DOS; FreeDOS: SHSUCDX).',
     'CPU-Takt: Wir spielen mit etwa 90 MHz (sysctl-Werkzeug der MiSTer, L1+ L2+). Getestet: noch nicht mit einem FreeDOS-Laufwerk.'],
  l='Grenzen: SWOS++ ist auf der MiSTer nicht getestet. Spielstände landen in <code>C:\\GAME</code> innerhalb der .vhd: sichern Sie die .vhd. Das Joypad folgt der Belegung des Cores.', m='Beispiel für eine .mgl (index 2 ist die Festplatte; das CD-Image, falls verwendet, ist index 4):'),
}


def mister(lang):
    x = M[lang]
    return (f'<h2 id="mister">{E(x["h"])}</h2><p class="panel next">{E(x["note"])}</p><ol class="steps">'
            + ''.join(f'<li>{i}</li>' for i in x['s']) + f'</ol><p>{x["m"]}</p>'
            f'<pre class="panel" style="white-space:pre-wrap;overflow-wrap:anywhere;font-size:14px">{E(MGL)}</pre><p>{x["l"]}</p>')


PL = {
 'en': ('World 2026-27 player list',
        'Every player of the World 2026-27 (mod 4.1.2) with club, position, all 7 skills and price: handy for spotting bargains on the transfer market. CSV file: it opens in Excel, LibreOffice or Google Sheets.',
        'Download the player list (CSV)',
        ('CSV column', 'Letter in your game', 'Meaning'),
        [('P','P','passing'),('V','V','shot power'),('H','H','heading'),('T','T','tackling'),('C','C','ball control'),('S','S','speed'),('F','F','finishing')],
        'A starred skill in the game (key skill) is listed in the key_skills column. Skills go from 0 to 7.'),
 'it': ('Lista giocatori Mondo 2026-27',
        'Tutti i giocatori del Mondo 2026-27 (mod 4.1.2) con squadra, ruolo, le 7 abilità e il prezzo: comoda per scovare gli affari sul mercato. File CSV: si apre con Excel, LibreOffice o Google Fogli.',
        'Scarica la lista giocatori (CSV)',
        ('Colonna del CSV', 'Lettera nel tuo gioco', 'Significato'),
        [('P','P','passaggio'),('V','C','tiro (potenza)'),('H','T','colpo di testa'),('T','F','contrasto (in gioco "FALCIARE")'),('C','A','controllo palla (in gioco "AGILITA\'")'),('S','V','velocità'),('F','S','finalizzazione (in gioco "SEGNARE")')],
        'Un\'abilità con la stella nel gioco (abilità chiave) è indicata nella colonna key_skills. Le abilità vanno da 0 a 7.'),
 'fr': ('Liste des joueurs du Monde 2026-27',
        'Tous les joueurs du Monde 2026-27 (mod 4.1.2) avec club, poste, les 7 qualités et le prix : pratique pour repérer les bonnes affaires sur le marché des transferts. Fichier CSV : il s\'ouvre dans Excel, LibreOffice ou Google Sheets.',
        'Télécharger la liste des joueurs (CSV)',
        ('Colonne du CSV', 'Lettre dans votre jeu', 'Signification'),
        [('P','P','passe'),('V','R','tir (puissance)'),('H','T','jeu de tête'),('T','I','tacle'),('C','C','contrôle du ballon'),('S','V','vitesse'),('F','A','finition')],
        'Une qualité marquée d\'une étoile dans le jeu (qualité clé) figure dans la colonne key_skills. Les qualités vont de 0 à 7.'),
 'de': ('Spielerliste Welt 2026-27',
        'Alle Spieler der Welt 2026-27 (Mod 4.1.2) mit Verein, Position, allen 7 Fähigkeiten und Preis: praktisch, um auf dem Transfermarkt Schnäppchen zu finden. CSV-Datei: öffnet sich in Excel, LibreOffice oder Google Sheets.',
        'Spielerliste herunterladen (CSV)',
        ('CSV-Spalte', 'Buchstabe in Ihrem Spiel', 'Bedeutung'),
        [('P','P','Passen'),('V','G','Schießen (Schusskraft)'),('H','K','Kopfball'),('T','Z','Tackling'),('C','B','Ballkontrolle'),('S','S','Geschwindigkeit'),('F','A','Abschluss')],
        'Eine Fähigkeit mit Stern im Spiel (Schlüsselfähigkeit) steht in der Spalte key_skills. Die Fähigkeiten gehen von 0 bis 7.'),
}


def players(lang):
    h, d, b, th, rows, k = PL[lang]
    tb = ''.join(f'<tr><td><code>{E(a)}</code></td><td><strong>{E(c)}</strong></td><td>{E(m)}</td></tr>' for a, c, m in rows)
    return (f'<h2 id="players">{E(h)}</h2><p>{E(d)}</p>'
            f'<p><a class="btn" href="/static/players-2627-4.1.2.csv" download>{E(b)}</a></p>'
            f'<table class="saves"><thead><tr>' + ''.join(f'<th>{E(x)}</th>' for x in th) + f'</tr></thead><tbody>{tb}</tbody></table>'
            f'<p class="note">{E(k)}</p>')
