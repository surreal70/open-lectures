---
author: Andreas Hümmer
title: 'Praxisübung: Prozessverwaltung mit Shell-Kommandos'
tags:
  - uebung
  - praxis
  - bs
  - prozesse
  - shell
  - linux
  - windows
bereich: BS
created: '2026-10-09'
modified: '2026-10-09'
---

# Praxisübung: Prozessverwaltung mit Shell-Kommandos

**Bereich:** BS – Prozesse und Systemadministration
**Voraussetzungen:** Terminal/Shell-Zugang (Linux oder Windows), Grundkenntnisse Kommandozeile

---

> [!info] **Lernziele**
> Nach dieser Übung solltest du:
> - Prozesse mit Shell-Kommandos anzeigen und analysieren können
> - Prozess-Prioritäten verstehen und ändern können
> - Threads eines Prozesses identifizieren können
> - IPC-Ressourcen (Pipes, Shared Memory, Sockets) untersuchen können
> - Signale an Prozesse senden können

---

## Vorbereitung

### Linux

Öffne ein Terminal. Die meisten Kommandos funktionieren auf jeder Linux-Distribution.

### Windows

Öffne **PowerShell** (als Administrator für manche Aufgaben) oder **cmd.exe**.

> [!tip] **WSL-Nutzer**
> Wenn du Windows Subsystem for Linux (WSL) verwendest, kannst du alle Linux-Kommandos dort ausführen.

---

## Teil 1: Prozesse anzeigen und analysieren

### Aufgabe 1.1: Prozessliste (Linux)

**Führe folgende Kommandos aus und dokumentiere die Ergebnisse:**

```bash
# 1. Alle Prozesse mit Details anzeigen
ps aux | head -20

# 2. Nur deine eigenen Prozesse
ps -u $USER

# 3. Prozessbaum anzeigen (Eltern-Kind-Beziehungen)
pstree -p | head -30

# 4. Top 5 Prozesse nach CPU-Nutzung
ps aux --sort=-%cpu | head -6

# 5. Top 5 Prozesse nach Speichernutzung
ps aux --sort=-%mem | head -6
```

**Fragen:**

a) Welcher Prozess hat die PID 1? Was ist seine Rolle?

_Dein Antwort:_

<br><br>

b) Finde einen Prozess im Zustand "S" (Sleeping). Was bedeutet dieser Zustand?

_Dein Antwort:_

<br><br>

---

### Aufgabe 1.2: Prozessliste (Windows PowerShell)

```powershell
# 1. Alle Prozesse anzeigen
Get-Process | Select-Object -First 20

# 2. Prozesse nach CPU sortiert
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10

# 3. Prozesse nach Speicher (WorkingSet) sortiert
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10

# 4. Detailinfo zu einem bestimmten Prozess (z.B. explorer)
Get-Process -Name explorer | Format-List *
```

**Frage:** Welcher Prozess verbraucht aktuell am meisten CPU auf deinem System?

_Dein Antwort:_

<br><br>

---

## Teil 2: Prozess-Details untersuchen

### Aufgabe 2.1: /proc Dateisystem (Linux)

Das `/proc` Dateisystem ist eine virtuelle Schnittstelle zum Kernel. Jeder Prozess hat ein Verzeichnis unter `/proc/<PID>/`.

```bash
# 1. Finde die PID deiner Shell
echo $$

# 2. Untersuche das Verzeichnis deiner Shell
ls -la /proc/$$/

# 3. Prozess-Status anzeigen
cat /proc/$$/status

# 4. Speicherlayout anzeigen
cat /proc/$$/maps | head -20

# 5. Geöffnete Dateien
ls -la /proc/$$/fd/

# 6. Kommandozeile des Prozesses
cat /proc/$$/cmdline
```

**Aufgabe:** Finde einen laufenden Browser (z.B. Firefox, Chrome) und untersuche seinen Speicherverbrauch:

