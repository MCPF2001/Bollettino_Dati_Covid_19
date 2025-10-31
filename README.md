# Bollettino_Dati_Covid_19


Progetto sviluppato per un **esame accademico**.
L’app mostra i dati COVID-19 (formato JSON) pubblicati dalla Protezione Civile: [https://github.com/pcm-dpc/COVID-19](https://github.com/pcm-dpc/COVID-19).

## Obiettivo

Visualizzare in una tabella i principali indicatori (data, regione, ricoverati, TI, ospedalizzati, guariti, deceduti) e permettere la selezione della riga per vedere/modificare i campi.

## Stack

* **Python 3**
* **Tkinter** / **ttk** per GUI
* **configparser** per configurazioni (opzionale)
* (opzionale) **requests** se si vogliono caricare i JSON direttamente da URL

## Dati sorgente

Repository ufficiale PCM-DPC, sezione *dati in formato JSON*.
Si possono usare:

* JSON **regionali**: `dpc-covid19-ita-regioni.json`
* oppure file giornalieri/storici equivalenti

> In alternativa si può lavorare con un JSON locale scaricato dal repo.

## Come funziona

1. **Avvio GUI**: finestra principale Tkinter (1280×720), `Treeview` ttk con scrollbar.
2. **Caricamento dati**:

   * Versione base: dati caricati da lista/JSON locale.
   * Versione estesa: lettura JSON via URL (requests) o da file.
3. **Tabella**: colonne `Data`, `Stato`, `Regione`, `Ricoverati con sintomi`, `Terapia intensiva`, `Totale ospedalizzati`, `Guariti`, `Deceduti`.
   Righe con “striping” per leggibilità.
4. **Selezione riga**: click sulla tabella → i campi a destra si popolano con i valori selezionati.
5. **Icona app (opzionale)**: si può impostare un’icona `.ico`.

## Requisiti

Python 3. Tkinter e configparser sono nella standard library.
Se carichi da URL:

```bash
pip install requests
```

## Esecuzione

Da terminale nella cartella del progetto:

```bash
python3 "Covid 19 .py"
```

> Suggerito: rinominare il file in `main.py` per semplicità.

## Configurazione (opzionale)

Puoi usare `config.ini` per impostare icon e sorgente dati:

```ini
[app]
icon=bacterium.ico
# sorgente dati: "url" oppure "file"
source=url
url=https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json
file=./dati/dpc-covid19-ita-regioni.json
```

Nel codice:

* Leggi la sezione `[app]` con `ConfigParser`.
* Se `source=url` → richiama `requests.get(url)` e fai `json()`.
* Se `source=file` → `json.load(open(file))`.

## Struttura (esempio)

```
.
├─ main.py
├─ README.md
├─ bacterium.ico               # opzionale
├─ config.ini                  # opzionale
└─ dati/                       # opzionale, se lavori offline
   └─ dpc-covid19-ita-regioni.json
```

## Note

* La GUI attuale visualizza e seleziona i record.
* Estensioni possibili: filtri per regione/data, grafici, export CSV, aggiornamento automatico.

## Licenza

Uso accademico/didattico. I dati restano di proprietà PCM-DPC (vedi repo ufficiale).

## 📬 Contatti

Per domande o suggerimenti, contattami su **Telegram**: @MCPF2001







