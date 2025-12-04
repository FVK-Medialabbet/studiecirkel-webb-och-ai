# Ollama + Open WebUI – Lokal AI-miljö på Medialabbet
Senast uppdaterad: 2025-11-28

Denna guide beskriver hur vi på Medialabbet sätter upp en lokal AI-miljö för kodning och text på workstation-laptopen med Ubuntu 25.04 och NVIDIA Quadro P2000 Mobile (4 GB VRAM).

Målet är att:
- köra små, resurssnåla modeller lokalt med Ollama
- få ett webbaserat gränssnitt via Open WebUI
- använda modeller som är särskilt lämpade för kod (coder-modeller)

---

## 1. Systemförutsättningar

- OS: Ubuntu 25.04
- RAM: 32 GB
- GPU: NVIDIA Quadro P2000 Mobile (ca 4 GB VRAM)
- Nätverk: Lokalt nätverk räcker (för att andra ska kunna nå Open WebUI)

Begränsningar:
- 4 GB VRAM innebär att vi använder små till medelstora modeller (1–2B parametrar, eventuellt 3B i kvantiserad form).

---

## 2. Installera Ollama

1. Uppdatera paket:
   ```bash
   sudo apt update
   ```

2. Installera Ollama med officiellt script:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

3. Logga ut/in eller starta om terminal för att säkerställa att kommandot `ollama` finns i PATH.

4. Verifiera installation:
   ```bash
   ollama --version
   ```

---

## 3. Rekommenderade modeller för Medialabbet

Vi fokuserar på små kodmodeller som fungerar bra med 4 GB VRAM.

### 3.1 Kodmodeller

1. Qwen2.5 Coder 1.5B:
   ```bash
   ollama pull qwen2.5-coder:1.5b
   ```

2. CodeGemma 2B:
   ```bash
   ollama pull codegemma:2b
   ```

Dessa modeller används för:
- kodförslag
- generering av funktioner, skript och konfigurationsfiler
- förklaringar av kod och enklare arkitekturdiskussioner

---

## 4. Enkel användning via terminal

Exempel: starta en konversation med Qwen2.5 Coder:

```bash
ollama run qwen2.5-coder:1.5b
```

Exempel: starta CodeGemma:

```bash
ollama run codegemma:2b
```

Avsluta med Ctrl+C när du är klar.

---

## 5. Installera Docker (för Open WebUI)

För att köra Open WebUI använder vi Docker.

1. Installera Docker och Compose-plugin:
   ```bash
   sudo apt update
   sudo apt install docker.io docker-compose-plugin -y
   sudo usermod -aG docker $USER
   ```

2. Logga ut och in igen så att användaren får docker-rättigheter.

3. Testa:
   ```bash
   docker ps
   ```

---

## 6. Installera Open WebUI som frontend till Ollama

Vi använder Open WebUI som ett webbaserat gränssnitt ovanpå Ollama.

Skapa en mapp, t.ex.:

```bash
mkdir -p ~/openwebui
cd ~/openwebui
```

Skapa filen `docker-compose.yml` med följande innehåll:

```yaml
version: "3.9"

services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:latest
    container_name: open-webui
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
    volumes:
      - ./data:/app/backend/data
    restart: unless-stopped
```

Starta Open WebUI:

```bash
docker compose up -d
```

Efter start nås Open WebUI i webbläsare via:

http://localhost:3000

För att stänga ned:

```bash
docker compose down
```

---

## 7. Koppla Open WebUI till Ollama-modeller

När Open WebUI är igång och Ollama kör på standardport (11434):

1. Öppna http://localhost:3000 i webbläsaren.
2. Skapa första admin-användaren (guiden på skärmen).
3. Under modellval kan du välja t.ex.:
   - `qwen2.5-coder:1.5b`
   - `codegemma:2b`

Om modellerna inte syns direkt:
- se till att de är nedladdade med `ollama pull`
- prova att starta om Ollama-tjänsten:
  ```bash
  sudo systemctl restart ollama
  ```

---

## 8. Förslag på användningssätt i Medialabbet

### 8.1 Kodning och infrastruktur

Använd modellerna till att:
- generera bash-skript och Dockerfiler
- föreslå struktur för repo (mappar, filer, README)
- skriva exempel på konfiguration (t.ex. docker-compose för Katchapp-dev)

### 8.2 Dokumentation och planering

- skriva första utkast till README-filer
- beskriva arkitektur i textform
- ta fram checklistor för nästa steg i utvecklingsmiljön

---

## 9. Nästa steg

1. Testa `qwen2.5-coder:1.5b` och `codegemma:2b` mot verkliga uppgifter i Medialabbet.
2. Om prestanda känns bra kan fler små modeller testas vid behov.
3. När Katchapp-projektet går vidare mot moln-drift kan samma arbetssätt återanvändas:
   - Ollama eller liknande i servermiljö
   - Open WebUI eller annan UI-lösning
   - fler/tyngre modeller på mer kraftfull hårdvara.