```bash
# PID von Firefox finden
pgrep -x firefox   # oder: pgrep chrome

# Speicherinfo anzeigen
cat /proc/<PID>/status | grep -E "(VmSize|VmRSS|VmData|VmStk)"
```

**Dokumentiere:**
- VmSize (Virtueller Speicher): _____ kB
- VmRSS (Resident Set Size): _____ kB
- VmData (Data Segment): _____ kB
- VmStk (Stack): _____ kB

---

### Aufgabe 2.2: Zombie-Prozesse finden (Linux)

Zombie-Prozesse sind beendete Kindprozesse, deren Exit-Status noch nicht vom Elternprozess abgeholt wurde.

```bash
# Zombie-Prozesse finden (Status 'Z')
ps aux | grep 'Z'

# Oder mit awk für bessere Filterung
ps aux | awk '$8 ~ /Z/ {print}'
```

**Frage:** Gibt es Zombie-Prozesse auf deinem System? Wenn ja, welcher Elternprozess ist verantwortlich?

_Dein Antwort:_

<br><br>

---

## Teil 3: Threads untersuchen

### Aufgabe 3.1: Threads eines Prozesses (Linux)

```bash
# 1. Firefox/Chrome starten (falls nicht bereits läuft)

# 2. Alle Threads eines Prozesses anzeigen
ps -T -p $(pgrep -x firefox) | head -20

# 3. Anzahl der Threads zählen
ps -T -p $(pgrep -x firefox) | wc -l

# 4. Threads im /proc Verzeichnis
ls /proc/$(pgrep -x firefox)/task/
```

**Frage:** Wie viele Threads hat dein Browser? Warum sind es so viele?

_Dein Antwort:_

<br><br>

---

## Teil 4: Prozess-Prioritäten

### Aufgabe 4.1: Nice-Werte (Linux)

Der "nice"-Wert bestimmt die Prozesspriorität. Höherer nice = niedrigere Priorität (der Prozess ist "netter" zu anderen).

```bash
# 1. nice-Werte aller Prozesse anzeigen
ps -eo pid,ni,comm | head -20

# 2. Prozess mit niedrigerer Priorität starten
nice -n 10 sleep 60 &

# 3. nice-Wert des gestarteten Prozesses prüfen
ps -o pid,ni,comm -p $!

# 4. Priorität eines laufenden Prozesses ändern (sudo nötig)
# sudo renice -n 15 -p <PID>
```

**Experiment:** Starte zwei CPU-intensive Prozesse mit unterschiedlichen nice-Werten und beobachte mit `top`:

```bash
# Terminal 1: Normale Priorität
dd if=/dev/zero of=/dev/null &
PID1=$!

# Terminal 2: Niedrige Priorität
nice -n 19 dd if=/dev/zero of=/dev/null &
PID2=$!

# In top: Drücke 'r' zum Renice oder beobachte CPU-Verteilung
top

# Aufräumen
kill $PID1 $PID2
```

**Frage:** Welchen Unterschied beobachtest du in der CPU-Nutzung?

_Dein Antwort:_

<br><br>

---

### Aufgabe 4.2: Prioritäten (Windows PowerShell)

```powershell
# 1. Prozess-Prioritäten anzeigen
Get-Process | Select-Object Name, PriorityClass | Where-Object {$_.PriorityClass -ne $null}

# 2. Prioritätsklassen:
# - Idle, BelowNormal, Normal, AboveNormal, High, RealTime

# 3. Notepad mit hoher Priorität starten
Start-Process -FilePath "notepad.exe" -Priority High

# 4. Priorität eines laufenden Prozesses ändern
# $p = Get-Process -Name notepad
# $p.PriorityClass = "AboveNormal"
```

---

## Teil 5: Interprozesskommunikation (IPC)

### Aufgabe 5.1: Pipes in der Shell (Linux)

