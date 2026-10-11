---
author: Andreas Hümmer
title: Adressräume
tags:
  - content
  - bs
  - speicher
  - adressraum
  - mmu
  - allokierung
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Adressräume

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Den Unterschied zwischen physischer und logischer Adresse kennen
> - Die Aufgaben der Speicherverwaltung verstehen
> - Die Funktion der MMU (Memory Management Unit) erklären können
> - Die typische Aufteilung eines Adressraums kennen
> - Belegungsstrategien (First-Fit, Best-Fit, etc.) unterscheiden können

---

## Überblick

Die Speicherverwaltung gehört zu den fundamentalsten Aufgaben eines Betriebssystems. Sie bildet die Brücke zwischen dem, was ein Programm „sieht" – seinen eigenen, privaten Adressraum – und der physischen Realität des begrenzten Hauptspeichers, den sich alle laufenden Prozesse teilen müssen.

Frühe Computer kannten nur einen Prozess zur Zeit: Das gesamte Programm wurde in den Speicher geladen, lief ab, und erst dann konnte das nächste starten. Mit dem Aufkommen von Multitasking-Systemen in den 1960er Jahren wurde die Speicherverwaltung zur Schlüsselkomponente: Mehrere Programme mussten gleichzeitig im Speicher residieren, voneinander isoliert und doch flexibel adressierbar.

Die moderne Lösung – **virtuelle Adressräume** – gibt jedem Prozess die Illusion, den gesamten Speicher für sich allein zu haben, während das Betriebssystem hinter den Kulissen die physischen Ressourcen verteilt, schützt und bei Bedarf auf die Festplatte auslagert.

---

## Definition

> [!quote] **Formale Definition**
> Ein **Adressraum** ist der Bereich von Speicheradressen, die einem Prozess zur Verfügung stehen. Das Betriebssystem verwaltet die Zuteilung von Speicherbereichen im Hauptspeicher (RAM).

Ein Adressraum ist mehr als nur ein zusammenhängender Block von Bytes – er ist eine strukturierte Umgebung mit festgelegten Bereichen für Code, Daten und dynamischen Speicher. Diese Struktur ermöglicht es dem Betriebssystem, Zugriffsrechte differenziert zu vergeben und Programme voreinander zu schützen.

---

## Das fundamentale Problem

Ohne Speicherverwaltung ergeben sich zwei schwerwiegende Probleme:

1. **Adresskonflikte:** Wenn zwei Programme zur Laufzeit beide die Adresse 0x1000 verwenden, überschreiben sie sich gegenseitig.

2. **Fehlende Isolation:** Ein fehlerhaftes oder bösartiges Programm könnte den Speicher eines anderen Programms – oder sogar des Betriebssystems – lesen oder verändern.

Die Lösung ist die Trennung von **logischen** (virtuellen) und **physischen** Adressen. Das Programm arbeitet mit seinen eigenen, virtuellen Adressen, während die Hardware diese zur Laufzeit in tatsächliche RAM-Adressen übersetzt.

---

## Aufgaben der Speicherverwaltung

Die Speicherverwaltung eines Betriebssystems erfüllt drei zentrale Aufgaben, die zusammenwirken, um den physischen Speicher effizient und sicher zu nutzen:

| Aufgabe | Beschreibung |
|---------|--------------|
| **1. Adressmapping** | Logische Adressen → Physikalische Adressen; Seiten (Pages) → Bereiche im Hauptspeicher |
| **2. Belegungsstrategie** | In welcher Lücke soll Speicher reserviert werden? Minimierung von Fragmentierung |
| **3. Ersetzungsstrategie** | Welcher Speicherbereich kann sinnvoll ausgelagert werden? |

### 1. Adressmapping (Adressübersetzung)

Die MMU übersetzt jede logische Adresse, die ein Programm verwendet, in die entsprechende physische Adresse im RAM. Dieser Vorgang erfolgt bei jedem Speicherzugriff – Milliarden Mal pro Sekunde – und muss daher in Hardware implementiert sein.

### 2. Belegungsstrategie (Allocation Policy)

