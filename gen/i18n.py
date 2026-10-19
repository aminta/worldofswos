"""Site texts in the four languages of SWOS 96/97 (IT, EN, FR, DE). FR and DE are translated from the English.

Game names (menus, countries, competitions) are written as the game spells them in each language: the in-game menu
names come from the mod's tools (mkseason.py CAREERS_NAMES / SEASONS_NAMES, historic.py NAMES).
"""

LANGS = ['en', 'it', 'fr', 'de']
LANG_NAME = {'en': 'English', 'it': 'Italiano', 'fr': 'Français', 'de': 'Deutsch'}
LOCALE = {'en': 'en_GB', 'it': 'it_IT', 'fr': 'fr_FR', 'de': 'de_DE'}

# in-game names (the mod's own menu strings)
GAME = {
    'careers': {'en': 'CLASSIC CAREERS', 'it': 'CARR. STORICHE', 'fr': "CARR. D'ANTAN", 'de': 'KLASS. KARRIERE'},
    'seasons': {'en': 'CLASSIC SEASONS', 'it': 'STAG. STORICHE', 'fr': "SAISONS D'ANTAN", 'de': 'SAISONKLASSIKER'},
    'tourneys': {'en': 'CLASSIC TOURNEYS', 'it': 'TORNEI STORICI', 'fr': 'TOURNOIS ANCIENS', 'de': 'TURNIERKLASSIKER'},
    # confirmed from the REL40rc1 exes (session 4.0, 2026-10-19)
    'e84': {'en': 'EUROPE 1984-85: First Division', 'it': 'EUROPA 1984-85: First Division',
            'fr': 'EUROPE 1984-85 : First Division', 'de': 'EUROPA 1984-85: First Division'},
    'world': {'en': 'WORLD 2026-27', 'it': 'MONDO 2026-27', 'fr': 'MONDE 2026-27', 'de': 'WELT 2026-27'},
}

CONTINENT = {
    'europe': {'en': 'Europe', 'it': 'Europa', 'fr': 'Europe', 'de': 'Europa'},
    'north_america': {'en': 'North and Central America', 'it': 'Nord e Centro America',
                      'fr': 'Amérique du Nord et centrale', 'de': 'Nord- und Mittelamerika'},
    'south_america': {'en': 'South America', 'it': 'Sud America', 'fr': 'Amérique du Sud', 'de': 'Südamerika'},
    'asia': {'en': 'Asia', 'it': 'Asia', 'fr': 'Asie', 'de': 'Asien'},
    'oceania': {'en': 'Oceania', 'it': 'Oceania', 'fr': 'Océanie', 'de': 'Ozeanien'},
    'africa': {'en': 'Africa', 'it': 'Africa', 'fr': 'Afrique', 'de': 'Afrika'},
}