```bash
# 1. Einfache Pipeline
cat /var/log/syslog | grep error | wc -l

# 2. Named Pipe (FIFO) erstellen
mkfifo /tmp/mypipe

# Terminal 1: Auf Pipe schreiben
echo "Hello from Terminal 1" > /tmp/mypipe

# Terminal 2: Von Pipe lesen
cat /tmp/mypipe

# 3. Aufräumen
rm /tmp/mypipe
```

**Experiment:** Erstelle eine Named Pipe und übertrage Daten zwischen zwei Terminal-Fenstern.

---

### Aufgabe 5.2: IPC-Ressourcen anzeigen (Linux)

```bash
# 1. System V IPC Ressourcen anzeigen
ipcs

# 2. Nur Shared Memory Segmente
ipcs -m

# 3. Nur Semaphore
ipcs -s

# 4. Nur Message Queues
ipcs -q

# 5. POSIX Shared Memory
ls -la /dev/shm/

# 6. Unix Domain Sockets
ls -la /var/run/*.sock 2>/dev/null
ls -la /tmp/*.sock 2>/dev/null
```

**Frage:** Welche IPC-Ressourcen sind aktuell auf deinem System aktiv?

_Dein Antwort:_

<br><br>

---

## Teil 6: Signale

### Aufgabe 6.1: Signale senden (Linux)

```bash
# 1. Alle verfügbaren Signale anzeigen
kill -l

# 2. Hintergrundprozess starten
sleep 300 &
PID=$!
echo "Gestartet mit PID: $PID"

# 3. SIGSTOP senden (Prozess anhalten)
kill -SIGSTOP $PID
ps -o pid,stat,comm -p $PID   # Status sollte 'T' (Stopped) sein

# 4. SIGCONT senden (Prozess fortsetzen)
kill -SIGCONT $PID
ps -o pid,stat,comm -p $PID   # Status sollte wieder 'S' sein

# 5. SIGTERM senden (höflich beenden)
kill -SIGTERM $PID

# 6. Falls SIGTERM nicht wirkt: SIGKILL (brutal beenden)
# kill -SIGKILL $PID   # oder: kill -9 $PID
```

**Wichtige Signale:**

| Signal | Nummer | Beschreibung |
|--------|--------|--------------|
| SIGHUP | 1 | Terminal geschlossen (Hangup) |
| SIGINT | 2 | Interrupt (Ctrl+C) |
| SIGKILL | 9 | Sofort beenden (nicht abfangbar!) |
| SIGTERM | 15 | Höflich beenden (Standard) |
| SIGSTOP | 19 | Anhalten (nicht abfangbar!) |
| SIGCONT | 18 | Fortsetzen |

---

## Zusammenfassung: Wichtige Kommandos

### Linux

| Kommando | Beschreibung |
|----------|--------------|
| `ps aux` | Alle Prozesse anzeigen |
| `ps -T -p <PID>` | Threads eines Prozesses |
| `top` / `htop` | Interaktive Prozessüberwachung |
| `pstree` | Prozessbaum |
| `kill -<SIGNAL> <PID>` | Signal senden |
| `nice -n <WERT> <CMD>` | Prozess mit Priorität starten |
| `renice -n <WERT> -p <PID>` | Priorität ändern |
| `ipcs` | IPC-Ressourcen anzeigen |
| `cat /proc/<PID>/...` | Prozessdetails |

### Windows PowerShell

| Kommando | Beschreibung |
|----------|--------------|
| `Get-Process` | Alle Prozesse |
| `Stop-Process -Id <PID>` | Prozess beenden |
| `Start-Process -Priority <P>` | Mit Priorität starten |
| `Get-Process | Sort-Object CPU` | Nach CPU sortieren |

---

## Quellen

- [[01-Prozessmodell|Prozessmodell]]
- [[02-Scheduling|Scheduling]]
- [[03-Threads|Threads]]
- [[04-Interprozesskommunikation|IPC]]
- Linux man-pages: `man ps`, `man kill`, `man nice`