Wenn ein Prozess Speicher anfordert, muss das Betriebssystem entscheiden, welcher freie Bereich verwendet wird. Die Wahl beeinflusst die Fragmentierung: Schlechte Entscheidungen führen dazu, dass freier Speicher in kleine, unnutzbare Stücke zerfällt.

### 3. Ersetzungsstrategie (Replacement Policy)

Wenn der physische Speicher voll ist, muss das Betriebssystem entscheiden, welche Daten auf die Festplatte ausgelagert werden. Die Strategie sollte Daten auslagern, die wahrscheinlich nicht bald wieder benötigt werden – denn ein Nachladen von der Festplatte dauert Millionen von CPU-Zyklen.

---

## Speicherallokierung

> [!quote] **Definition**
> Das **Reservieren von Speicherbereichen** im Hauptspeicher durch das Betriebssystem nennt man **Allokieren** (englisch: allocation).

### Grundlegende Eigenschaften

Die Speicherallokierung folgt mehreren wichtigen Prinzipien:

| Eigenschaft | Beschreibung |
|-------------|--------------|
| **Zuteilung bei Bedarf** | Speicher wird allokiert, wenn ein Prozess startet oder dynamisch mehr Speicher anfordert |
| **Nicht-Kontiguität** | Die Speicherbereiche eines Prozesses müssen nicht zusammenhängend im RAM liegen |
| **Isolation** | Jeder Prozess sieht nur seinen eigenen Adressraum; fremde Bereiche sind unsichtbar |
| **Dynamische Anpassung** | Heap und Stack können zur Laufzeit wachsen und schrumpfen |

### Speicherbelegung im Arbeitsspeicher

Das folgende Diagramm zeigt eine typische Momentaufnahme des physischen Speichers mit mehreren geladenen Programmen und den entstehenden Lücken:

![[02-05-01-arbeitsspeicher-belegung.png]]
*<span class="fig-id">02-05-01-arbeitsspeicher-belegung</span>: Typische Belegung des Arbeitsspeichers: Das Betriebssystem residiert am Anfang des Speichers (niedrige Adressen), gefolgt von verschiedenen Anwendungsprogrammen. Durch das Starten und Beenden von Prozessen entstehen Lücken unterschiedlicher Größe – die sogenannte externe Fragmentierung.*

### Externe vs. Interne Fragmentierung

Bei der Speicherverwaltung unterscheidet man zwei Arten von Fragmentierung:

| Art | Beschreibung | Beispiel |
|-----|--------------|----------|
| **Externe Fragmentierung** | Freier Speicher ist in viele kleine Lücken verteilt, sodass eine große Anforderung nicht erfüllt werden kann, obwohl insgesamt genug Speicher frei wäre | 100 KB frei in 10 × 10-KB-Lücken, aber 50 KB am Stück benötigt |
| **Interne Fragmentierung** | Zugewiesene Blöcke sind größer als angefordert; der Überschuss bleibt ungenutzt | Prozess fordert 3 KB an, bekommt 4-KB-Block zugeteilt (1 KB verschwendet) |

> [!tip] **Lösung für externe Fragmentierung**
> **Paging** eliminiert externe Fragmentierung vollständig, indem es Speicher in gleich große Blöcke (Pages) aufteilt. Jede Anforderung wird auf volle Pages aufgerundet, was nur noch interne Fragmentierung (maximal eine Page pro Prozess) verursacht.

---

## Physische vs. Logische Adresse

Der Unterschied zwischen physischen und logischen Adressen ist das Herzstück der modernen Speicherverwaltung:

![[02-05-01-adressumrechnung.png]]
*<span class="fig-id">02-05-01-adressumrechnung</span>: Die Adressumrechnung durch die MMU: Das Programm arbeitet mit logischen (virtuellen) Adressen, die MMU übersetzt diese transparent in physische Adressen. Der Prozess „sieht" seinen Adressraum ab 0, während seine Daten tatsächlich an ganz anderen Stellen im physischen Speicher liegen können.*