T = {
 'en': dict(
    next41='In 4.1: the 2026 World Cup and Euro 2024 among the classic tourneys, with the real squads and the real formats (48 teams with the best third-placed; 24 teams).',
    h_next='Coming next',
    next_text='In 4.2: the national teams of the World 2026-27, complete and exact. Real squads, call-ups from the clubs of the world and job offers as national team coach; the 2030 World Cup with 48 teams and Euro 2028 with 24; the real qualifiers of every confederation; the Nations League.',
    next_note='A plan, not a date.',
    soon='Coming soon', soon_dl='The 4.0 patcher: by the end of October 2026',
    soon_install='Version 4.0, with the World 2026-27, is coming soon: the patcher will be on this page on release day. These are the steps you will follow.',
    visits='Visits',
    frames=['CLASSIC CAREERS: the historic worlds', 'WORLD 2026-27: the countries of Europe',
            'Serie A mid-season, with its zones', 'The Champions League table of 36 after 4 matchdays'],
    h_shots='Screens from the game',
    shots=[('Italian football', [('serie-a-table-it', 'Serie A mid-season, with its zones: Champions League, Europa League, Conference League, relegation'),
                                 ('serie-b-table-it', 'Serie B: promotion, play-off, play-out and relegation')]),
           ('Serie D, the real one', [('serie-d-table-it', 'A Serie D group of 2026-27, with its zones')]),
           ('English football', [('premier-table-it', 'The Premier League table with its zones'),
                                 ('premier-format-it', 'The FORMAT page of the Premier League')]),
           ("Brazil's state championships", [('brazil-state-table-it', 'The Campeonato Paulista 2026 after 7 matchdays, with its zones'),
                                             ('brazil-state-format-it', 'Its FORMAT page'),
                                             ('brazil-state-knockout-it', 'The Paulista final, first leg: São Paulo v Palmeiras')]),
           ('Argentina 2026', [('argentina-zone-it', 'The Liga Profesional: a zone of 15 in the Apertura'),
                               ('argentina-promedio-it', 'Relegation by promedio and the annual table')]),
           ('Major League Soccer 2026', [('mls-table-it', 'The Eastern and Western Conference tables'),
                                         ('mls-playoffs-it', 'The MLS Cup Playoffs')]),
           ('Mid-season splits', [('split-scotland-it', 'Scotland: top six and bottom six after 33 matchdays'),
                                  ('split-austria-it', 'Austria: the Meistergruppe after 22 matchdays')]),
           ('UEFA Champions League: the league phase', [('cl-league-phase-it', 'The table of 36 after 4 matchdays'),
                                                        ('cl-format-it', 'The FORMAT page of the league phase')])],
    testers_p='<strong>Marco</strong> (purple kits, menu music with SWOS++), <strong>Daniele</strong> (the season-end crash with a weak club). Thank you!',
    site='World of SWOS', sub='SWOS 96/97 Mod',
    skip='Skip to content', menu='Menu', lang_label='Language',
    nav_home='Home', nav_world='World 2026-27', nav_countries='Countries', nav_classic='Classic careers',
    nav_install='Install', nav_credits='Credits',
    meta_home='SWOS 96/97 Mod 4.0: the World 2026-27 career for Sensible World of Soccer 96/97. 91 countries, real '
              'squads and every competition in its real format. Free, unofficial fan mod.',
    kicker='SWOS 96/97 Mod 4.0 · World 2026-27',
    tagline='Football competitions, global and local, that no other game has, has ever had, or probably ever will.',
    concept='The same great SWOS as ever and, at the same time, a completely new game.',
    lead='A free fan mod for Sensible World of Soccer 96/97 (DOS, CD or GOG): today\'s football as it really is, '
         'league by league and cup by cup, in a career that spans the whole world, and the 1996-97 game as it '
         'really was.',
    dl='Download the patcher', dl_small='free · runs in your browser',
    how='How to install', see_world='Explore the world',
    s_countries='countries', s_clubs='clubs', s_divisions='league divisions', s_cups='national cups',
    s_lcups='league cups',
    h_what='What the mod is',
    what=['SWOS 96/97 Mod patches your own copy of <em>Sensible World of Soccer 96/97</em>, the game we have played '
          'for thirty years, in all four of its languages: Italian, English, French and German.',
          'Nothing of the game you love is lost: same pitch, same players running, same menus. What changes is the '
          'world around them. Version 4.0 brings a new career, <strong>World 2026-27</strong>: the 2026-27 season of '
          '91 countries, every league, cup and play-off rebuilt exactly as its federation wrote it.'],
    h_high='The highlights of 4.0',
    cards=[
     ('Every league in its real format',
      '22 leagues split mid-season as their regulations say, promotion and relegation play-offs in 17 countries, '
      'European play-offs, Argentina\'s Apertura and Clausura with relegation by promedio, the MLS with its two '
      'conferences and the MLS Cup Playoffs.'),
     ('European cups as UEFA plays them',
      'The league phase of 36 with 8 matches (6 in the Conference League), one table with all ten UEFA tie-breakers, '
      'the knockout play-offs and the seeded bracket, the qualifying paths of the 2026-27 access list, no away goals, '
      'and UEFA coefficients simulated from the second season.'),
     ('Italian football down to Serie D',
      'The Serie B play-off and play-out with their real rules, Serie C in three groups and its 28-club play-off, '
      'the real Serie D 2026-27 in 9 groups with play-offs, play-outs and the Poule Scudetto, the Coppa Italia '
      'Serie D on its real bracket.'),
     ('National cups as they really are',
      'Every club still in its cup when the data was taken, from its real round, with the ties really drawn; '
      'league cups such as the EFL Cup and the Coppa Italia Serie C; no cup where none is played in 2026-27.'),
     ('Real clubs, real squads',
      'Squads at the end of the summer 2026 transfer window, fixed shirt numbers as today, real coaches and kits; '
      'the club you manage gets its 9 real reserves, 25 players in all.'),
     ('Tables in colour, believable results',
      'Every table shows its end-of-season zones, as on TV; simulated matches with real draw rates and scorelines; '
      'each club\'s strength checked against the real 2025-26 tables.'),
    ],
    h_classic='And the classic game',
    classic='The 1996-97 world of the original game, with the competitions it never had: Serie C1 and C2, the South '
            'American, African, Asian and CONCACAF club cups, the Intercontinental Cup. Then the historic worlds: '
            'the <strong>Europe 1984-85</strong> career from DaniSwos\'s database, classic seasons such as the DDR '
            '1988-89 and Serie A 1947-48, classic tourneys such as the World Cup 1934.',
    h_install='How to install',
    steps=['Download <strong>swos-9697-mod-patcher.html</strong> from the release page and open it in your browser. '
           'It works offline too: nothing is uploaded anywhere.',
           'Drop in your language\'s executable and the game\'s <code>DATA</code> files, as the page asks, then '
           'download the patched files.',
           'Back up your game folder, copy the files into it (the TEAM files into <code>DATA</code>) and start a '
           'new career. In {careers} choose {world}, then the continent and the country.'],
    install_note='The patcher ships only differences and checks every file before and after patching: you need '
                 'your own original copy of SWOS 96/97, CD or GOG. Already on an older version of the mod? Drop the '
                 'files you have now: the patcher recognises them and brings them up to date. Saves are never '
                 'touched.',
    unofficial='Unofficial, free fan mod. Not affiliated with or endorsed by Sensible Software, its successors or '
               'the owners of the game, nor by any league, federation or UEFA. All names of clubs and competitions '
               'are used only to describe real football.',
    by='A mod by Davide Lorigliola, member of the cultural association 12 Bit Retrogaming (Trieste), and the SWOS community.',
    source='Source code and releases on GitHub',
    # countries
    h_countries='Every country, every competition',
    countries_lead='{n} countries and every playable competition, with its format, as the World 2026-27 plays it. '
                   'Generated from the mod\'s own data.',
    clubs_n='{n} clubs', comps_n='{n} competitions',
    c_lead='{name}: every playable competition in the World 2026-27, with its format.',
    c_game='The in-game FORMAT page', c_game_note='As the game shows it (FORMAT button of the competition).',
    c_details='Full details (English)', c_back='All countries',
    kind={'Cup': 'Cup', 'League cup': 'League cup'},
    approx='Declared approximation',
    # world page
    h_world='World 2026-27', world_lead='Today\'s football, rebuilt exactly, point by point.',
    meta_world='The World 2026-27 career of SWOS 96/97 Mod 4.0: every rule rebuilt exactly, point by point.',
    toc='On this page',
    # credits
    h_credits='Credits and data sources',
    credits_lead='Where the data comes from, and the people who helped.',
    testers='Testers and feedback', thanks_dani='The Europe 1984-85 database: <strong>DaniSwos</strong>.',
    h_classic_page='Classic careers, seasons and tourneys', classic_lead='The historic worlds of the mod.',
    lang_wip='', notfound='Page not found', notfound_p='This page is out of play.', back_home='Back to the home page',
 ),
 'it': dict(
    next41='Nella 4.1: il Mondiale 2026 e l\'Europeo 2024 tra i tornei storici, con le rose vere e le formule vere (48 squadre con le migliori terze; 24 squadre).',
    h_next='In arrivo',
    next_text='Nella 4.2: le nazionali del Mondo 2026-27, complete ed esatte. Rose vere, convocazioni dai club del mondo e offerte di lavoro da commissario tecnico; il Mondiale 2030 a 48 squadre e l\'Europeo 2028 a 24; le qualificazioni vere di ogni confederazione; la Nations League.',
    next_note='Un programma, non una data.',
    soon='Coming soon', soon_dl='Il patcher della 4.0: entro fine ottobre 2026',
    soon_install='La versione 4.0, con il Mondo 2026-27, arriva a breve: il giorno del rilascio il patcher sarà su questa pagina. Questi sono i passi che seguirai.',
    visits='Visite',
    frames=['CARR. STORICHE: i mondi storici', 'MONDO 2026-27: le nazioni d\'Europa',
            'La Serie A a metà stagione, con le sue zone', 'La classifica a 36 della Champions League dopo 4 giornate'],
    h_shots='Schermate dal gioco',
    shots=[('Il calcio italiano', [('serie-a-table-it', 'La Serie A a metà stagione, con le sue zone: Champions League, Europa League, Conference League, retrocessione'),
                                   ('serie-b-table-it', 'Serie B: promozione, play-off, play-out e retrocessione')]),
           ('La Serie D, quella vera', [('serie-d-table-it', 'Un girone di Serie D 2026-27, con le sue zone')]),
           ('Il calcio inglese', [('premier-table-it', 'La classifica della Premier League con le sue zone'),
                                  ('premier-format-it', 'La pagina FORMULA della Premier League')]),
           ('I campionati statali brasiliani', [('brazil-state-table-it', 'Il Campeonato Paulista 2026 dopo 7 giornate, con le sue zone'),
                                                ('brazil-state-format-it', 'La sua pagina FORMULA'),
                                                ('brazil-state-knockout-it', 'La finale del Paulista, andata: San Paolo-Palmeiras')]),
           ('Argentina 2026', [('argentina-zone-it', 'La Liga Profesional: una zona da 15 nell\'Apertura'),
                               ('argentina-promedio-it', 'La retrocessione per promedio e la classifica annuale')]),
           ('Major League Soccer 2026', [('mls-table-it', 'Le classifiche della Eastern e della Western Conference'),
                                         ('mls-playoffs-it', 'I play-off della MLS Cup')]),
           ('Split a metà stagione', [('split-scotland-it', 'Scozia: top six e bottom six dopo 33 giornate'),
                                      ('split-austria-it', 'Austria: la Meistergruppe dopo 22 giornate')]),
           ('UEFA Champions League: la fase campionato', [('cl-league-phase-it', 'La classifica a 36 dopo 4 giornate'),
                                                          ('cl-format-it', 'La pagina FORMULA della fase campionato')])],
    testers_p='<strong>Marco</strong> (le maglie viola, la musica dei menu con SWOS++), <strong>Daniele</strong> (il blocco di fine stagione con una squadra debole). Grazie!',
    site='World of SWOS', sub='SWOS 96/97 Mod',
    skip='Vai al contenuto', menu='Menu', lang_label='Lingua',
    nav_home='Home', nav_world='Mondo 2026-27', nav_countries='Nazioni', nav_classic='Carriere storiche',
    nav_install='Installazione', nav_credits='Crediti',
    meta_home='SWOS 96/97 Mod 4.0: la carriera Mondo 2026-27 per Sensible World of Soccer 96/97. 91 nazioni, rose '
              'vere e ogni competizione con la sua vera formula. Mod gratuita e non ufficiale.',
    kicker='SWOS 96/97 Mod 4.0 · Mondo 2026-27',
    tagline='Le competizioni di calcio, globali e locali, che nessun altro gioco ha, ha mai avuto e probabilmente avrà.',
    concept='Il solito grande SWOS di sempre e, insieme, un gioco completamente nuovo.',
    lead='Una mod gratuita per Sensible World of Soccer 96/97 (DOS, CD o GOG): il calcio di oggi com\'è davvero, '
         'campionato per campionato e coppa per coppa, in una carriera grande come il mondo, e il gioco del '
         '1996-97 com\'era davvero.',
    dl='Scarica il patcher', dl_small='gratis · funziona nel browser',
    how='Come si installa', see_world='Esplora il mondo',
    s_countries='nazioni', s_clubs='squadre', s_divisions='divisioni', s_cups='coppe nazionali',
    s_lcups='coppe di lega',
    h_what='Cos\'è la mod',
    what=['SWOS 96/97 Mod modifica la tua copia di <em>Sensible World of Soccer 96/97</em>, il gioco a cui giochiamo '
          'da trent\'anni, in tutte e quattro le sue lingue: italiano, inglese, francese e tedesco.',
          'Del gioco che ami non si perde niente: lo stesso campo, gli stessi omini che corrono, gli stessi menu. '
          'Cambia il mondo intorno. La versione 4.0 porta una nuova carriera, <strong>Mondo 2026-27</strong>: la '
          'stagione 2026-27 di 91 nazioni, ogni campionato, coppa e play-off ricostruiti esattamente come li ha '
          'scritti la sua federazione.'],
    h_high='Le novità della 4.0',
    cards=[
     ('Ogni campionato con la sua vera formula',
      '22 campionati che si dividono a metà stagione come dicono i regolamenti, play-off promozione e retrocessione '
      'in 17 nazioni, play-off europei, Apertura e Clausura argentini con la retrocessione per promedio, la MLS '
      'con le sue due conference e i play-off della MLS Cup.'),
     ('Le coppe europee come le gioca la UEFA',
      'La fase campionato a 36 con 8 partite (6 in Conference League), una classifica unica con tutti e dieci i '
      'criteri UEFA, gli spareggi e il tabellone con le teste di serie, i turni preliminari della lista d\'accesso '
      '2026-27, niente gol in trasferta e i coefficienti UEFA simulati dalla seconda stagione.'),
     ('Il calcio italiano fino alla Serie D',
      'Play-off e play-out di Serie B con le loro vere regole, la Serie C in tre gironi e il suo play-off a 28 '
      'squadre, la vera Serie D 2026-27 in 9 gironi con play-off, play-out e Poule Scudetto, la Coppa Italia '
      'Serie D sul suo vero tabellone.'),
     ('Le coppe nazionali come sono davvero',
      'Ogni squadra ancora in corsa quando sono stati presi i dati, dal suo vero turno, con gli accoppiamenti '
      'sorteggiati davvero; coppe di lega come la EFL Cup e la Coppa Italia Serie C; nessuna coppa dove nel '
      '2026-27 non si gioca.'),
     ('Squadre vere, rose vere',
      'Le rose a fine mercato estivo 2026, i numeri di maglia fissi come oggi, allenatori e maglie veri; la squadra '
      'che alleni ha anche le sue 9 vere riserve, 25 giocatori in tutto.'),
     ('Classifiche a colori, risultati credibili',
      'Ogni classifica mostra le sue zone di fine stagione, come in TV; partite simulate con le vere percentuali di '
      'pareggi e i veri punteggi; la forza di ogni squadra verificata sulle vere classifiche 2025-26.'),
    ],
    h_classic='E il gioco classico',
    classic='Il mondo 1996-97 del gioco originale, con le competizioni che non aveva: Serie C1 e C2, le coppe per '
            'club sudamericane, africane, asiatiche e CONCACAF, la Coppa Intercontinentale. Poi i mondi storici: la '
            'carriera <strong>Europa 1984-85</strong> dal database di DaniSwos, stagioni storiche come la DDR '
            '1988-89 e la Serie A 1947-48, tornei storici come i Mondiali 1934.',
    h_install='Come si installa',
    steps=['Scarica <strong>swos-9697-mod-patcher.html</strong> dalla pagina della release e aprilo nel browser. '
           'Funziona anche offline: non viene caricato niente da nessuna parte.',
           'Trascina l\'eseguibile della tua lingua e i file della cartella <code>DATA</code> del gioco, come chiede '
           'la pagina, poi scarica i file modificati.',
           'Fai una copia di sicurezza della cartella del gioco, copiaci i file (i TEAM in <code>DATA</code>) e '
           'inizia una nuova carriera. In {careers} scegli {world}, poi il continente e la nazione.'],
    install_note='Il patcher contiene solo le differenze e controlla ogni file prima e dopo: serve una tua copia '
                 'originale di SWOS 96/97, CD o GOG. Hai già una versione precedente della mod? Trascina i file che '
                 'hai adesso: il patcher li riconosce e li aggiorna. I salvataggi non vengono mai toccati.',
    unofficial='Mod amatoriale gratuita e non ufficiale. Non è affiliata né approvata da Sensible Software, dai suoi '
               'successori o dai proprietari del gioco, né da leghe, federazioni o dalla UEFA. I nomi di squadre e '
               'competizioni servono solo a descrivere il calcio vero.',
    by='Una mod di Davide Lorigliola, socio dell\'associazione culturale 12 Bit Retrogaming (Trieste), e della comunità di SWOS.',
    source='Codice sorgente e release su GitHub',
    h_countries='Ogni nazione, ogni competizione',
    countries_lead='{n} nazioni e ogni competizione giocabile, con la sua formula, come la gioca il Mondo 2026-27. '
                   'Generato dai dati della mod.',
    clubs_n='{n} squadre', comps_n='{n} competizioni',
    c_lead='{name}: ogni competizione giocabile nel Mondo 2026-27, con la sua formula.',
    c_game='La pagina FORMULA del gioco', c_game_note='Come la mostra il gioco (pulsante FORMULA della competizione).',
    c_details='Tutti i dettagli', c_back='Tutte le nazioni',
    kind={'Coppa': 'Coppa', 'Coppa di lega': 'Coppa di lega'},
    approx='Approssimazione dichiarata',
    h_world='Mondo 2026-27', world_lead='Il calcio di oggi, ricostruito esattamente, punto per punto.',
    meta_world='La carriera Mondo 2026-27 di SWOS 96/97 Mod 4.0: ogni regola ricostruita esattamente, punto per punto.',
    toc='In questa pagina',
    h_credits='Crediti e fonti dei dati', credits_lead='Da dove vengono i dati e chi ci ha aiutato.',
    testers='Tester e segnalazioni', thanks_dani='Il database Europa 1984-85: <strong>DaniSwos</strong>.',
    h_classic_page='Carriere, stagioni e tornei storici', classic_lead='I mondi storici della mod.',
    lang_wip='', notfound='Pagina non trovata', notfound_p='Questa pagina è finita fuori dal campo.',
    back_home='Torna alla home',
 ),
 'fr': dict(
    next41="Dans la 4.1 : la Coupe du monde 2026 et l'Euro 2024 parmi les tournois anciens, avec les vrais effectifs et les vraies formules (48 équipes avec les meilleurs troisièmes ; 24 équipes).",
    h_next='Prochainement',
    next_text="Dans la 4.2 : les sélections nationales du Monde 2026-27, complètes et exactes. De vrais effectifs, des convocations depuis les clubs du monde et des offres d'emploi de sélectionneur ; la Coupe du monde 2030 à 48 équipes et l'Euro 2028 à 24 ; les vraies qualifications de chaque confédération ; la Ligue des nations.",
    next_note='Un programme, pas une date.',
    soon='Coming soon', soon_dl='Le patcher de la 4.0 : d\'ici fin octobre 2026',
    soon_install='La version 4.0, avec le Monde 2026-27, arrive bientôt : le jour de la sortie, le patcher sera sur cette page. Voici les étapes que vous suivrez.',
    visits='Visites',
    frames=["CARR. D'ANTAN : les mondes historiques", "MONDE 2026-27 : les pays d'Europe",
            'La Serie A à mi-saison, avec ses zones', 'Le classement à 36 de la Ligue des champions après 4 journées'],
    h_shots='Écrans du jeu',
    shots=[('Le football italien', [('serie-a-table-it', 'La Serie A à mi-saison, avec ses zones : Champions League, Europa League, Conference League, relégation'),
                                    ('serie-b-table-it', 'Serie B : montée, barrages, maintien et relégation')]),
           ('La Serie D, la vraie', [('serie-d-table-it', 'Un groupe de Serie D 2026-27, avec ses zones')]),
           ('Le football français', [('ligue1-table-fr', 'La Ligue 1 2026-27 à mi-saison, avec ses zones'),
                                     ('ligue1-format-fr', 'La page FORMULE de la Ligue 1, avec les barrages')]),
           ('Le football anglais', [('premier-table-it', 'Le classement de la Premier League avec ses zones'),
                                    ('premier-format-it', 'La page FORMULE de la Premier League')]),
           ('Les championnats des États brésiliens', [('brazil-state-table-it', 'Le Campeonato Paulista 2026 après 7 journées, avec ses zones'),
                                                      ('brazil-state-format-it', 'Sa page FORMULE'),
                                                      ('brazil-state-knockout-it', 'La finale du Paulista, aller : São Paulo-Palmeiras')]),
           ('Argentine 2026', [('argentina-zone-it', "La Liga Profesional : une zone de 15 dans l'Apertura"),
                               ('argentina-promedio-it', 'La relégation au promedio et le classement annuel')]),
           ('Major League Soccer 2026', [('mls-table-it', "Les classements de l'Eastern et de la Western Conference"),
                                         ('mls-playoffs-it', 'Les play-offs de la MLS Cup')]),
           ('Scissions en cours de saison', [('split-scotland-it', 'Écosse : les six premiers et les six derniers après 33 journées'),
                                             ('split-austria-it', 'Autriche : la Meistergruppe après 22 journées')]),
           ('Ligue des champions de l\'UEFA : la phase de ligue', [('cl-league-phase-it', 'Le classement à 36 après 4 journées'),
                                                                   ('cl-format-it', 'La page FORMULE de la phase de ligue')])],
    testers_p='<strong>Marco</strong> (les maillots violets, la musique des menus avec SWOS++), <strong>Daniele</strong> (le blocage de fin de saison avec un club faible). Merci !',
    site='World of SWOS', sub='SWOS 96/97 Mod',
    skip='Aller au contenu', menu='Menu', lang_label='Langue',
    nav_home='Accueil', nav_world='Monde 2026-27', nav_countries='Pays', nav_classic="Carrières d'antan",
    nav_install='Installation', nav_credits='Crédits',
    meta_home="SWOS 96/97 Mod 4.0 : la carrière Monde 2026-27 pour Sensible World of Soccer 96/97. 91 pays, les vrais "
              "effectifs et chaque compétition dans sa vraie formule. Mod de fan gratuit et non officiel.",
    kicker='SWOS 96/97 Mod 4.0 · Monde 2026-27',
    tagline="Les compétitions de football, mondiales et locales, qu'aucun autre jeu n'a, n'a jamais eues et "
            "n'aura probablement jamais.",
    concept='Le grand SWOS de toujours et, en même temps, un jeu entièrement nouveau.',
    lead="Un mod gratuit pour Sensible World of Soccer 96/97 (DOS, CD ou GOG) : le football d'aujourd'hui tel qu'il "
         "est vraiment, championnat par championnat et coupe par coupe, dans une carrière aussi vaste que le monde, "
         "et le jeu de 1996-97 tel qu'il était vraiment.",
    dl='Télécharger le patcher', dl_small='gratuit · dans votre navigateur',
    how='Comment installer', see_world='Explorer le monde',
    s_countries='pays', s_clubs='clubs', s_divisions='divisions', s_cups='coupes nationales', s_lcups='coupes de la ligue',
    h_what="Qu'est-ce que le mod ?",
    what=["SWOS 96/97 Mod modifie votre propre copie de <em>Sensible World of Soccer 96/97</em>, le jeu auquel nous "
          "jouons depuis trente ans, dans ses quatre langues : italien, anglais, français et allemand.",
          "Rien ne se perd du jeu que vous aimez : le même terrain, les mêmes petits joueurs qui courent, les mêmes "
          "menus. C'est le monde autour qui change. La version 4.0 apporte une nouvelle carrière, <strong>Monde "
          "2026-27</strong> : la saison 2026-27 de 91 pays, chaque championnat, chaque coupe et chaque barrage "
          "reconstruits exactement comme leur fédération les a écrits."],
    h_high='Les nouveautés de la 4.0',
    cards=[
     ('Chaque championnat dans sa vraie formule',
      "22 championnats scindés en cours de saison comme le veulent leurs règlements, des barrages de montée et de "
      "relégation dans 17 pays, des barrages européens, l'Apertura et la Clausura argentines avec la relégation au "
      "promedio, la MLS avec ses deux conférences et les play-offs de la MLS Cup."),
     ("Les coupes d'Europe comme les joue l'UEFA",
      "La phase de ligue à 36 avec 8 matchs (6 en Conference League), un classement unique avec les dix critères "
      "de l'UEFA, les barrages et le tableau avec têtes de série, les tours de qualification de la liste d'accès "
      "2026-27, plus de buts à l'extérieur, et des coefficients UEFA simulés dès la deuxième saison."),
     ("Le football italien jusqu'à la Serie D",
      "Les barrages de montée et de maintien de Serie B avec leurs vraies règles, la Serie C en trois groupes et "
      "ses barrages à 28 clubs, la vraie Serie D 2026-27 en 9 groupes avec barrages, maintien et Poule Scudetto, "
      "la Coppa Italia Serie D sur son vrai tableau."),
     ('Les coupes nationales telles quelles',
      "Chaque club encore en lice au moment de la collecte des données, à partir de son vrai tour, avec les "
      "affiches réellement tirées ; des coupes de la ligue comme l'EFL Cup et la Coppa Italia Serie C ; aucune "
      "coupe là où il n'y en a pas en 2026-27."),
     ('De vrais clubs, de vrais effectifs',
      "Les effectifs à la fin du mercato d'été 2026, des numéros de maillot fixes comme aujourd'hui, les vrais "
      "entraîneurs et maillots ; le club que vous dirigez reçoit ses 9 vrais remplaçants, 25 joueurs en tout."),
     ('Des classements en couleur, des résultats crédibles',
      "Chaque classement affiche ses zones de fin de saison, comme à la télé ; des matchs simulés avec les vrais "
      "taux de nuls et les vrais scores ; la force de chaque club vérifiée sur les vrais classements 2025-26."),
    ],
    h_classic='Et le jeu classique',
    classic="Le monde 1996-97 du jeu original, avec les compétitions qui lui manquaient : la Serie C1 et C2, les "
            "coupes de clubs d'Amérique du Sud, d'Afrique, d'Asie et de la CONCACAF, la Coupe intercontinentale. Puis "
            "les mondes historiques : la carrière <strong>Europe 1984-85</strong> tirée de la base de données de "
            "DaniSwos, des saisons d'antan comme la RDA 1988-89 et la Serie A 1947-48, des tournois anciens comme "
            "la Coupe du monde 1934.",
    h_install='Comment installer',
    steps=["Téléchargez <strong>swos-9697-mod-patcher.html</strong> depuis la page de la version et ouvrez-le dans "
           "votre navigateur. Il fonctionne aussi hors ligne : rien n'est envoyé nulle part.",
           "Déposez l'exécutable de votre langue et les fichiers du dossier <code>DATA</code> du jeu, comme la page "
           "le demande, puis téléchargez les fichiers modifiés.",
           "Sauvegardez le dossier du jeu, copiez-y les fichiers (les fichiers TEAM dans <code>DATA</code>) et "
           "commencez une nouvelle carrière. Dans {careers}, choisissez {world}, puis le continent et le pays."],
    install_note="Le patcher ne contient que les différences et vérifie chaque fichier avant et après : il vous faut "
                 "votre propre copie originale de SWOS 96/97, CD ou GOG. Vous avez déjà une version précédente du "
                 "mod ? Déposez les fichiers que vous avez : le patcher les reconnaît et les met à jour. Les "
                 "sauvegardes ne sont jamais touchées.",
    unofficial="Mod de fan gratuit et non officiel. Il n'est ni affilié ni approuvé par Sensible Software, ses "
               "successeurs ou les propriétaires du jeu, ni par aucune ligue, fédération ou l'UEFA. Les noms des "
               "clubs et des compétitions ne servent qu'à décrire le vrai football.",
    by='Un mod de Davide Lorigliola, membre de l\'association culturelle 12 Bit Retrogaming (Trieste), et de la communauté SWOS.',
    source='Code source et versions sur GitHub',
    h_countries='Chaque pays, chaque compétition',
    countries_lead="{n} pays et chaque compétition jouable, avec sa formule, telle que la joue le Monde 2026-27. "
                   "Généré à partir des données du mod.",
    clubs_n='{n} clubs', comps_n='{n} compétitions',
    c_lead='{name} : chaque compétition jouable dans le Monde 2026-27, avec sa formule.',
    c_game='La page FORMULE du jeu', c_game_note='Telle que le jeu l\'affiche (bouton FORMULE de la compétition), en majuscules et sans accents.',
    c_details='Tous les détails (en anglais)', c_back='Tous les pays',
    kind={'Cup': 'Coupe', 'League cup': 'Coupe de la ligue'},
    approx='Approximation déclarée',
    h_world='Monde 2026-27', world_lead="Le football d'aujourd'hui, reconstruit exactement, point par point.",
    meta_world="La carrière Monde 2026-27 de SWOS 96/97 Mod 4.0 : chaque règle reconstruite exactement, point par point.",
    toc='Sur cette page',
    h_credits='Crédits et sources des données', credits_lead="D'où viennent les données, et ceux qui ont aidé.",
    testers='Testeurs et retours', thanks_dani='La base de données Europe 1984-85 : <strong>DaniSwos</strong>.',
    h_classic_page="Carrières, saisons et tournois d'antan", classic_lead='Les mondes historiques du mod.',
    lang_wip='Certaines parties ne sont pas encore traduites : elles apparaissent en anglais.',
    notfound='Page introuvable', notfound_p='Cette page est sortie du terrain.', back_home="Retour à l'accueil",
 ),
 'de': dict(
    next41='In 4.1: die WM 2026 und die EM 2024 bei den Turnierklassikern, mit den echten Kadern und den echten Modi (48 Teams mit den besten Gruppendritten; 24 Teams).',
    h_next='Als Nächstes',
    next_text='In 4.2: die Nationalmannschaften der Welt 2026-27, vollständig und genau. Echte Kader, Nominierungen aus den Vereinen der Welt und Jobangebote als Nationaltrainer; die WM 2030 mit 48 Teams und die EM 2028 mit 24; die echten Qualifikationen jeder Konföderation; die Nations League.',
    next_note='Ein Plan, kein Termin.',
    soon='Coming soon', soon_dl='Der Patcher der 4.0: bis Ende Oktober 2026',
    soon_install='Version 4.0 mit der Welt 2026-27 kommt bald: Am Tag der Veröffentlichung ist der Patcher auf dieser Seite. Das sind die Schritte, die du dann gehst.',
    visits='Besuche',
    frames=['KLASS. KARRIERE: die historischen Welten', 'WELT 2026-27: die Länder Europas',
            'Die Serie A zur Saisonmitte, mit ihren Zonen', 'Die Tabelle der Champions League mit 36 Vereinen nach 4 Spieltagen'],
    h_shots='Bilder aus dem Spiel',
    shots=[('Italiens Fußball', [('serie-a-table-it', 'Die Serie A zur Saisonmitte, mit ihren Zonen: Champions League, Europa League, Conference League, Abstieg'),
                                 ('serie-b-table-it', 'Serie B: Aufstieg, Playoffs, Playout und Abstieg')]),
           ('Die Serie D, die echte', [('serie-d-table-it', 'Eine Serie-D-Staffel 2026-27 mit ihren Zonen')]),
           ('Deutschlands Fußball', [('bundesliga-table-de', 'Die Bundesliga 2026-27 zur Saisonmitte, mit ihren Zonen'),
                                     ('bundesliga-format-de', 'Die MODUS-Seite der Bundesliga, mit der Relegation')]),
           ('Englands Fußball', [('premier-table-it', 'Die Tabelle der Premier League mit ihren Zonen'),
                                 ('premier-format-it', 'Die MODUS-Seite der Premier League')]),
           ('Brasiliens Staatsmeisterschaften', [('brazil-state-table-it', 'Die Campeonato Paulista 2026 nach 7 Spieltagen, mit ihren Zonen'),
                                                 ('brazil-state-format-it', 'Ihre MODUS-Seite'),
                                                 ('brazil-state-knockout-it', 'Das Finale der Paulista, Hinspiel: São Paulo gegen Palmeiras')]),
           ('Argentinien 2026', [('argentina-zone-it', 'Die Liga Profesional: eine Zone mit 15 Vereinen in der Apertura'),
                                 ('argentina-promedio-it', 'Abstieg nach Promedio und die Jahrestabelle')]),
           ('Major League Soccer 2026', [('mls-table-it', 'Die Tabellen der Eastern und der Western Conference'),
                                         ('mls-playoffs-it', 'Die MLS-Cup-Playoffs')]),
           ('Teilung zur Saisonmitte', [('split-scotland-it', 'Schottland: obere und untere sechs nach 33 Spieltagen'),
                                        ('split-austria-it', 'Österreich: die Meistergruppe nach 22 Spieltagen')]),
           ('UEFA Champions League: die Ligaphase', [('cl-league-phase-it', 'Die Tabelle mit 36 Vereinen nach 4 Spieltagen'),
                                                     ('cl-format-it', 'Die MODUS-Seite der Ligaphase')])],
    testers_p='<strong>Marco</strong> (lila Trikots, Menümusik mit SWOS++), <strong>Daniele</strong> (der Absturz am Saisonende mit einem schwachen Verein). Danke!',
    site='World of SWOS', sub='SWOS 96/97 Mod',
    skip='Zum Inhalt', menu='Menü', lang_label='Sprache',
    nav_home='Start', nav_world='Welt 2026-27', nav_countries='Länder', nav_classic='Klassische Karrieren',
    nav_install='Installation', nav_credits='Credits',
    meta_home='SWOS 96/97 Mod 4.0: die Karriere Welt 2026-27 für Sensible World of Soccer 96/97. 91 Länder, echte '
              'Kader und jeder Wettbewerb in seinem echten Modus. Kostenlose, inoffizielle Fan-Mod.',
    kicker='SWOS 96/97 Mod 4.0 · Welt 2026-27',
    tagline='Fußballwettbewerbe, weltweit und lokal, wie sie kein anderes Spiel hat, je hatte und wohl je haben wird.',
    concept='Das große SWOS wie eh und je und zugleich ein völlig neues Spiel.',
    lead='Eine kostenlose Fan-Mod für Sensible World of Soccer 96/97 (DOS, CD oder GOG): der Fußball von heute, wie '
         'er wirklich ist, Liga für Liga und Pokal für Pokal, in einer Karriere so groß wie die Welt, und das Spiel '
         'von 1996-97, wie es wirklich war.',
    dl='Patcher herunterladen', dl_small='kostenlos · läuft im Browser',
    how='So wird installiert', see_world='Die Welt entdecken',
    s_countries='Länder', s_clubs='Vereine', s_divisions='Ligen und Staffeln', s_cups='Landespokale',
    s_lcups='Ligapokale',
    h_what='Was ist die Mod?',
    what=['SWOS 96/97 Mod verändert deine eigene Kopie von <em>Sensible World of Soccer 96/97</em>, dem Spiel, das wir '
          'seit dreißig Jahren spielen, in allen vier Sprachen: Italienisch, Englisch, Französisch und Deutsch.',
          'Vom Spiel, das du liebst, geht nichts verloren: derselbe Platz, dieselben kleinen Spieler, dieselben Menüs. '
          'Anders ist die Welt drumherum. Version 4.0 bringt eine neue Karriere, <strong>Welt 2026-27</strong>: die '
          'Saison 2026-27 von 91 Ländern, jede Liga, jeder Pokal und jedes Playoff genau so nachgebaut, wie der '
          'Verband es festgelegt hat.'],
    h_high='Das Neue in 4.0',
    cards=[
     ('Jede Liga in ihrem echten Modus',
      '22 Ligen, die sich zur Saisonmitte teilen, wie es ihre Statuten vorsehen, Auf- und Abstiegsplayoffs in 17 '
      'Ländern, Europapokal-Playoffs, Apertura und Clausura in Argentinien mit Abstieg nach Promedio, die MLS mit '
      'ihren zwei Conferences und den MLS-Cup-Playoffs.'),
     ('Europapokale, wie die UEFA sie spielt',
      'Die Ligaphase mit 36 Vereinen und 8 Spielen (6 in der Conference League), eine einzige Tabelle mit allen '
      'zehn UEFA-Kriterien, die K.-o.-Playoffs und der gesetzte Turnierbaum, die Qualifikationswege der '
      'Zulassungsliste 2026-27, keine Auswärtstorregel und ab der zweiten Saison simulierte UEFA-Koeffizienten.'),
     ('Italiens Fußball bis zur Serie D',
      'Playoffs und Playout der Serie B mit ihren echten Regeln, die Serie C in drei Staffeln und ihre Playoffs mit '
      '28 Vereinen, die echte Serie D 2026-27 in 9 Staffeln mit Playoffs, Playouts und Poule Scudetto, die Coppa '
      'Italia Serie D mit ihrem echten Turnierbaum.'),
     ('Landespokale, wie sie wirklich sind',
      'Jeder Verein, der bei der Datenerhebung noch im Wettbewerb war, ab seiner echten Runde, mit den wirklich '
      'ausgelosten Paarungen; Ligapokale wie der EFL Cup und die Coppa Italia Serie C; kein Pokal, wo 2026-27 '
      'keiner gespielt wird.'),
     ('Echte Vereine, echte Kader',
      'Die Kader zum Ende der Sommer-Transferperiode 2026, feste Rückennummern wie heute, echte Trainer und Trikots; '
      'dein eigener Verein bekommt seine 9 echten Ersatzspieler dazu, 25 Spieler insgesamt.'),
     ('Farbige Tabellen, glaubwürdige Ergebnisse',
      'Jede Tabelle zeigt ihre Zonen zum Saisonende, wie im Fernsehen; simulierte Spiele mit echten Remis-Quoten und '
      'Ergebnissen; die Stärke jedes Vereins an den echten Tabellen 2025-26 geprüft.'),
    ],
    h_classic='Und das klassische Spiel',
    classic='Die Welt 1996-97 des Originalspiels, mit den Wettbewerben, die ihr fehlten: Serie C1 und C2, die '
            'Vereinspokale Südamerikas, Afrikas, Asiens und der CONCACAF, der Weltpokal. Dazu die historischen '
            'Welten: die Karriere <strong>Europa 1984-85</strong> aus der Datenbank von DaniSwos, '
            'Saisonklassiker wie die DDR 1988-89 und die Serie A 1947-48, Turnierklassiker wie die WM 1934.',
    h_install='So wird installiert',
    steps=['Lade <strong>swos-9697-mod-patcher.html</strong> von der Release-Seite herunter und öffne die Datei im '
           'Browser. Sie funktioniert auch offline: Es wird nichts hochgeladen.',
           'Zieh die ausführbare Datei deiner Sprache und die Dateien aus dem Ordner <code>DATA</code> des Spiels '
           'hinein, wie die Seite es verlangt, und lade dann die gepatchten Dateien herunter.',
           'Sichere den Spielordner, kopiere die Dateien hinein (die TEAM-Dateien nach <code>DATA</code>) und starte '
           'eine neue Karriere. Unter {careers} wählst du {world}, dann den Kontinent und das Land.'],
    install_note='Der Patcher enthält nur die Unterschiede und prüft jede Datei vorher und nachher: Du brauchst deine '
                 'eigene Originalkopie von SWOS 96/97, CD oder GOG. Du hast schon eine ältere Version der Mod? Zieh '
                 'die Dateien hinein, die du jetzt hast: Der Patcher erkennt sie und bringt sie auf den neuesten '
                 'Stand. Spielstände werden nie angerührt.',
    unofficial='Inoffizielle, kostenlose Fan-Mod. Weder verbunden mit noch unterstützt von Sensible Software, deren '
               'Nachfolgern oder den Rechteinhabern des Spiels, noch von Ligen, Verbänden oder der UEFA. Die Namen '
               'von Vereinen und Wettbewerben dienen nur dazu, den echten Fußball zu beschreiben.',
    by='Eine Mod von Davide Lorigliola, Mitglied des Kulturvereins 12 Bit Retrogaming (Triest), und der SWOS-Community.',
    source='Quellcode und Releases auf GitHub',
    h_countries='Jedes Land, jeder Wettbewerb',
    countries_lead='{n} Länder und jeder spielbare Wettbewerb mit seinem Modus, wie ihn die Welt 2026-27 spielt. '
                   'Aus den Daten der Mod erzeugt.',
    clubs_n='{n} Vereine', comps_n='{n} Wettbewerbe',
    c_lead='{name}: jeder spielbare Wettbewerb in der Welt 2026-27, mit seinem Modus.',
    c_game='Die MODUS-Seite im Spiel', c_game_note='So wie das Spiel sie zeigt (Schaltfläche MODUS des Wettbewerbs), in Großbuchstaben und ohne Umlaute.',
    c_details='Alle Details (Englisch)', c_back='Alle Länder',
    kind={'Cup': 'Pokal', 'League cup': 'Ligapokal'},
    approx='Erklärte Annäherung',
    h_world='Welt 2026-27', world_lead='Der Fußball von heute, genau nachgebaut, Punkt für Punkt.',
    meta_world='Die Karriere Welt 2026-27 von SWOS 96/97 Mod 4.0: jede Regel genau nachgebaut, Punkt für Punkt.',
    toc='Auf dieser Seite',
    h_credits='Credits und Datenquellen', credits_lead='Woher die Daten kommen und wer geholfen hat.',
    testers='Tester und Rückmeldungen', thanks_dani='Die Datenbank Europa 1984-85: <strong>DaniSwos</strong>.',
    h_classic_page='Klassische Karrieren, Saisons und Turniere', classic_lead='Die historischen Welten der Mod.',
    lang_wip='Einige Teile sind noch nicht übersetzt: Sie erscheinen auf Englisch.',
    notfound='Seite nicht gefunden', notfound_p='Diese Seite ist im Aus.', back_home='Zurück zur Startseite',
 ),
}
