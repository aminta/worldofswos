# DNS per worldofswos.com e worldofswos.it (da applicare a mano da Davide su Register.it)

Stato al 2026-10-19 sera: FATTO. worldofswos.com: 4 A + 4 AAAA GitHub Pages, www CNAME aminta.github.io.,
certificato approvato, HTTPS obbligatorio. worldofswos.it: redirect di Register.it (pagina JS) verso
http://worldofswos.com/it/ (che passa poi a https). https://worldofswos.it non risponde (Register.it non ha
certificato per il redirect): per averlo, opzione B sotto. Record della posta (MX/TXT/SRV) lasciati intatti.
Register.it: Pannello > worldofswos.com > DOMINIO & DNS > **Configurazione DNS** (per il .it: **Redirect e sottodomini**).

Il sito è servito da GitHub Pages (repo `aminta/worldofswos`, cartella `site/`, file `CNAME` = `worldofswos.com`).
Valori ufficiali GitHub: https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site

## worldofswos.com (dominio principale)

| Tipo  | Nome (host) | Valore                    |
|-------|-------------|---------------------------|
| A     | @           | 185.199.108.153           |
| A     | @           | 185.199.109.153           |
| A     | @           | 185.199.110.153           |
| A     | @           | 185.199.111.153           |
| AAAA  | @           | 2606:50c0:8000::153       |
| AAAA  | @           | 2606:50c0:8001::153       |
| AAAA  | @           | 2606:50c0:8002::153       |
| AAAA  | @           | 2606:50c0:8003::153       |
| CNAME | www         | aminta.github.io.         |

Togliere eventuali A/AAAA/CNAME di parcheggio del registrar su `@` e `www`.
Poi su GitHub: Settings > Pages > Custom domain = `worldofswos.com`, attendere il certificato, spuntare
"Enforce HTTPS". Consigliato: verificare il dominio in Settings (account) > Pages > Verified domains
(record TXT `_github-pages-challenge-aminta` che GitHub mostra in quel momento).

## worldofswos.it (redirect verso il .com)

GitHub Pages serve un solo dominio per repo, quindi il .it va rediretto dal registrar:
- **Opzione A (consigliata)**: redirect/inoltro web permanente (301) del registrar da `worldofswos.it` e
  `www.worldofswos.it` a `https://worldofswos.com/it/`, se il registrar lo offre con HTTPS.
- **Opzione B**: un secondo repo minimo `aminta/worldofswos-it` con GitHub Pages, CNAME `worldofswos.it` e una pagina
  che rimanda a `https://worldofswos.com/it/` (meta refresh + canonical); stessi record A/AAAA del .com su `@` e
  `www CNAME aminta.github.io.` sul .it. Ha HTTPS sicuro via GitHub.

Nessun record MX è necessario per il sito.