| Adresstyp | Beschreibung | Eigenschaften |
|-----------|--------------|---------------|
| **Physische Adresse** | Reale Adresse einer Speicherzelle im RAM | Eindeutig, direkt am Adressbus anliegend, vom BS verwaltet |
| **Logische Adresse** | Virtuelle Adresse aus Sicht des Programms | Beginnt bei 0, prozessspezifisch, wird durch MMU übersetzt |

### Warum diese Trennung?

Die Trennung bietet mehrere fundamentale Vorteile:

1. **Relokation:** Programme können an beliebiger Stelle im physischen Speicher geladen werden – ihre logischen Adressen bleiben gleich.

2. **Schutz:** Ohne gültige Zuordnung in der Page Table kann ein Prozess eine Adresse gar nicht erst ansprechen – der Zugriff scheitert in der Hardware.

3. **Sharing:** Derselbe physische Speicherbereich (z.B. eine Shared Library) kann in mehreren virtuellen Adressräumen erscheinen.

4. **Virtueller Speicher:** Der logische Adressraum kann größer sein als der physische Speicher – das Betriebssystem lagert bei Bedarf aus.

### Die MMU (Memory Management Unit)

Die **MMU** ist eine Hardware-Komponente (meist in der CPU integriert), die bei jedem Speicherzugriff die Adressübersetzung durchführt:

| Aufgabe | Beschreibung |
|---------|--------------|
| **Adressübersetzung** | Wandelt logische Adressen in physische um (via Page Table, TLB) |
| **Speicherschutz** | Prüft Zugriffsrechte (Read, Write, Execute) |
| **Trap-Auslösung** | Generiert Page Fault bei ungültigen Zugriffen |

> [!info] **Historischer Hintergrund**
> Frühe Systeme wie der Intel 8086 hatten keine echte MMU – Programme nutzten direkt physische Adressen. Erst mit dem 80286 (1982) und vollständig mit dem 80386 (1985) wurde Paging und damit echte Speichervirtualisierung möglich.

---

## Belegungsstrategien

Durch ständiges Allokieren und Freigeben von Speicher entstehen Lücken unterschiedlicher Größe. Wenn ein neuer Speicherbereich benötigt wird, muss das Betriebssystem entscheiden, welche Lücke verwendet wird.

> [!example] **Beispiel: Anforderung von 15 KB**
> 
> | Lücke | Größe | First-Fit | Best-Fit | Worst-Fit |
> |-------|-------|:---------:|:--------:|:---------:|
> | Lücke 1 | 20 KB | ✅ gewählt | | |
> | Lücke 2 | 15 KB | | ✅ gewählt | |
> | Lücke 3 | 30 KB | | | ✅ gewählt |

### Übersicht der Strategien

| Strategie | Algorithmus | Vorteile | Nachteile |
|-----------|-------------|----------|-----------|
| **First-Fit** | Erste passende Lücke von Anfang an | Schnell (O(n) worst case, oft O(1)) | Fragmentierung am Speicheranfang |
| **Next-Fit** | Erste passende Lücke ab letzter Position | Verteilt Fragmentierung gleichmäßiger | Zyklische Durchsuchung nötig |
| **Best-Fit** | Kleinste passende Lücke | Minimale Verschwendung bei großen Lücken | Langsam (O(n)), erzeugt viele kleine Reste |
| **Worst-Fit** | Größte verfügbare Lücke | Große Reste bleiben nutzbar | Langsam, verschwendet große zusammenhängende Bereiche |

### Welche Strategie ist die beste?

In der Praxis hat sich **First-Fit** als guter Kompromiss erwiesen:
- Schnell in der Ausführung
- Erzeugt ähnliche Fragmentierung wie Best-Fit
- Einfach zu implementieren

**Best-Fit** klingt optimal, erzeugt aber paradoxerweise oft mehr Fragmentierung, weil es viele winzige Restlücken hinterlässt, die für nichts mehr verwendbar sind.

