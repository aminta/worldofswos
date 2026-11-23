"""4.2: the Gameplay page (OPTIONS -> GAMEPLAY) and the home's 'out now: 4.2' panel, 4 languages.

Source of every fact: the mod's release/notes-4.2.md (v4.2, tag 951d82e); the menu labels as each exe spells them
(tools/gameplay.py, difficulty.py, setpieces.py, practice.py, cpucards.py, gkinj.py on main; the switch words from the
release exes). The CPU BUILD UP line follows tools/buildup.py's own description (not in the notes).
Frames: gp-<slot>-<lang>.png (a menu, one per language) and gp-match-<x>.png (an in-match shot, no menu text).
"""

# the CUSTOM GAMEPLAY page's rows, as the game spells them: (label, values in the order shown here, start value)
ROWS = {
    'en': [('DIFFICULTY', 'EASY · NORMAL · HARD', 'NORMAL'), ('DRIBBLING', 'CLASSIC · NEW · CUSTOM', 'CLASSIC'),
           ('SET PIECES', 'CLASSIC · REALISTIC · ARCADE', 'CLASSIC'), ('CPU RED CARDS', 'ON · OFF', 'ON'),
           ('CPU INJURIES', 'ON · OFF', 'ON'), ('GOALKEEPER INJURIES', 'ON · OFF', 'ON'), ('ROLES', 'ON · OFF', 'OFF')],
    'it': [("DIFFICOLTA'", 'FACILE · NORMALE · DIFFICILE', 'NORMALE'), ('DRIBBLING', 'CLASSICO · NUOVO · PERSONALIZZATO', 'CLASSICO'),
           ('CALCI PIAZZATI', 'CLASSICI · REALISTICI · ARCADE', 'CLASSICI'), ('ROSSI ALLA CPU', 'ATTIV. · DISATT.', 'ATTIV.'),
           ('INFORTUNI ALLA CPU', 'ATTIV. · DISATT.', 'ATTIV.'), ('INFORTUNI PORTIERI', 'ATTIV. · DISATT.', 'ATTIV.'),
           ('RUOLI', 'ATTIV. · DISATT.', 'DISATT.')],
    'fr': [('DIFFICULTE', 'FACILE · NORMAL · DIFFICILE', 'NORMAL'), ('DRIBBLE', 'CLASSIQUE · NOUVEAU · PERSONNALISE', 'CLASSIQUE'),
           ('COUPS DE PIED ARRETES', 'CLASSIQUES · REALISTES · ARCADE', 'CLASSIQUES'),
           ('CARTONS ROUGES CPU', 'ACTIVE · DESACTIVE', 'ACTIVE'), ('BLESSURES CPU', 'ACTIVE · DESACTIVE', 'ACTIVE'),
           ('BLESSURES DES GARDIENS', 'ACTIVE · DESACTIVE', 'ACTIVE'), ('APTITUDES PAR POSTE', 'ACTIVE · DESACTIVE', 'DESACTIVE')],
    'de': [('SCHWIERIGKEIT', 'LEICHT · NORMAL · SCHWER', 'NORMAL'), ('DRIBBLING', 'KLASSISCH · NEU · INDIVIDUELL', 'KLASSISCH'),
           ('STANDARDSITUATIONEN', 'KLASSISCH · REALISTISCH · ARCADE', 'KLASSISCH'), ('ROTE KARTEN CPU', 'EIN · AUS', 'EIN'),
           ('VERLETZUNGEN CPU', 'EIN · AUS', 'EIN'), ('TORWARTVERLETZUNGEN', 'EIN · AUS', 'EIN'), ('SPIELERTYPEN', 'EIN · AUS', 'AUS')],
}

# frame slots: (name, per-language?) -> caption per language
FRAMES = {
    'options': (True, {'en': 'The OPTIONS menu: the new GAMEPLAY row', 'it': 'Il menu OPZIONI: la nuova riga GAMEPLAY',
                       'fr': 'Le menu OPTIONS : la nouvelle ligne GAMEPLAY', 'de': 'Das Menü OPTIONEN: die neue Zeile SPIELWEISE'}),
    'custom': (True, {'en': 'The CUSTOM GAMEPLAY page, one row per option', 'it': 'La pagina GAMEPLAY PERSONALIZZATO, una riga per opzione',
                      'fr': 'La page GAMEPLAY PERSONNALISE, une ligne par option', 'de': 'Die Seite SPIELWEISE INDIVIDUELL, eine Zeile pro Option'}),
    'dribbling': (True, {'en': 'The CUSTOM DRIBBLING page, on the values of NEW', 'it': 'La pagina DRIBBLING PERSONALIZZATO, con i valori di NUOVO',
                         'fr': 'La page DRIBBLE PERSONNALISE, avec les valeurs de NOUVEAU', 'de': 'Die Seite DRIBBLING INDIVIDUELL mit den Werten von NEU'}),
    'practice': (True, {'en': 'The TRAINING page of a career', 'it': 'La pagina PRATICA della carriera',
                        'fr': "La page ENTRAINEMENT d'une carrière", 'de': 'Die Seite TRAINING einer Karriere'}),
    'practice-results': (True, {'en': 'After a free kick practice: SHOTS and GOALS', 'it': 'Dopo una prova punizioni: TIRI e GOL',
                                'fr': 'Après un entraînement aux coups francs : TIRS et BUTS', 'de': 'Nach einem Freistoßtraining: SCHUESSE und TORE'}),
    'match-dribbling': (False, {'en': 'Dribbling in a match', 'it': 'Il dribbling in partita', 'fr': 'Le dribble en match',
                                'de': 'Dribbling im Spiel'}),
    'match-setpieces': (False, {'en': 'A set piece in a match', 'it': 'Un calcio piazzato in partita', 'fr': 'Un coup de pied arrêté en match',
                                'de': 'Eine Standardsituation im Spiel'}),
    'match-roles': (False, {'en': 'Position traits in a match', 'it': 'Le abilità per ruolo in partita', 'fr': 'Les aptitudes par poste en match',
                            'de': 'Spielertypen im Spiel'}),
}

