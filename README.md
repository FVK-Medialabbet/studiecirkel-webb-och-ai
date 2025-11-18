<p align="center">
  <img src="docs/assets/images/medialabbet-logo-anim.svg" height="140">
</p>

# Medialabbet – Introduktionskurs i generativ AI

Det här repot innehåller kursmaterialet för Medialabbets introduktionskurs i generativ AI och stora språkmodeller (LLM).

Kursen bygger på:
- öppna källor och aktuella exempel om generativ AI
- praktiska erfarenheter från Medialabbet, Friskvårdsklubben och Bottennappet i Väst
- eget framtaget material, övningar och diskussionsfrågor

Materialet publiceras både som:
- en **webbsida** via MkDocs + GitHub Pages
- **PDF**:er som kan delas och skrivas ut till deltagare

Allt innehåll skrivs i **Markdown** och genereras automatiskt till hemsidan: https://fvk-medialabbet.github.io/ai-kurs-medialabbet/

---

## Struktur

Den viktigaste strukturen i repot:
```text
    .
    ├── docs/                    # Allt kursinnehåll (Markdown)
    │   ├── index.md             # Startsida / kursöversikt
    │   ├── kapitel-01-....md    # Kapitel 1 – Generativ AI och datans roll
    │   ├── kapitel-02-....md    # Kapitel 2 – Stora språkmodeller (LLM)
    │   └── assets/
    │       └── images/
    │           ├── medialabbet-logo.png
    │           ├── medialabbet-logo.svg
    │           ├── medialabbet-logo-anim.svg
    │           └── medialabbet-logo-icon.svg
    ├── mkdocs.yml               # MkDocs-konfiguration
    ├── requirements.txt         # Python-dependenser (MkDocs, tema m.m.)
    └── .github/workflows/       # GitHub Actions för build/deploy
```
Lägg till fler kapitel, övningar och bilagor genom att skapa nya `.md`-filer i `docs/` och uppdatera navigeringen i `mkdocs.yml`.

---

## Logotyper och grafik

Loggorna ligger i `docs/assets/images/`:

- `medialabbet-logo-anim.svg` – animerad fullbreddslogga  
- `medialabbet-logo.svg` – statisk fullbreddslogga (vektor)  
- `medialabbet-logo.png` – statisk fullbreddslogga (raster)  
- `medialabbet-logo-icon.svg` – stiliserad M-ikon för mindre ytor

### Användning i sidor under `docs/`

Animerad logga högst upp på en sida:
```markdown
    ![Medialabbet logotyp](assets/images/medialabbet-logo-anim.svg)
```
Statisk logga:
```markdown
    ![Medialabbet logotyp](assets/images/medialabbet-logo.svg)
```
Ikon, t.ex. i en info-ruta:
```markdown
    ![Medialabbet ikon](assets/images/medialabbet-logo-icon.svg)
```
### Användning i README (den här filen)

I början av filen används:
```html
    <p align="center">
      <img src="docs/assets/images/medialabbet-logo-anim.svg" alt="Medialabbet logotyp" height="140">
    </p>
```
Justera gärna höjd eller byt till statisk logga om du vill.

---

## Köra sajten lokalt

För att bygga och testa kurswebben lokalt:

1. Installera Python 3 om det inte redan finns.
2. Installera beroenden:
```bash
       pip install -r requirements.txt
```
3. Starta utvecklingsservern:
```bash
       mkdocs serve
```
4. Öppna webbläsaren och gå till:

       http://127.0.0.1:8000

När du sparar en `.md`-fil i `docs/` uppdateras sidan automatiskt.

---

## Publicering via GitHub Pages

Det här repot är baserat på `Andre601/mkdocs-template` och har en färdig GitHub Actions-workflow som:

- bygger MkDocs-sajten
- deployar den till branchen `gh-pages`
- publicerar kursen via GitHub Pages

Vanligt flöde:

1. Pusha ändringar till `main`.
2. Vänta tills Actions-jobbet (deploy) är klart.
3. Hitta kurs-sajten under repo-inställningar → **Pages**.

---

## Licens och källor

Kursmaterialet i det här repot är framtaget av FVK-Medialabbet och får vidareutvecklas över tid i takt med att vi lär oss mer och samlar in erfarenheter från deltagare.

Innehållet är inspirerat av, men inte översatt från, bland annat:

- *Generative AI and LLMs For Dummies, Snowflake Special Edition* (John Wiley & Sons, 2024)
- artiklar, bloggar och videor om generativ AI och LLM:er
- praktiska erfarenheter från Medialabbet, Friskvårdsklubben och Bottennappet i Väst

När vi bestämt hur materialet får återanvändas lägger vi till en tydlig licens (t.ex. en Creative Commons-licens).