> [!example] **Analogie: Parkplatzsuche**
> - **First-Fit:** Nimm den ersten Parkplatz, der frei ist
> - **Best-Fit:** Fahre den ganzen Parkplatz ab, um die kleinste passende Lücke zu finden
> - **Worst-Fit:** Parke immer in der größten Lücke (damit noch Platz für andere bleibt)

---

## Speicherschutz

> [!danger] **Kernprinzip**
> Es muss **unmöglich** sein, dass ein Prozess auf den Speicherbereich eines anderen Prozesses zugreift – weder lesend noch schreibend. Dieses Prinzip heißt **Memory Protection**.

Der Speicherschutz ist eine der wichtigsten Sicherheitsfunktionen eines Betriebssystems. Ohne ihn könnte ein fehlerhaftes oder bösartiges Programm:
- Daten anderer Programme auslesen (Passwörter, Kreditkartennummern)
- Code anderer Programme manipulieren (Malware-Injektion)
- Das Betriebssystem selbst beschädigen (Systemabsturz)

### Mechanismen des Speicherschutzes

![[02-05-01-speicherschutz-grenzregister.png]]
*<span class="fig-id">02-05-01-speicherschutz-grenzregister</span>: Speicherschutz mit Grenzregistern: Bei jedem Speicherzugriff prüft die Hardware, ob die angeforderte Adresse innerhalb des erlaubten Bereichs liegt (Base ≤ Adresse < Base + Limit). Liegt sie außerhalb, wird ein Trap ausgelöst.*

### Base- und Limit-Register

Das einfachste Schutzkonzept verwendet zwei spezielle Register:

| Register | Funktion |
|----------|----------|
| **Base Register** | Enthält die Startadresse des erlaubten Speicherbereichs |
| **Limit Register** | Enthält die Größe des erlaubten Bereichs |

Bei jedem Speicherzugriff prüft die Hardware:
```
Wenn (Adresse >= Base) UND (Adresse < Base + Limit):
    Zugriff erlaubt
Sonst:
    Trap auslösen → Betriebssystem übernimmt (Segmentation Fault)
```

### Moderne Schutzmechanismen

In modernen Systemen mit Paging wird der Schutz über die **Page Table** realisiert:

| Mechanismus | Funktion |
|-------------|----------|
| **Valid Bit** | Zeigt an, ob die Page überhaupt zugeordnet ist |
| **Protection Bits** | Read (R), Write (W), Execute (X) Rechte pro Page |
| **User/Supervisor Bit** | Unterscheidet User-Mode und Kernel-Mode Zugriffe |
| **No-Execute (NX)** | Verhindert Code-Ausführung in Datenbereichen (gegen Buffer-Overflow-Angriffe) |

---

## Typischer Adressraum eines Prozesses

Jeder Prozess erhält einen eigenen virtuellen Adressraum mit einer festgelegten Struktur. Diese Aufteilung ist historisch gewachsen und findet sich in ähnlicher Form auf allen Unix-artigen Systemen:

![[02-05-01-prozess-adressraum.png]]
*<span class="fig-id">02-05-01-prozess-adressraum</span>: Typischer Aufbau eines Prozess-Adressraums: Stack und Heap wachsen aufeinander zu und teilen sich den verfügbaren Platz dynamisch. Die Segmente Text, Data und BSS haben feste Größen, die beim Programmstart bekannt sind.*

### Die Segmente im Detail

| Segment | Inhalt | Eigenschaften |
|---------|--------|---------------|
| **Text** | Programmcode (Maschinencode) | Read-only, Execute, kann zwischen Prozessen geteilt werden |
| **Data** | Initialisierte globale und statische Variablen | Read/Write, Größe bei Programmstart bekannt |
| **BSS** | Uninitialisierte globale und statische Variablen | Read/Write, wird mit Nullen initialisiert |
| **Heap** | Dynamisch allokierter Speicher (`malloc`, `new`) | Read/Write, wächst nach oben (steigende Adressen) |
| **Stack** | Lokale Variablen, Rücksprungadressen, Parameter | Read/Write, wächst nach unten (fallende Adressen) |