P = {
 'en': dict(
  nav='Gameplay', title='Gameplay: how the mod plays',
  lead='Version 4.2 changes how a match plays, if you want it to: difficulty, dribbling, set pieces and position traits, '
       'each with a choice of its own. And one switch gives you back the 1996 game, exactly.',
  table=('Option', 'Values', 'New install'),
  preview='Preview: the Italian screen stands in until the {L} one is captured.',
  end=('Download the patcher', "What's new in 4.2", 'All the 4.2 notes on GitHub'),
  sec=[
   ('where', 'Where: OPTIONS → GAMEPLAY', [
    ('p', "Everything is in one row of the game's <strong>OPTIONS</strong> menu: <strong>GAMEPLAY</strong>. It has two values:"),
    ('ul', ['<strong>ORIGINAL</strong>: the game as it was in 1996, exactly. Every option on this page acts as in the original game, '
            'but what you chose is not forgotten: go back to CUSTOM and your settings are there as you left them.',
            '<strong>CUSTOM</strong> (the default): press FIRE on it and the <strong>CUSTOM GAMEPLAY</strong> page opens, one row per option.']),
    ('p', "On that page LEFT / RIGHT change a row's value and FIRE moves it on to the next one. <strong>DEFAULTS</strong> puts every row "
          'back to its start value, <strong>BACK</strong> leaves the page. A career remembers its choices: a career saved on ORIGINAL stays on ORIGINAL.'),
    ('table', None),
    ('p', 'The new options all start from the original game (NORMAL, CLASSIC, CLASSIC, ROLES OFF), so nothing changes until you choose. '
          'If you played 4.1, GAMEPLAY starts on CUSTOM with the settings you already had.'),
    ('frames', ['options', 'custom'])]),
   ('difficulty', 'DIFFICULTY: EASY, NORMAL, HARD', [
    ('p', 'How strong the computer is when it plays against you. <strong>NORMAL</strong> is the original game.'),
    ('ul', ["<strong>EASY</strong>: the computer team's players are 80% as good, its goalkeeper is 2 points weaker and its passes go astray more often.",
            '<strong>HARD</strong>: its players are 10% better, its goalkeeper 2 points stronger and its passes more accurate.']),
    ('p', 'The level changes only a computer team that plays against you. Two human players, computer against computer, training games, '
          'SWOS++ (the add-on for the English game) and simulated results (the matches the game works out without playing them) always play the original game.')]),
   ('dribbling', 'DRIBBLING: CLASSIC, NEW, CUSTOM', [
    ('p', 'Dribbling means running past an opponent with the ball at your feet. <strong>CLASSIC</strong> is the original game; '
          '<strong>NEW</strong> is the mod\'s new dribbling, ready to play; <strong>CUSTOM</strong> lets you set each part of it yourself. With NEW:'),
    ('ul', ['your player slows down less when he runs with the ball;',
            'on sharp turns the ball stays closer to his feet;',
            'after winning the ball you keep it a moment longer before anyone can take it back;',
            'the computer slides in less often, and never while you dribble inside its own penalty area;',
            "its second man holds back further, instead of closing in on you together with the first;",
            'after losing the ball to a strong tackle, the computer needs a moment longer to win it back.']),
    ('p', "To be honest: in 4.2 the computer's defenders press and cover more (fewer 'skittles' standing still while you go past them), "
          'but they don\'t tackle more often.'),
    ('p', 'These settings apply only while the ball is in play: free kicks, corners, throw-ins, goal kicks and kick-offs stay as in the original game. '
          'Like DIFFICULTY, they act in your matches against the computer.'),
    ('h3', 'The CUSTOM DRIBBLING page'),
    ('p', 'DRIBBLING on CUSTOM opens a page of its own. A number row shows a step: 0 is the original game, and the higher the step, '
          'the more help you get (the legend at the bottom: LEFT: CLASSIC, RIGHT: MORE HELP). <strong>DEFAULTS</strong> puts back the values of NEW, '
          'for example SPEED WITH BALL 2 of 4 and BALL CLOSE ON TURNS 4 of 10; <strong>BACK</strong> returns to the CUSTOM GAMEPLAY page.'),
    ('ul', ['<strong>SPEED WITH BALL</strong>: how little your player slows down when he runs with the ball.',
            '<strong>BALL CLOSE ON TURNS</strong>: how close the ball stays to his feet on sharp turns.',
            '<strong>BALL SHIELDING</strong>: how long you keep the ball after winning it, before an opponent can take it back.',
            "<strong>FEWER CPU SLIDES</strong>: the computer's players start a sliding tackle only from closer, so less often.",
            "<strong>LESS CPU DOUBLING</strong>: how far back the computer's second man stays, instead of closing in on you with the first.",
            '<strong>CPU WIN BACK DELAY</strong>: how long the computer waits before going for the ball again after losing it to a strong tackle.',
            '<strong>NO SLIDES IN BOX</strong>: ON, the computer never slides in while you dribble inside its penalty area, where every foul is a penalty; '
            'OFF, it can, as in the original game. ON with NEW.',
            "<strong>CPU DEFENDERS</strong>: how the computer's defenders face you. <strong>CHASE</strong>: they run after you, as in the original game "
            '(the value of NEW); <strong>WAIT</strong>: they stay between you and the goal instead of chasing you from behind; '
            '<strong>COVER</strong> and <strong>ONE AT A TIME</strong>: one man presses you and a team-mate covers behind him.',
            "<strong>CPU BUILD UP</strong>: ON, the computer's team builds its play more calmly: its goalkeeper looks for a free team-mate more often "
            'and, under pressure, it kicks the ball long less often. OFF, as in the original game. ON with NEW.']),
    ('frames', ['dribbling', 'match-dribbling'])]),
   ('setpieces', 'SET PIECES: CLASSIC, REALISTIC, ARCADE', [
    ('p', 'Set pieces are the restarts with the ball standing still: free kicks, corners and the like. Three values, for every match; '
          '<strong>CLASSIC</strong> is the original game.'),
    ('p', '<strong>REALISTIC</strong>:'),
    ('ul', ['headers from corners and crosses go down instead of over the bar; a good header of the ball keeps it under the bar from further out;',
            'goalkeepers no longer catch everything that drops into the six-yard box;',
            'the computer goes for high balls more often;',
            "free kicks near the box dip over the wall the way real ones do, and how often they go in depends on the taker's shooting, "
            'as in real football: a top specialist scores about one in ten, an average taker one in fifteen, a weak one about one in thirty. '
            "When the computer's free kick misses, it goes over the bar or into the wall."]),
    ('p', '<strong>ARCADE</strong>:'),
    ('ul', ['the same headers and goalkeepers as REALISTIC;',
            'more free kicks around the box: there, a clean tackle is whistled as a foul one time in three;',
            'the computer curls its free kicks towards the far post: a top shooter scores about one in six from 20-25 metres, a weak one hardly ever.']),
    ('p', 'Your own free kicks stay in your hands, direction and curl, in every mode.'),
    ('frames', ['match-setpieces'])]),
   ('roles', 'ROLES: position traits', [
    ('p', 'A position trait is something a player does better because of his position. With <strong>ROLES</strong> on <strong>ON</strong> '
          '(it starts on OFF, the original game) every team has them, the computer\'s too. The position is the player\'s natural one, '
          'the one in his team\'s file, not the place where you put him in the line-up. An idea of Marco\'s.'),
    ('ul', ["<strong>Headers down in the opponents' box</strong>: any outfield player heading the ball inside the opponents' penalty area "
            'aims it down, the more so the better he is in the air. Lobbed headers (stick held back) and standing headers don\'t change; '
            'anywhere else, headers go up and away as in the original game.',
            "<strong>The winger's whipped cross</strong>: a right or left winger (RW / LW) out wide in the last quarter of the pitch "
            "plays a low, fast cross into the box with the 'back' after-touch (the stick moved just after the kick) instead of the high ball. "
            'The same from a corner or a free kick out wide taken by a winger, when the ball goes towards the middle. '
            "The computer's wingers rarely play this ball, so the whipped cross is mostly yours.",
            '<strong>Centre-backs</strong> (D) reach high balls a little further in their own penalty area, the more so the better they are in the air.']),
    ('p', 'With SET PIECES on REALISTIC or ARCADE every header already goes down; with ROLES on, only those in the opponents\' box do. '
          'ROLES OFF, GAMEPLAY ORIGINAL, SWOS++ and training games always play the original game; the set-piece practice uses the traits as a match would.'),
    ('frames', ['match-roles'])]),
   ('cards', 'Cards and injuries', [
    ('p', 'The CUSTOM GAMEPLAY page also holds three options from earlier versions of the mod, ON at the start:'),
    ('ul', ["<strong>CPU RED CARDS</strong>: the computer's players are booked and sent off like yours. "
            'In the original game a computer player was never sent off and never got a second yellow card.',
            "<strong>CPU INJURIES</strong>: the computer's players get injured like yours.",
            "<strong>GOALKEEPER INJURIES</strong>: after every match each team's goalkeeper has a 1 in 25 chance of an injury "
            'that keeps him out for one or two matches.']),
    ('p', 'OFF, or GAMEPLAY on ORIGINAL, plays the original game.')]),
   ('practice', 'Set-piece practice', [
    ('p', 'In a career, the <strong>TRAINING</strong> button on your squad screen now opens a page of its own:'),
    ('ul', ['<strong>TRAINING MATCH</strong>: the training game, as before;',
            '<strong>FREE KICK PRACTICE</strong>, <strong>PENALTY PRACTICE</strong>, <strong>CORNER PRACTICE</strong>: the set piece comes '
            'again and again, the ball placed for you each time: free kicks from the centre and from both sides at four distances from goal, '
            'penalties, corners from both sides. No match clock, no stadium presentation, no score bar: just the set pieces;',
            '<strong>PLAY IN ATTACK</strong> / <strong>PLAY IN DEFENCE</strong>: in attack your team takes the set piece; '
            'in defence the computer takes it and you defend.']),
    ('p', '<strong>SHOTS</strong> sets the number of attempts: 5, 10, 20, 50 or UNLIMITED (10 at first). <strong>HALF</strong> sets the goal: '
          'RANDOM (the one the match gives you), TOP, BOTTOM or ALTERNATING. Press ESC whenever you like. A results page then shows '
          'SHOTS and GOALS: <strong>OK</strong> takes you back, <strong>TRY AGAIN</strong> starts another series of the same practice.'),
    ('p', 'A practice never changes your career more than a training game already does. With GAMEPLAY on ORIGINAL the page title '
          'reads TRAINING - GAMEPLAY: ORIGINAL and the practice plays the classic set pieces.'),
    ('frames', ['practice', 'practice-results'])]),
  ],
  # the home after the 4.2 release
  h42='Out now: SWOS 96/97 Mod 4.2',
  p42='The biggest change is on the pitch: matches now play the way you choose.',
  list42=['GAMEPLAY in OPTIONS: difficulty, a new dribbling, realistic or arcade set pieces and position traits, and one switch back to the 1996 game.',
          'Set-piece practice in your career: free kicks, penalties and corners, in attack or in defence.',
          'Serie D complete with all 162 clubs; the Serie C and Serie D groups drawn again every summer by geography.',
          'Every club in its real formation, the real line-ups of Serie A and Serie B, player prices from the real market value.',
          'The new Serie C Supercup, and the World 2026-27 in SEASON mode too.',
          'Keeper gloves, names written with the joystick, shirt numbers from the keypad, many fixes. Your 4.1 careers carry on in 4.2.'],
  over=dict(out_sub='SWOS Mod 4.2 · free', cur40='The 4.2 release on GitHub', news_title42="What's new in 4.2",
            road43="the computer clubs' transfer market, with each country's real transfer windows and loans; substitutions by the computer; goalkeeper skills; players' skills checked against real attributes; players' ages on screen; 50 kit colours instead of 10, our own catalogue drawn from real club colours; a database editor in the game: names, value and skills of any team, from the main menu (never during a career; a career started on an edited database is marked DATABASE MODIFICATO); a value editor for your custom teams.",
            road43_tag='Planned:'),
 ),
 'it': dict(
  nav='Gameplay', title='Gameplay: come si gioca con la mod',
  lead='La 4.2 cambia il modo in cui si gioca la partita, se lo vuoi tu: difficoltà, dribbling, calci piazzati e abilità per ruolo, '
       'ognuno con la sua scelta. E con un solo interruttore torni esattamente al gioco del 1996.',
  table=('Opzione', 'Valori', 'Installazione nuova'),
  preview='Anteprima.',
  end=('Scarica il patcher', 'Le novità della 4.2', 'Tutte le note della 4.2 su GitHub'),
  sec=[
   ('where', 'Dove: OPZIONI → GAMEPLAY', [
    ('p', 'Tutto sta in una riga del menu <strong>OPZIONI</strong> del gioco: <strong>GAMEPLAY</strong>. Ha due valori:'),
    ('ul', ["<strong>ORIGINALE</strong>: il gioco com'era nel 1996, esattamente. Ogni opzione di questa pagina vale come nel gioco originale, "
            'ma quello che avevi scelto non si perde: torni a PERSONALIZZATO e ritrovi le tue impostazioni come le avevi lasciate.',
            '<strong>PERSONALIZZATO</strong> (il valore di partenza): premi FUOCO e si apre la pagina <strong>GAMEPLAY PERSONALIZZATO</strong>, '
            'una riga per ogni opzione.']),
    ('p', 'Nella pagina SINISTRA / DESTRA cambiano il valore di una riga e FUOCO lo fa avanzare. <strong>PREDEFINITI</strong> rimette ogni riga '
          'al valore di partenza, <strong>INDIETRO</strong> esce dalla pagina. La carriera ricorda le tue scelte: una carriera salvata con ORIGINALE resta su ORIGINALE.'),
    ('table', None),
    ('p', "Le opzioni nuove partono tutte dal gioco originale (NORMALE, CLASSICO, CLASSICI, RUOLI DISATT.), quindi niente cambia finché non scegli tu. "
          'Se giocavi con la 4.1, GAMEPLAY parte su PERSONALIZZATO con le impostazioni che avevi già.'),
    ('frames', ['options', 'custom'])]),
   ('difficulty', "DIFFICOLTA': FACILE, NORMALE, DIFFICILE", [
    ('p', 'Quanto è forte il computer quando gioca contro di te. <strong>NORMALE</strong> è il gioco originale.'),
    ('ul', ['<strong>FACILE</strong>: i giocatori della squadra del computer valgono l\'80%, il portiere ha 2 punti in meno e i passaggi sbagliano più spesso.',
            '<strong>DIFFICILE</strong>: i giocatori sono migliori del 10%, il portiere ha 2 punti in più e i passaggi sono più precisi.']),
    ('p', 'Il livello cambia solo una squadra del computer che gioca contro di te. Due giocatori umani, computer contro computer, allenamenti, '
          "SWOS++ (l'aggiunta per la versione inglese) e risultati simulati (le partite che il gioco calcola senza giocarle) restano sempre il gioco originale.")]),
   ('dribbling', 'DRIBBLING: CLASSICO, NUOVO, PERSONALIZZATO', [
    ('p', 'Dribblare vuol dire saltare un avversario con la palla al piede. <strong>CLASSICO</strong> è il gioco originale; '
          '<strong>NUOVO</strong> è il nuovo dribbling della mod, pronto da giocare; con <strong>PERSONALIZZATO</strong> regoli tu ogni voce. Con NUOVO:'),
    ('ul', ['il tuo giocatore rallenta meno quando corre con la palla;',
            'nei cambi di direzione la palla resta più vicina al piede;',
            'appena conquistata la palla, la tieni un attimo in più prima che qualcuno possa riprendertela;',
            'il computer entra in scivolata meno spesso, e mai mentre dribbli dentro la sua area;',
            'il suo secondo uomo resta più indietro, invece di venirti addosso insieme al primo;',
            'dopo aver perso palla su un contrasto forte, il computer ci mette un attimo in più a riprenderla.']),
    ('p', "Per essere onesti: nella 4.2 i difensori del computer pressano e coprono di più (meno 'birilli' fermi mentre li salti), "
          'ma non entrano in contrasto più spesso.'),
    ('p', "Queste regolazioni valgono solo a palla in gioco: punizioni, calci d'angolo, rimesse laterali, rinvii dal fondo e calci d'inizio "
          "restano come nel gioco originale. Come la DIFFICOLTA', agiscono nelle tue partite contro il computer."),
    ('h3', 'La pagina DRIBBLING PERSONALIZZATO'),
    ('p', 'DRIBBLING su PERSONALIZZATO apre una pagina tutta sua. Una riga con un numero mostra un livello: 0 è il gioco originale, e più è alto, '
          "più aiuto hai (la legenda in basso: SINISTRA: CLASSICO, DESTRA: PIU' AIUTO). <strong>PREDEFINITI</strong> rimette i valori di NUOVO, "
          'per esempio VELOCITA CON PALLA 2 su 4 e PALLA INCOLLATA 4 su 10; <strong>INDIETRO</strong> torna alla pagina GAMEPLAY PERSONALIZZATO.'),
    ('ul', ['<strong>VELOCITA CON PALLA</strong>: quanto poco rallenta il tuo giocatore quando corre con la palla.',
            '<strong>PALLA INCOLLATA</strong>: quanto la palla resta vicina al piede nei cambi di direzione.',
            '<strong>PROTEZIONE PALLA</strong>: per quanto tieni la palla appena conquistata, prima che un avversario possa riprendertela.',
            '<strong>MENO SCIVOLATE CPU</strong>: i giocatori del computer partono in scivolata solo da più vicino, quindi meno spesso.',
            '<strong>MENO RADDOPPI CPU</strong>: quanto resta indietro il secondo uomo del computer, invece di venirti addosso insieme al primo.',
            '<strong>CPU LENTA A RIPRENDERE</strong>: quanto aspetta il computer prima di tornare sulla palla dopo averla persa su un contrasto forte.',
            '<strong>AREA SENZA SCIVOLATE</strong>: ATTIV., il computer non entra mai in scivolata mentre dribbli dentro la sua area, dove ogni fallo è rigore; '
            'DISATT., può farlo, come nel gioco originale. Con NUOVO è ATTIV.',
            '<strong>DIFENSORI CPU</strong>: come ti affrontano i difensori del computer. <strong>INSEGUONO</strong>: ti rincorrono, come nel gioco originale '
            '(il valore di NUOVO); <strong>ASPETTANO</strong>: restano tra te e la porta invece di rincorrerti da dietro; '
            '<strong>COPERTURA</strong> e <strong>UNO ALLA VOLTA</strong>: uno ti pressa e un compagno copre alle sue spalle.',
            '<strong>COSTRUZIONE CPU</strong>: ATTIV., la squadra del computer costruisce il gioco con più calma: il portiere cerca più spesso '
            'un compagno libero e, sotto pressione, calcia lungo meno spesso. DISATT., come nel gioco originale. Con NUOVO è ATTIV.']),
    ('frames', ['dribbling', 'match-dribbling'])]),
   ('setpieces', 'CALCI PIAZZATI: CLASSICI, REALISTICI, ARCADE', [
    ('p', "I calci piazzati sono le ripartenze a palla ferma: punizioni, calci d'angolo e simili. Tre valori, per ogni partita; "
          '<strong>CLASSICI</strong> è il gioco originale.'),
    ('p', '<strong>REALISTICI</strong>:'),
    ('ul', ['su angoli e cross i colpi di testa vanno verso il basso invece che sopra la traversa; chi è bravo di testa tiene la palla sotto la traversa anche da più lontano;',
            "i portieri non bloccano più tutto quello che cade nell'area piccola;",
            'il computer va più spesso sui palloni alti;',
            "le punizioni vicino all'area scendono dopo la barriera come quelle vere, e quante entrano dipende dal tiro di chi calcia, come nel calcio reale: "
            'uno specialista segna circa una volta su dieci, un tiratore medio una su quindici, uno scarso circa una su trenta. '
            'Quando la punizione del computer non va in porta, finisce sopra la traversa o sulla barriera.']),
    ('p', '<strong>ARCADE</strong>:'),
    ('ul', ['gli stessi colpi di testa e gli stessi portieri di REALISTICI;',
            "più punizioni attorno all'area: lì un contrasto pulito viene fischiato fallo una volta su tre;",
            'il computer tira le punizioni a giro sul secondo palo: un ottimo tiratore segna circa una su sei da 20-25 metri, uno scarso quasi mai.']),
    ('p', 'Le tue punizioni restano sempre nelle tue mani, direzione ed effetto, in ogni modalità.'),
    ('frames', ['match-setpieces'])]),
   ('roles', 'RUOLI: le abilità per ruolo', [
    ('p', "Un'abilità per ruolo è una cosa che un giocatore fa meglio grazie al suo ruolo. Con <strong>RUOLI</strong> su <strong>ATTIV.</strong> "
          '(alla partenza è DISATT., il gioco originale) le hanno tutte le squadre, anche quelle del computer. Il ruolo è quello naturale del giocatore, '
          'quello del file della squadra, non il posto in cui lo schieri in formazione. Idea di Marco.'),
    ('ul', ["<strong>Colpo di testa verso il basso nell'area avversaria</strong>: qualsiasi giocatore di movimento che colpisce di testa dentro l'area "
            "avversaria manda la palla verso il basso, tanto più quanto è bravo di testa. Il pallonetto di testa (leva indietro) e il colpo di testa da fermo "
            'non cambiano; in ogni altro punto i colpi di testa vanno in alto e lontano come nel gioco originale.',
            "<strong>Il cross teso delle ali</strong>: un'ala destra o sinistra (RW / LW) sulla fascia, nell'ultimo quarto di campo, con l'effetto 'indietro' "
            '(la leva mossa subito dopo il calcio) fa un cross basso e veloce in mezzo all\'area invece del pallone alto. Lo stesso da un calcio d\'angolo '
            "o da una punizione laterale battuti da un'ala, se il pallone va verso il centro. Le ali del computer giocano di rado questo pallone, "
            'quindi il cross teso è soprattutto tuo.',
            '<strong>I difensori centrali</strong> (D) arrivano un po\' più lontano sui palloni alti nella propria area, tanto più quanto sono bravi di testa.']),
    ('p', "Con CALCI PIAZZATI su REALISTICI o ARCADE tutti i colpi di testa vanno già verso il basso; con RUOLI attivi lo fanno solo quelli nell'area avversaria. "
          'Con RUOLI DISATT., GAMEPLAY ORIGINALE, SWOS++ e le partitelle di allenamento si gioca sempre il gioco originale; la prova dei calci piazzati '
          'usa le abilità come una partita.'),
    ('frames', ['match-roles'])]),
   ('cards', 'Cartellini e infortuni', [
    ('p', 'Nella pagina GAMEPLAY PERSONALIZZATO ci sono anche tre opzioni delle versioni precedenti della mod, ATTIV. alla partenza:'),
    ('ul', ['<strong>ROSSI ALLA CPU</strong>: i giocatori del computer vengono ammoniti ed espulsi come i tuoi. '
            'Nel gioco originale un giocatore del computer non veniva mai espulso e non prendeva mai il secondo giallo.',
            '<strong>INFORTUNI ALLA CPU</strong>: i giocatori del computer si infortunano come i tuoi.',
            '<strong>INFORTUNI PORTIERI</strong>: dopo ogni partita il portiere di ogni squadra ha una probabilità su 25 di infortunarsi '
            'e di restare fuori per una o due partite.']),
    ('p', 'DISATT., o GAMEPLAY su ORIGINALE, è il gioco originale.')]),
   ('practice', 'La prova dei calci piazzati', [
    ('p', 'In carriera, il pulsante <strong>ALLENAMENTO</strong> della schermata della rosa ora apre una pagina tutta sua, <strong>PRATICA</strong>:'),
    ('ul', ['<strong>ALLENAMENTO</strong>: la partitella di sempre;',
            "<strong>PROVA PUNIZIONI</strong>, <strong>PROVA RIGORI</strong>, <strong>PROVA CALCI D'ANGOLO</strong>: il calcio piazzato si ripete "
            'di continuo, con il pallone rimesso a posto ogni volta: punizioni dal centro e dai due lati a quattro distanze dalla porta, rigori, '
            "calci d'angolo da entrambi i lati. Niente cronometro, niente presentazione dello stadio, niente barra del risultato: solo i calci piazzati;",
            '<strong>GIOCA IN ATTACCO</strong> / <strong>GIOCA IN DIFESA</strong>: in attacco il calcio piazzato lo batte la tua squadra; '
            'in difesa lo batte il computer e tu difendi.']),
    ('p', "<strong>TIRI</strong> sceglie quanti tentativi: 5, 10, 20, 50 o INFINITI (all'inizio 10). <strong>META' CAMPO</strong> sceglie la porta: "
          'CASUALE (quella che ti dà la partita), ALTA, BASSA o ALTERNATA. Premi ESC quando vuoi. Poi una pagina mostra TIRI e GOL: '
          '<strong>OK</strong> ti riporta indietro, <strong>RIPROVA</strong> fa ripartire un\'altra serie della stessa prova.'),
    ('p', 'La prova non cambia mai la tua carriera più di quanto faccia già una partitella di allenamento. Con GAMEPLAY su ORIGINALE il titolo '
          'della pagina diventa PRATICA - GAMEPLAY: ORIGINALE e la prova usa i calci piazzati classici.'),
    ('frames', ['practice', 'practice-results'])]),
  ],
  h42='Disponibile: SWOS 96/97 Mod 4.2',
  p42='Il cambiamento più grande è in campo: la partita ora si gioca come scegli tu.',
  list42=['GAMEPLAY in OPZIONI: difficoltà, un nuovo dribbling, calci piazzati realistici o arcade e abilità per ruolo, e un solo interruttore per tornare al gioco del 1996.',
          "Prova dei calci piazzati in carriera: punizioni, rigori e calci d'angolo, in attacco o in difesa.",
          'La Serie D completa con tutte le 162 squadre; i gironi di Serie C e Serie D rifatti ogni estate per geografia.',
          'Ogni squadra con il suo modulo vero, le formazioni vere di Serie A e Serie B, i prezzi dei giocatori dal valore di mercato reale.',
          'La nuova Supercoppa Serie C, e il Mondo 2026-27 anche in modalità STAGIONE.',
          'I guanti dei portieri, i nomi scritti con il joystick, i numeri di maglia dal tastierino, molte correzioni. Le carriere della 4.1 continuano nella 4.2.'],
  over=dict(out_sub='SWOS Mod 4.2 · gratis', cur40='La release 4.2 su GitHub', news_title42='Le novità della 4.2',
            road43='il mercato delle squadre del computer, con le vere finestre di mercato di ogni paese e i prestiti; le sostituzioni del computer; le abilità dei portieri; le abilità dei giocatori ricontrollate sugli attributi reali; l\'età dei giocatori sullo schermo; 50 colori di maglia invece di 10, un catalogo tutto nostro preso dai colori veri dei club; un editor del database nel gioco: nomi, valore e abilità di qualsiasi squadra, dal menu principale (mai durante una carriera; una carriera iniziata su un database modificato è segnata DATABASE MODIFICATO); un editor del valore per le tue squadre personalizzate.',
            road43_tag='In programma:'),
 ),
 'fr': dict(
  nav='Gameplay', title='Gameplay : comment joue le mod',
  lead="La 4.2 change la façon dont se joue un match, si vous le voulez : difficulté, dribble, coups de pied arrêtés et aptitudes par poste, "
       "chacun avec son propre choix. Et un seul interrupteur vous rend exactement le jeu de 1996.",
  table=('Option', 'Valeurs', 'Nouvelle installation'),
  preview="Aperçu : l'écran italien remplace l'écran {L} en attendant sa capture.",
  end=('Télécharger le patcher', 'Les nouveautés de la 4.2', 'Toutes les notes de la 4.2 sur GitHub'),
  sec=[
   ('where', 'Où : OPTIONS → GAMEPLAY', [
    ('p', "Tout se trouve sur une ligne du menu <strong>OPTIONS</strong> du jeu : <strong>GAMEPLAY</strong>. Elle a deux valeurs :"),
    ('ul', ["<strong>ORIGINAL</strong> : le jeu tel qu'il était en 1996, exactement. Chaque option de cette page agit comme dans le jeu original, "
            "mais vos choix ne sont pas oubliés : revenez à PERSONNALISE et vous retrouvez vos réglages tels que vous les aviez laissés.",
            "<strong>PERSONNALISE</strong> (la valeur de départ) : appuyez sur FEU et la page <strong>GAMEPLAY PERSONNALISE</strong> s'ouvre, une ligne par option."]),
    ('p', "Sur cette page, GAUCHE / DROITE changent la valeur d'une ligne et FEU la fait passer à la suivante. <strong>PREDEFINIS</strong> remet chaque "
          "ligne à sa valeur de départ, <strong>QUITTER</strong> ferme la page. Une carrière garde ses choix : une carrière sauvegardée sur ORIGINAL reste sur ORIGINAL."),
    ('table', None),
    ('p', "Les nouvelles options partent toutes du jeu original (NORMAL, CLASSIQUE, CLASSIQUES, APTITUDES PAR POSTE DESACTIVE) : rien ne change tant que "
          "vous ne choisissez pas. Si vous jouiez avec la 4.1, GAMEPLAY part sur PERSONNALISE avec les réglages que vous aviez déjà."),
    ('frames', ['options', 'custom'])]),
   ('difficulty', 'DIFFICULTE : FACILE, NORMAL, DIFFICILE', [
    ('p', "La force de l'ordinateur quand il joue contre vous. <strong>NORMAL</strong> est le jeu original."),
    ('ul', ["<strong>FACILE</strong> : les joueurs de l'équipe de l'ordinateur valent 80 %, son gardien a 2 points de moins et ses passes se perdent plus souvent.",
            '<strong>DIFFICILE</strong> : ses joueurs sont meilleurs de 10 %, son gardien a 2 points de plus et ses passes sont plus précises.']),
    ('p', "Le niveau ne change qu'une équipe de l'ordinateur qui joue contre vous. Deux joueurs humains, ordinateur contre ordinateur, matchs d'entraînement, "
          "SWOS++ (le module pour la version anglaise) et résultats simulés (les matchs que le jeu calcule sans les jouer) restent toujours le jeu original.")]),
   ('dribbling', 'DRIBBLE : CLASSIQUE, NOUVEAU, PERSONNALISE', [
    ('p', "Dribbler, c'est passer un adversaire avec le ballon au pied. <strong>CLASSIQUE</strong> est le jeu original ; "
          "<strong>NOUVEAU</strong> est le nouveau dribble du mod, prêt à jouer ; <strong>PERSONNALISE</strong> vous laisse régler chaque élément vous-même. Avec NOUVEAU :"),
    ('ul', ['votre joueur ralentit moins quand il court avec le ballon ;',
            'dans les changements de direction, le ballon reste plus près de son pied ;',
            "après avoir gagné le ballon, vous le gardez un instant de plus avant qu'on puisse vous le reprendre ;",
            "l'ordinateur tacle moins souvent, et jamais pendant que vous dribblez dans sa propre surface de réparation ;",
            "son deuxième homme reste plus en retrait, au lieu de vous fondre dessus avec le premier ;",
            "après avoir perdu le ballon sur un tacle appuyé, l'ordinateur met un instant de plus à le reprendre."]),
    ('p', "Pour être honnêtes : dans la 4.2, les défenseurs de l'ordinateur pressent et couvrent davantage (moins de « quilles » immobiles pendant que vous "
          "les passez), mais ils ne taclent pas plus souvent."),
    ('p', "Ces réglages ne valent que ballon en jeu : coups francs, corners, touches, six mètres et coups d'envoi restent comme dans le jeu original. "
          "Comme la DIFFICULTE, ils agissent dans vos matchs contre l'ordinateur."),
    ('h3', 'La page DRIBBLE PERSONNALISE'),
    ('p', "DRIBBLE sur PERSONNALISE ouvre une page à part. Une ligne chiffrée montre un cran : 0 est le jeu original, et plus le cran est haut, "
          "plus vous êtes aidé (la légende en bas : GAUCHE: CLASSIQUE, DROITE: PLUS D'AIDE). <strong>PREDEFINIS</strong> remet les valeurs de NOUVEAU, "
          'par exemple VITESSE AVEC BALLON 2 sur 4 et BALLON COLLE AU PIED 4 sur 10 ; <strong>QUITTER</strong> revient à la page GAMEPLAY PERSONNALISE.'),
    ('ul', ['<strong>VITESSE AVEC BALLON</strong> : à quel point votre joueur ralentit peu quand il court avec le ballon.',
            '<strong>BALLON COLLE AU PIED</strong> : à quel point le ballon reste près du pied dans les changements de direction.',
            "<strong>PROTECTION DU BALLON</strong> : combien de temps vous gardez le ballon après l'avoir gagné, avant qu'un adversaire puisse le reprendre.",
            "<strong>MOINS DE TACLES CPU</strong> : les joueurs de l'ordinateur ne partent en tacle glissé que de plus près, donc moins souvent.",
            "<strong>MOINS PRISES A DEUX CPU</strong> : à quel point le deuxième homme de l'ordinateur reste en retrait, au lieu de vous fondre dessus avec le premier.",
            "<strong>CPU LENTE A RECUPERER</strong> : combien de temps l'ordinateur attend avant de revenir sur le ballon après l'avoir perdu sur un tacle appuyé.",
            "<strong>SURFACE SANS TACLES</strong> : ACTIVE, l'ordinateur ne tacle jamais pendant que vous dribblez dans sa surface, où chaque faute est un penalty ; "
            'DESACTIVE, il peut le faire, comme dans le jeu original. ACTIVE avec NOUVEAU.',
            "<strong>DEFENSEURS CPU</strong> : comment les défenseurs de l'ordinateur vous affrontent. <strong>POURSUIVENT</strong> : ils vous courent après, "
            "comme dans le jeu original (la valeur de NOUVEAU) ; <strong>ATTENDENT</strong> : ils restent entre vous et le but au lieu de vous poursuivre "
            "par derrière ; <strong>COUVERTURE</strong> et <strong>UN PAR UN</strong> : un joueur vous presse et un coéquipier couvre derrière lui.",
            "<strong>CONSTRUCTION CPU</strong> : ACTIVE, l'équipe de l'ordinateur construit son jeu plus calmement : son gardien cherche plus souvent "
            'un coéquipier libre et, sous pression, elle dégage long moins souvent. DESACTIVE, comme dans le jeu original. ACTIVE avec NOUVEAU.']),
    ('frames', ['dribbling', 'match-dribbling'])]),
   ('setpieces', 'COUPS DE PIED ARRETES : CLASSIQUES, REALISTES, ARCADE', [
    ('p', "Les coups de pied arrêtés sont les remises en jeu ballon arrêté : coups francs, corners et autres. Trois valeurs, pour chaque match ; "
          '<strong>CLASSIQUES</strong> est le jeu original.'),
    ('p', '<strong>REALISTES</strong> :'),
    ('ul', ["sur corners et centres, les têtes partent vers le bas au lieu de passer au-dessus de la barre ; un bon joueur de tête garde le ballon sous la barre même de plus loin ;",
            'les gardiens ne captent plus tout ce qui tombe dans la surface de but ;',
            "l'ordinateur va plus souvent sur les ballons aériens ;",
            "les coups francs près de la surface retombent après le mur comme les vrais, et leur réussite dépend de la frappe du tireur, comme dans le vrai football : "
            "un grand spécialiste marque environ une fois sur dix, un tireur moyen une sur quinze, un tireur faible environ une sur trente. "
            "Quand le coup franc de l'ordinateur rate, il passe au-dessus de la barre ou finit dans le mur."]),
    ('p', '<strong>ARCADE</strong> :'),
    ('ul', ['les mêmes têtes et les mêmes gardiens que REALISTES ;',
            'plus de coups francs autour de la surface : là, un tacle propre est sifflé faute une fois sur trois ;',
            "l'ordinateur enroule ses coups francs vers le second poteau : un excellent tireur marque environ une fois sur six à 20-25 mètres, un tireur faible presque jamais."]),
    ('p', 'Vos propres coups francs restent entre vos mains, direction et effet, dans tous les modes.'),
    ('frames', ['match-setpieces'])]),
   ('roles', 'APTITUDES PAR POSTE', [
    ('p', "Une aptitude par poste, c'est ce qu'un joueur fait mieux grâce à son poste. Avec <strong>APTITUDES PAR POSTE</strong> sur <strong>ACTIVE</strong> "
          "(au départ DESACTIVE, le jeu original), toutes les équipes en ont, celles de l'ordinateur aussi. Le poste est le poste naturel du joueur, "
          "celui du fichier de l'équipe, pas la place où vous le mettez dans la composition. Une idée de Marco."),
    ('ul', ["<strong>Têtes vers le bas dans la surface adverse</strong> : tout joueur de champ qui reprend de la tête dans la surface de réparation adverse "
            "envoie le ballon vers le bas, d'autant plus qu'il est bon de la tête. La tête lobée (manette tirée en arrière) et la tête à l'arrêt ne changent pas ; "
            'partout ailleurs, les têtes partent haut et loin comme dans le jeu original.',
            "<strong>Le centre tendu des ailiers</strong> : un ailier droit ou gauche (RW / LW) sur le côté, dans le dernier quart du terrain, joue avec "
            "l'effet « arrière » (la manette bougée juste après la frappe) un centre bas et rapide dans la surface au lieu du ballon haut. De même sur un corner "
            "ou un coup franc excentré tiré par un ailier, quand le ballon va vers le centre. Les ailiers de l'ordinateur jouent rarement ce ballon : "
            "le centre tendu est surtout pour vous.",
            "<strong>Les défenseurs centraux</strong> (D) vont chercher les ballons aériens un peu plus loin dans leur propre surface, d'autant plus qu'ils sont bons de la tête."]),
    ('p', "Avec COUPS DE PIED ARRETES sur REALISTES ou ARCADE, toutes les têtes partent déjà vers le bas ; avec les aptitudes actives, seules celles dans la "
          "surface adverse le font. APTITUDES PAR POSTE DESACTIVE, GAMEPLAY ORIGINAL, SWOS++ et les matchs d'entraînement jouent toujours le jeu original ; "
          "l'entraînement aux coups de pied arrêtés utilise les aptitudes comme un match."),
    ('frames', ['match-roles'])]),
   ('cards', 'Cartons et blessures', [
    ('p', 'La page GAMEPLAY PERSONNALISE contient aussi trois options de versions précédentes du mod, ACTIVE au départ :'),
    ('ul', ["<strong>CARTONS ROUGES CPU</strong> : les joueurs de l'ordinateur sont avertis et expulsés comme les vôtres. "
            "Dans le jeu original, un joueur de l'ordinateur n'était jamais expulsé et ne recevait jamais de second carton jaune.",
            "<strong>BLESSURES CPU</strong> : les joueurs de l'ordinateur se blessent comme les vôtres.",
            "<strong>BLESSURES DES GARDIENS</strong> : après chaque match, le gardien de chaque équipe a une chance sur 25 de se blesser "
            'et de manquer un ou deux matchs.']),
    ('p', 'DESACTIVE, ou GAMEPLAY sur ORIGINAL, est le jeu original.')]),
   ('practice', "L'entraînement aux coups de pied arrêtés", [
    ('p', "En carrière, le bouton d'entraînement de l'écran de l'effectif ouvre maintenant une page à part, <strong>ENTRAINEMENT</strong> :"),
    ('ul', ["<strong>MATCH D'ENTRAINEMENT</strong> : le match d'entraînement, comme avant ;",
            '<strong>COUPS FRANCS</strong>, <strong>PENALTYS</strong>, <strong>CORNERS</strong> : le coup de pied arrêté revient encore et encore, '
            'le ballon replacé pour vous à chaque fois : coups francs du centre et des deux côtés à quatre distances du but, penaltys, corners des deux côtés. '
            "Pas de chronomètre, pas de présentation du stade, pas de bandeau du score : rien que les coups de pied arrêtés ;",
            "<strong>JOUER EN ATTAQUE</strong> / <strong>JOUER EN DEFENSE</strong> : en attaque, votre équipe tire le coup de pied arrêté ; "
            "en défense, c'est l'ordinateur qui le tire et vous défendez."]),
    ('p', "<strong>TIRS</strong> fixe le nombre de tentatives : 5, 10, 20, 50 ou ILLIMITES (10 au départ). <strong>MOITIE</strong> choisit le but : "
          "ALEATOIRE (celui que le match vous donne), HAUTE, BASSE ou ALTERNEE. Appuyez sur ESC quand vous voulez. Une page montre ensuite TIRS et BUTS : "
          "<strong>OK</strong> vous ramène en arrière, <strong>REJOUER</strong> lance une autre série du même entraînement."),
    ('p', "Un entraînement ne change jamais votre carrière plus qu'un match d'entraînement. Avec GAMEPLAY sur ORIGINAL, le titre de la page devient "
          "ENTRAINEMENT - GAMEPLAY: ORIGINAL et l'entraînement joue les coups de pied arrêtés classiques."),
    ('frames', ['practice', 'practice-results'])]),
  ],
  h42='Disponible : SWOS 96/97 Mod 4.2',
  p42='Le plus grand changement est sur le terrain : les matchs se jouent désormais comme vous le choisissez.',
  list42=["GAMEPLAY dans OPTIONS : difficulté, un nouveau dribble, des coups de pied arrêtés réalistes ou arcade et des aptitudes par poste, et un seul interrupteur pour revenir au jeu de 1996.",
          "L'entraînement aux coups de pied arrêtés en carrière : coups francs, penaltys et corners, en attaque ou en défense.",
          'La Serie D complète avec ses 162 clubs ; les groupes de Serie C et de Serie D retirés chaque été selon la géographie.',
          'Chaque club dans sa vraie formation, les vraies compositions de Serie A et de Serie B, le prix des joueurs selon leur vraie valeur marchande.',
          'La nouvelle Supercoupe de Serie C, et le Monde 2026-27 aussi en mode SAISON.',
          "Des gants pour les gardiens, les noms écrits au joystick, les numéros de maillot au pavé numérique, de nombreuses corrections. Vos carrières 4.1 continuent dans la 4.2."],
  over=dict(out_sub='SWOS Mod 4.2 · gratuit', cur40='La version 4.2 sur GitHub', news_title42='Les nouveautés de la 4.2',
            road43="le marché des transferts des clubs de l'ordinateur, avec les vraies fenêtres de transferts de chaque pays et les prêts ; les remplacements de l'ordinateur ; les qualités des gardiens ; les qualités des joueurs revues sur leurs vrais attributs ; l'âge des joueurs à l'écran ; 50 couleurs de maillot au lieu de 10, notre propre catalogue tiré des vraies couleurs des clubs ; un éditeur de base de données dans le jeu : noms, valeur et qualités de n'importe quelle équipe, depuis le menu principal (jamais pendant une carrière ; une carrière commencée sur une base modifiée est marquée DATABASE MODIFICATO) ; un éditeur de valeur pour vos équipes personnalisées.",
            road43_tag='Prévu :'),
 ),
 'de': dict(
  nav='Spielweise', title='Spielweise: so spielt sich die Mod',
  lead='Version 4.2 ändert, wie sich ein Spiel spielt, wenn du es willst: Schwierigkeit, Dribbling, Standardsituationen und Spielertypen, '
       'jedes mit einer eigenen Wahl. Und ein einziger Schalter gibt dir genau das Spiel von 1996 zurück.',
  table=('Option', 'Werte', 'Neue Installation'),
  preview='Vorschau: der italienische Bildschirm steht hier, bis der {L} aufgenommen ist.',
  end=('Patcher herunterladen', 'Das Neue in 4.2', 'Alle Notizen zu 4.2 auf GitHub'),
  sec=[
   ('where', 'Wo: OPTIONEN → SPIELWEISE', [
    ('p', 'Alles steckt in einer Zeile des Spielmenüs <strong>OPTIONEN</strong>: <strong>SPIELWEISE</strong>. Sie hat zwei Werte:'),
    ('ul', ['<strong>ORIGINAL</strong>: das Spiel genau so wie 1996. Jede Option dieser Seite wirkt wie im Originalspiel, '
            'aber deine Wahl geht nicht verloren: Zurück auf INDIVIDUELL findest du deine Einstellungen so, wie du sie gelassen hast.',
            '<strong>INDIVIDUELL</strong> (der Startwert): Drück FEUER darauf, und die Seite <strong>SPIELWEISE INDIVIDUELL</strong> öffnet sich, eine Zeile pro Option.']),
    ('p', 'Auf dieser Seite ändern LINKS / RECHTS den Wert einer Zeile, FEUER schaltet zum nächsten. <strong>STANDARD</strong> setzt jede Zeile auf '
          'ihren Startwert zurück, <strong>ENDE</strong> verlässt die Seite. Eine Karriere merkt sich ihre Wahl: Eine auf ORIGINAL gespeicherte Karriere bleibt auf ORIGINAL.'),
    ('table', None),
    ('p', 'Die neuen Optionen starten alle beim Originalspiel (NORMAL, KLASSISCH, KLASSISCH, SPIELERTYPEN AUS): Nichts ändert sich, bis du wählst. '
          'Hast du mit 4.1 gespielt, startet SPIELWEISE auf INDIVIDUELL mit den Einstellungen, die du schon hattest.'),
    ('frames', ['options', 'custom'])]),
   ('difficulty', 'SCHWIERIGKEIT: LEICHT, NORMAL, SCHWER', [
    ('p', 'Wie stark der Computer ist, wenn er gegen dich spielt. <strong>NORMAL</strong> ist das Originalspiel.'),
    ('ul', ['<strong>LEICHT</strong>: Die Spieler der Computermannschaft sind 80 % so gut, ihr Torwart ist 2 Punkte schwächer und ihre Pässe gehen öfter daneben.',
            '<strong>SCHWER</strong>: Ihre Spieler sind 10 % besser, ihr Torwart ist 2 Punkte stärker und ihre Pässe sind genauer.']),
    ('p', 'Die Stufe ändert nur eine Computermannschaft, die gegen dich spielt. Zwei menschliche Spieler, Computer gegen Computer, Trainingsspiele, '
          'SWOS++ (die Erweiterung für die englische Version) und simulierte Ergebnisse (Spiele, die das Spiel berechnet, ohne sie zu spielen) bleiben immer das Originalspiel.')]),
   ('dribbling', 'DRIBBLING: KLASSISCH, NEU, INDIVIDUELL', [
    ('p', 'Dribbeln heißt, mit dem Ball am Fuß an einem Gegner vorbeizugehen. <strong>KLASSISCH</strong> ist das Originalspiel; '
          '<strong>NEU</strong> ist das neue Dribbling der Mod, fertig zum Spielen; mit <strong>INDIVIDUELL</strong> stellst du jeden Teil selbst ein. Mit NEU:'),
    ('ul', ['wird dein Spieler mit dem Ball weniger langsam;',
            'bleibt der Ball bei scharfen Richtungswechseln näher am Fuß;',
            'behältst du den Ball nach dem Erobern einen Moment länger, bevor ihn dir jemand abnehmen kann;',
            'grätscht der Computer seltener, und nie, während du in seinem eigenen Strafraum dribbelst;',
            'bleibt sein zweiter Mann weiter zurück, statt dich zusammen mit dem ersten anzugehen;',
            'braucht der Computer nach einem Ballverlust durch ein hartes Tackling einen Moment länger, um ihn zurückzuholen.']),
    ('p', "Ehrlich gesagt: In 4.2 pressen und sichern die Verteidiger des Computers mehr ab (weniger 'Slalomstangen', die stillstehen, während du an ihnen "
          'vorbeigehst), aber sie gehen nicht öfter ins Tackling.'),
    ('p', 'Diese Einstellungen gelten nur bei laufendem Ball: Freistöße, Ecken, Einwürfe, Abstöße und Anstöße bleiben wie im Originalspiel. '
          'Wie die SCHWIERIGKEIT wirken sie in deinen Spielen gegen den Computer.'),
    ('h3', 'Die Seite DRIBBLING INDIVIDUELL'),
    ('p', 'DRIBBLING auf INDIVIDUELL öffnet eine eigene Seite. Eine Zahlenzeile zeigt eine Stufe: 0 ist das Originalspiel, und je höher die Stufe, '
          'desto mehr Hilfe bekommst du (die Legende unten: LINKS: KLASSISCH, RECHTS: MEHR HILFE). <strong>STANDARD</strong> stellt die Werte von NEU wieder her, '
          'zum Beispiel TEMPO AM BALL 2 von 4 und ENGE BALLFUEHRUNG 4 von 10; <strong>ENDE</strong> führt zurück zur Seite SPIELWEISE INDIVIDUELL.'),
    ('ul', ['<strong>TEMPO AM BALL</strong>: wie wenig dein Spieler langsamer wird, wenn er mit dem Ball läuft.',
            '<strong>ENGE BALLFUEHRUNG</strong>: wie nah der Ball bei scharfen Richtungswechseln am Fuß bleibt.',
            '<strong>BALL ABSCHIRMEN</strong>: wie lange du den Ball nach dem Erobern behältst, bevor ein Gegner ihn zurückholen kann.',
            '<strong>WENIGER CPU GRAETSCHEN</strong>: Die Spieler des Computers grätschen erst aus kürzerer Entfernung, also seltener.',
            '<strong>WENIGER DOPPELN CPU</strong>: wie weit der zweite Mann des Computers zurückbleibt, statt dich zusammen mit dem ersten anzugehen.',
            '<strong>CPU WARTET LAENGER</strong>: wie lange der Computer wartet, bevor er nach einem Ballverlust durch ein hartes Tackling wieder zum Ball geht.',
            '<strong>STRAFRAUM OHNE GRAETSCHE</strong>: EIN, der Computer grätscht nie, während du in seinem Strafraum dribbelst, wo jedes Foul ein Elfmeter ist; '
            'AUS, er kann es, wie im Originalspiel. Mit NEU auf EIN.',
            '<strong>CPU VERTEIDIGER</strong>: wie dich die Verteidiger des Computers angehen. <strong>JAGEN</strong>: Sie laufen dir nach, wie im Originalspiel '
            '(der Wert von NEU); <strong>WARTEN</strong>: Sie bleiben zwischen dir und dem Tor, statt dich von hinten zu jagen; '
            '<strong>DECKEN</strong> und <strong>EINZELN</strong>: Einer presst dich, ein Mitspieler sichert hinter ihm ab.',
            '<strong>CPU AUFBAU</strong>: EIN, die Computermannschaft baut ruhiger auf: Ihr Torwart sucht öfter einen freien Mitspieler, '
            'und unter Druck schlägt sie den Ball seltener lang. AUS, wie im Originalspiel. Mit NEU auf EIN.']),
    ('frames', ['dribbling', 'match-dribbling'])]),
   ('setpieces', 'STANDARDSITUATIONEN: KLASSISCH, REALISTISCH, ARCADE', [
    ('p', 'Standardsituationen sind die Spielfortsetzungen mit ruhendem Ball: Freistöße, Ecken und Ähnliches. Drei Werte, für jedes Spiel; '
          '<strong>KLASSISCH</strong> ist das Originalspiel.'),
    ('p', '<strong>REALISTISCH</strong>:'),
    ('ul', ['Kopfbälle nach Ecken und Flanken gehen nach unten statt über die Latte; ein guter Kopfballspieler hält den Ball auch aus größerer Entfernung unter der Latte;',
            'Torhüter fangen nicht mehr alles, was in den Fünfmeterraum fällt;',
            'der Computer geht öfter zu hohen Bällen;',
            'Freistöße nahe am Strafraum senken sich hinter der Mauer wie echte, und wie oft sie drin sind, hängt vom Schuss des Schützen ab, wie im echten Fußball: '
            'ein Top-Spezialist trifft etwa einmal in zehn Versuchen, ein durchschnittlicher Schütze einmal in fünfzehn, ein schwacher etwa einmal in dreißig. '
            'Geht der Freistoß des Computers nicht hinein, fliegt er über die Latte oder in die Mauer.']),
    ('p', '<strong>ARCADE</strong>:'),
    ('ul', ['dieselben Kopfbälle und Torhüter wie bei REALISTISCH;',
            'mehr Freistöße rund um den Strafraum: Dort wird ein sauberes Tackling in einem von drei Fällen als Foul gepfiffen;',
            'der Computer zirkelt seine Freistöße an den langen Pfosten: Ein sehr guter Schütze trifft aus 20-25 Metern etwa einmal in sechs Versuchen, ein schwacher fast nie.']),
    ('p', 'Deine eigenen Freistöße bleiben in deiner Hand, Richtung und Effet, in jedem Modus.'),
    ('frames', ['match-setpieces'])]),
   ('roles', 'SPIELERTYPEN', [
    ('p', 'Ein Spielertyp ist etwas, das ein Spieler wegen seiner Position besser kann. Mit <strong>SPIELERTYPEN</strong> auf <strong>EIN</strong> '
          '(am Anfang AUS, das Originalspiel) haben ihn alle Mannschaften, auch die des Computers. Die Position ist die natürliche des Spielers, '
          'die aus der Mannschaftsdatei, nicht der Platz, auf den du ihn in der Aufstellung stellst. Eine Idee von Marco.'),
    ('ul', ['<strong>Kopfbälle nach unten im gegnerischen Strafraum</strong>: Jeder Feldspieler, der im gegnerischen Strafraum köpft, bringt den Ball nach unten, '
            'umso mehr, je besser er köpft. Der Kopfball-Lupfer (Stick nach hinten) und der Kopfball im Stand ändern sich nicht; '
            'überall sonst gehen Kopfbälle hoch und weit wie im Originalspiel.',
            "<strong>Die scharfe Flanke der Flügelspieler</strong>: Ein rechter oder linker Flügelspieler (RW / LW) außen im letzten Viertel des Spielfelds "
            "spielt mit dem Effet 'zurück' (der Stick direkt nach dem Schuss bewegt) eine flache, schnelle Flanke in den Strafraum statt des hohen Balls. "
            'Ebenso bei einer Ecke oder einem Freistoß von außen durch einen Flügelspieler, wenn der Ball zur Mitte geht. '
            'Die Flügelspieler des Computers spielen diesen Ball selten, die scharfe Flanke gehört also vor allem dir.',
            '<strong>Innenverteidiger</strong> (D) erreichen hohe Bälle im eigenen Strafraum etwas weiter, umso mehr, je besser sie köpfen.']),
    ('p', 'Mit STANDARDSITUATIONEN auf REALISTISCH oder ARCADE gehen schon alle Kopfbälle nach unten; mit SPIELERTYPEN auf EIN nur die im gegnerischen Strafraum. '
          'SPIELERTYPEN AUS, SPIELWEISE ORIGINAL, SWOS++ und Trainingsspiele spielen immer das Originalspiel; das Standardtraining nutzt die Spielertypen wie ein Spiel.'),
    ('frames', ['match-roles'])]),
   ('cards', 'Karten und Verletzungen', [
    ('p', 'Auf der Seite SPIELWEISE INDIVIDUELL stehen auch drei Optionen aus früheren Versionen der Mod, am Anfang auf EIN:'),
    ('ul', ['<strong>ROTE KARTEN CPU</strong>: Die Spieler des Computers werden verwarnt und vom Platz gestellt wie deine. '
            'Im Originalspiel flog ein Computerspieler nie vom Platz und bekam nie eine zweite Gelbe Karte.',
            '<strong>VERLETZUNGEN CPU</strong>: Die Spieler des Computers verletzen sich wie deine.',
            '<strong>TORWARTVERLETZUNGEN</strong>: Nach jedem Spiel verletzt sich der Torwart jeder Mannschaft mit einer Chance von 1 zu 25 '
            'und fällt ein oder zwei Spiele aus.']),
    ('p', 'AUS, oder SPIELWEISE auf ORIGINAL, ist das Originalspiel.')]),
   ('practice', 'Das Standardtraining', [
    ('p', 'In der Karriere öffnet die Schaltfläche <strong>TRAINING</strong> auf deinem Kaderbildschirm jetzt eine eigene Seite:'),
    ('ul', ['<strong>TRAININGSSPIEL</strong>: das Trainingsspiel wie bisher;',
            '<strong>FREISTOESSE</strong>, <strong>ELFMETER</strong>, <strong>ECKBAELLE</strong>: Die Standardsituation kommt wieder und wieder, '
            'der Ball jedes Mal für dich hingelegt: Freistöße aus der Mitte und von beiden Seiten in vier Entfernungen vom Tor, Elfmeter, Ecken von beiden Seiten. '
            'Keine Spieluhr, keine Stadionvorstellung, keine Ergebnisleiste: nur die Standardsituationen;',
            '<strong>IM ANGRIFF SPIELEN</strong> / <strong>IN DER ABWEHR SPIELEN</strong>: Im Angriff führt deine Mannschaft die Standardsituation aus; '
            'in der Abwehr führt sie der Computer aus und du verteidigst.']),
    ('p', '<strong>SCHUESSE</strong> legt die Zahl der Versuche fest: 5, 10, 20, 50 oder ENDLOS (am Anfang 10). <strong>HAELFTE</strong> wählt das Tor: '
          'ZUFALL (das, das dir das Spiel gibt), OBEN, UNTEN oder WECHSELND. Drück ESC, wann du willst. Danach zeigt eine Seite SCHUESSE und TORE: '
          '<strong>OK</strong> bringt dich zurück, <strong>NOCHMAL</strong> startet eine weitere Serie desselben Trainings.'),
    ('p', 'Ein Standardtraining verändert deine Karriere nie mehr als ein Trainingsspiel. Mit SPIELWEISE auf ORIGINAL lautet der Seitentitel '
          'TRAINING - SPIELWEISE: ORIGINAL und das Training spielt die klassischen Standardsituationen.'),
    ('frames', ['practice', 'practice-results'])]),
  ],
  h42='Jetzt verfügbar: SWOS 96/97 Mod 4.2',
  p42='Die größte Änderung ist auf dem Platz: Spiele spielen sich jetzt so, wie du es wählst.',
  list42=['SPIELWEISE in OPTIONEN: Schwierigkeit, ein neues Dribbling, realistische oder Arcade-Standardsituationen und Spielertypen, und ein Schalter zurück zum Spiel von 1996.',
          'Standardtraining in der Karriere: Freistöße, Elfmeter und Ecken, im Angriff oder in der Abwehr.',
          'Die Serie D komplett mit allen 162 Vereinen; die Gruppen der Serie C und Serie D jeden Sommer nach Geografie neu eingeteilt.',
          'Jeder Verein in seiner echten Formation, die echten Aufstellungen der Serie A und Serie B, Spielerpreise nach dem echten Marktwert.',
          'Der neue Supercup der Serie C, und die Welt 2026-27 auch im Modus SAISON.',
          'Torwarthandschuhe, Namen mit dem Joystick schreiben, Rückennummern über den Ziffernblock, viele Korrekturen. Deine Karrieren aus 4.1 laufen in 4.2 weiter.'],
  over=dict(out_sub='SWOS Mod 4.2 · kostenlos', cur40='Die Version 4.2 auf GitHub', news_title42='Das Neue in 4.2',
            road43='der Transfermarkt der Computer-Vereine, mit den echten Transferfenstern jedes Landes und Leihgeschäften; Auswechslungen durch den Computer; Torwartfähigkeiten; die Fähigkeiten der Spieler an echten Attributen überprüft; das Alter der Spieler auf dem Bildschirm; 50 Trikotfarben statt 10, ein eigener Katalog nach den echten Vereinsfarben; ein Datenbank-Editor im Spiel: Namen, Wert und Fähigkeiten jeder Mannschaft, aus dem Hauptmenü (nie während einer Karriere; eine Karriere auf einer geänderten Datenbank wird als DATABASE MODIFICATO markiert); ein Wert-Editor für deine eigenen Mannschaften.',
            road43_tag='Geplant:'),
 ),
}

LANG_IN = {'en': 'English', 'fr': 'français', 'de': 'deutsche'}   # (the preview note's {L})