> [!info] **Warum wachsen Heap und Stack gegeneinander?**
> Dieses Design erlaubt maximale Flexibilität: Beide können den verfügbaren Platz in der Mitte nutzen, ohne dass bei Programmstart festgelegt werden muss, wie viel jeder braucht. Erst wenn sie sich treffen, ist der Speicher wirklich erschöpft.

### Stack vs. Heap

| Eigenschaft | Stack | Heap |
|-------------|-------|------|
| **Allokation** | Automatisch (bei Funktionsaufruf) | Manuell (`malloc`, `new`) |
| **Deallokation** | Automatisch (bei Rückkehr) | Manuell (`free`, `delete`) |
| **Geschwindigkeit** | Sehr schnell (nur Pointer verschieben) | Langsamer (Verwaltungsstruktur) |
| **Größe** | Begrenzt (typisch 1-8 MB) | Nur durch RAM/Swap begrenzt |
| **Fragmentierung** | Keine | Möglich |
| **Fehlertypen** | Stack Overflow | Memory Leak, Use-after-free |

---

## Speichergrößen – Historischer Überblick

Die Entwicklung der Speichergrößen zeigt den exponentiellen Fortschritt der Computertechnik:

| System / Ära | Typischer Speicher | Adressbreite |
|--------------|-------------------|--------------|
| Commodore 64 (1982) | 64 KB | 16 Bit |
| Arduino (ATMEL) | 2 KB – 256 KB | 8-16 Bit |
| IBM PC/XT (1983) | 512 KB – 640 KB | 20 Bit (Real Mode) |
| 80386 (1985) | 1 – 16 MB | 32 Bit |
| 32-Bit System (max.) | 4 GB (2³²) | 32 Bit |
| Smartphone (heute) | 4 – 16 GB | 64 Bit |
| Desktop (heute) | 16 – 128 GB | 64 Bit |
| Server (heute) | 256 GB – 12 TB | 64 Bit |
| 64-Bit (theoretisch) | 16 Exabyte (2⁶⁴) | 64 Bit |

> [!note] **Die 640-KB-Grenze**
> Die berühmte Grenze von 640 KB beim IBM PC entstand durch das Design von MS-DOS: Der Bereich oberhalb war für ROM-BIOS und Grafikkarten reserviert. Bill Gates' angebliches Zitat „640K ought to be enough for anybody" ist übrigens erfunden – er hat das nie gesagt.

---

## Praktische Werkzeuge

### Linux-Kommandos zur Speicheranalyse

| Kommando | Beschreibung |
|----------|--------------|
| `free -h` | Zeigt RAM- und Swap-Nutzung |
| `cat /proc/meminfo` | Detaillierte Speicherinformationen |
| `cat /proc/<PID>/maps` | Speicher-Layout eines Prozesses |
| `cat /proc/<PID>/status` | Speicherverbrauch eines Prozesses |
| `pmap <PID>` | Detaillierte Memory-Map eines Prozesses |
| `top` / `htop` | Interaktive Prozess- und Speicherübersicht |
| `vmstat` | Statistiken zu virtuellem Speicher |

```bash
# Beispiel: Speicher-Layout von Prozess 1234 anzeigen
$ cat /proc/1234/maps | head -10
00400000-00452000 r-xp 00000000 08:01 123456  /usr/bin/programm  # Text
00651000-00652000 r--p 00051000 08:01 123456  /usr/bin/programm  # Data
00652000-00653000 rw-p 00052000 08:01 123456  /usr/bin/programm  # Data
01234000-01345000 rw-p 00000000 00:00 0       [heap]
7fff12340000-7fff12361000 rw-p 00000000 00:00 0 [stack]
```

### Windows-Werkzeuge

| Werkzeug | Beschreibung |
|----------|--------------|
| Task-Manager | Grundlegende Speicherübersicht |
| Ressourcenmonitor | Detaillierte Speichernutzung |
| VMMap (Sysinternals) | Visualisierung des Adressraums |
| Process Explorer | Erweiterte Prozessansicht |

---

## Zusammenhänge

- [[02-Virtueller-Speicher|Virtueller Speicher]] → Erweiterung des Adressraums auf Festplatte
- [[03-Paging|Paging]] → Speicheraufteilung in gleich große Pages
- [[04-Segmentierung|Segmentierung]] → Alternative logische Speicherorganisation
- [[01-Prozessmodell|Prozessmodell]] → Speicherlayout eines Prozesses

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied physische vs. logische Adresse
> - Die drei Aufgaben der Speicherverwaltung
> - Belegungsstrategien (First-Fit, Best-Fit, Worst-Fit) – Vor- und Nachteile
> - Funktion der MMU und Adressübersetzung
> - Aufbau des Prozess-Adressraums (Text, Data, BSS, Heap, Stack)


> [!question] **Häufige Prüfungsfragen**
> 1. Was ist der Unterschied zwischen physischer und logischer Adresse?
> 2. Erklären Sie die Funktion der MMU!
> 3. Vergleichen Sie die Belegungsstrategien First-Fit und Best-Fit!
> 4. Wie wird der Speicherschutz zwischen Prozessen gewährleistet?
> 5. Was versteht man unter Fragmentierung? Unterscheiden Sie externe und interne Fragmentierung!
> 6. Skizzieren Sie den typischen Adressraum eines Prozesses und erklären Sie die einzelnen Segmente!
> 7. Warum wachsen Heap und Stack in entgegengesetzte Richtungen?

> [!tip] **Merkhilfen**
> - **First-Fit** = „Erste freie Parklücke nehmen"
> - **Best-Fit** = „Perfekt passende Parklücke suchen" (aber viele kleine Reste!)
> - **Worst-Fit** = „Größte Parklücke nehmen"
> - **MMU** = „Übersetzer" zwischen virtueller und physischer Welt
> - **Base + Limit** = „Anfang und Länge" des erlaubten Bereichs
> - **TDBHS** = Text, Data, BSS, Heap, Stack (von unten nach oben)

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
>
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Memory Access](https://www.youtube.com/watch?v=A9WLYbE0p-I) | Grundlagen der Speicheradressierung und Zugriff |
> | 🎬 | [CoreDumped – Stack](https://www.youtube.com/watch?v=N3o5yHYLviQ) | Stack-Speicher: Aufbau und Funktionsweise |
> | 🎬 | [CoreDumped – Heap](https://www.youtube.com/watch?v=ioJkA7Mw2-U) | Heap-Speicher: Dynamische Allokation |

---

## Quellen
- Tanenbaum, A. S. & Bos, H.: Modern Operating Systems, 5th Edition, Kapitel 3
- Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts, 10th Edition, Kapitel 8-9
- Arpaci-Dusseau, R. & Arpaci-Dusseau, A.: Operating Systems: Three Easy Pieces (OSTEP), Kapitel 13-17

### Direkte Quellenreferenzen

**Tanenbaum, A. S. & Bos, H.: Modern Operating Systems (5th Edition)**
- Kapitel 3: Memory Management
  - 3.1 No Memory Abstraction (→ Historischer Kontext)
  - 3.2 A Memory Abstraction: Address Spaces (→ Adressräume)
    - 3.2.1 The Notion of an Address Space (→ Definition)
    - 3.2.2 Swapping (→ Ersetzungsstrategie)
    - 3.2.3 Managing Free Memory (→ Belegungsstrategien)
  - 3.3 Virtual Memory (→ Logische vs. physische Adressen)

**Silberschatz, A., Galvin, P. B. & Gagne, G.: Operating System Concepts (10th Edition)**
- Chapter 8: Main Memory
  - 8.1 Background (→ Adressräume, logische/physische Adressen)
    - 8.1.2 Address Binding (→ MMU)
    - 8.1.3 Logical Versus Physical Address Space
  - 8.2 Contiguous Memory Allocation
    - 8.2.1 Memory Protection (→ Speicherschutz, Base/Limit)
    - 8.2.2 Memory Allocation (→ First-Fit, Best-Fit, Worst-Fit)
    - 8.2.3 Fragmentation (→ Externe/Interne Fragmentierung)
