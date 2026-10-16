# Abbildungsverzeichnis

> Dieses Verzeichnis enthält alle Abbildungen der bisher fertiggestellten Kapitel: **02-Betriebssysteme / 01-Einführung**, **02-Betriebssysteme / 02-Architektur**, **02-Betriebssysteme / 03-Prozesse**, **02-Betriebssysteme / 05-Speicherverwaltung**, **02-Betriebssysteme / 06-Ein-Ausgabe**, **02-Betriebssysteme / 07-Dateisysteme** und **03-Rechnernetze / 03-Referenzmodelle**.

> [!note] Urheberrecht
> Alle Grafiken, soweit nicht anders gekennzeichnet, sind selbst erstellt.
> © Andreas Hümmer

---

## 02-Betriebssysteme / 01-Einführung

### 01-Historie (02-01-01)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-01-01-industrielle-revolution | Fabrikhalle im 19. Jahrhundert - Beginn der Automatisierung |
| 02-01-01-jacquard-webstuhl-lochkarten | Jacquard-Webstuhl (1805) - Lochkarten zur Mustersteuerung |
| 02-01-01-babbage-analytical-engine | Modell der Analytical Engine von Charles Babbage |
| 02-01-01-hollerith-tabelliermaschine | Hollerith-Tabelliermaschine (ca. 1890) |
| 02-01-01-hollerith-lochkarte | Hollerith-Lochkarte - Datenträger für die US-Volkszählung 1890 |
| 02-01-01-zuse-z3-deutsches-museum | Nachbau der Zuse Z3 im Deutschen Museum München |
| 02-01-01-colossus | Colossus Mark 2 in Bletchley Park, bedient von "Wrens" |
| 02-01-01-eniac | ENIAC in der Moore School of Electrical Engineering |
| 02-01-01-eniac-programmiererinnen | ENIAC-Programmiererinnen bei der Verkabelung - Die "ENIAC Six" |
| 02-01-01-harvard-mark-i | Harvard Mark I (ASCC) - Elektromechanischer Großrechner |
| 02-01-01-ibm-7094 | IBM 7094 Konsole - Transistorisierter Großrechner der 2. Generation |
| 02-01-01-lochkarten-sortiert | Lochkarten-Stapel sortiert in Ablagefächern |
| 02-01-01-papertape-archiv | Lochstreifen-Archiv (Papertape) - Alternative zu Lochkarten |
| 02-01-01-batch-speicher-layout | Speicheraufteilung im Batch-Betrieb |
| 02-01-01-hardware-interrupt-ablauf | Hardware-Interrupt-Ablauf: CPU und Gerät arbeiten asynchron |
| 02-01-01-polling-vs-interrupts | Polling vs. Interrupts - Vergleich der Abfragemethoden |
| 02-01-01-spooling-architektur | Spooling: Pufferung langsamer Geräte über schnellen Zwischenspeicher |
| 02-01-01-ibm-system360-mainframe | IBM System/360 - Die erste kompatible Rechnerfamilie |
| 02-01-01-uniprogramming-auslastung | Uniprogramming: Ein Job blockiert die CPU während I/O-Wartezeiten |
| 02-01-01-multiprogramming-auslastung | Multiprogramming: Mehrere Jobs teilen sich die CPU |
| 02-01-01-time-sharing-prinzip | Time-Sharing: CPU wechselt per Timer zwischen Benutzern |
| 02-01-01-time-sharing-detail | Time-Sharing-System mit Terminal-Konzentrator und Mainframe |
| 02-01-01-dec-pdp-1 | DEC PDP-1 (1960) - Einer der ersten kommerziellen Minicomputer |
| 02-01-01-dec-pdp-11 | DEC PDP-11 (1970) - Der einflussreichste Minicomputer |
| 02-01-01-xerox-alto-maus-1973 | Xerox Alto (1973) - Erster PC mit GUI und Maus |
| 02-01-01-ibm-pc-xt-1983 | IBM PC XT (1983) - Erweitertes Modell mit Festplatte |
| 02-01-01-commodore-c64 | Commodore 64 (1982) - Der meistverkaufte Heimcomputer |
| 02-01-01-zx-spectrum | Sinclair ZX Spectrum (1982) - Populärer britischer Heimcomputer |
| 02-01-01-apple-macintosh-1984 | Apple Macintosh 128K (1984) - Popularisierte die GUI |
| 02-01-01-frueh-pc-terminal | Frühe PC-Workstation - Zielplattform für Linux |
| 02-01-01-virtualisierung-container | Virtuelle Maschinen vs. Container - Unterschiede im Aufbau |
| 02-01-01-programmausfuehrung-evolution | Evolution der Programmausführung: 1:1 → Batch → Time-Sharing |

### 02-Definition (02-01-02)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-01-02-schichtenarchitektur | Betriebssystem als Schichtenstapel zwischen Anwendungen und Hardware |
| 02-01-02-smartcard | Smartcard mit sichtbarem Chip-Modul und Kontaktflächen |
| 02-01-02-smartcard-kontakte | Kontaktbelegung des Chip-Moduls nach ISO 7816-2 |
| 02-01-02-smartcard-chip-aufbau | Interner Aufbau des Smartcard-Chips (CPU, RAM, EEPROM, Krypto) |
| 02-01-02-DELL-EMC-Poweredge-R640-8dell-poweredge-server-offen | Dell PowerEdge Server - Ansicht mit geöffnetem Gehäuse |
| 02-01-02-rack-server-betriebssysteme | Schematische Darstellung: Mehrere Betriebssysteme in einem Server |

### 03-Aufgaben (02-01-03)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-01-03-bs-schnittstelle | Betriebssystem zwischen Anwendungen und Hardware |
| 02-01-03-bs-zwei-sichtweisen | Top-Down vs. Bottom-Up-Sicht auf das Betriebssystem |

---

## 02-Betriebssysteme / 02-Architektur

### 01-Kerneltypen (02-02-01)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-02-01-monolithischer-kernel | Monolithischer Kernel: Alle Dienste im Kernel-Space |
| 02-02-01-linux-lkm | Linux mit Loadable Kernel Modules (LKM) |
| 02-02-01-mikrokernel | Mikrokernel: Minimaler Kern, Server-Prozesse im User-Space |
| 02-02-01-mikrokernel-message-passing | IPC via Message Passing im Mikrokernel |
| 02-02-01-hybridkernel-windows-nt | Windows NT Hybridkernel-Architektur |
| 02-02-01-hybridkernel-macos-xnu | macOS XNU-Kernel: BSD Layer + I/O Kit + Mach |
| 02-02-01-exokernel | Exokernel mit Library Operating System (libOS) |
| 02-02-01-unikernel | Unikernel: Anwendung + minimale Kernelkomponenten |

### 02-Schichtenmodell (02-02-02)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-02-02-schichtenprinzip | Grundidee der Schichtung: Schicht N nutzt nur Schicht N-1 |
| 02-02-02-sechs-schichten-modell | 6-Schichten-Modell von Hardware bis Anwendung |
| 02-02-02-cpu-protection-rings | CPU-Schutzringe (Ring 0–3) als Privilegstufen |
| 02-02-02-ring-wechsel-mode-switch | Mode Switch zwischen User Mode und Kernel Mode |
| 02-02-02-unix-linux-architektur | Unix/Linux-Architektur mit Subsystemen |
| 02-02-02-virtual-file-system | VFS: Einheitliche Dateisystem-Schnittstelle |
| 02-02-02-windows-nt-architektur | Windows NT Schichtenarchitektur |
| 02-02-02-strenge-vs-relaxierte-schichtung | Strenge vs. relaxierte Schichtung |

### 03-Systemaufrufe (02-02-03)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-02-03-syscall-schnittstelle | Systemaufruf-Weg von Anwendung bis Kernel |
| 02-02-03-syscall-ablauf-detail | Detaillierter Ablauf eines Systemaufrufs (8 Stationen) |
| 02-02-03-syscall-fork-exec-shell | Shell führt Kommando aus: fork() → exec() → wait() |
| 02-02-03-file-descriptor-tabelle | Filedeskriptor-Tabelle eines Prozesses |
| 02-02-03-prozess-adressraum | Adressraum eines Prozesses (Text, Data, Heap, Stack) |
| 02-02-03-fork-copy-on-write | Copy-on-Write bei fork() |
| 02-02-03-open-file-table | File Descriptor → Open File Table → Inode |
| 02-02-03-libc-wrapper | libc als Wrapper: printf() → write() → sys_write() |
| 02-02-03-vdso-schnelle-syscalls | vDSO für schnelle Syscalls ohne Kontextwechsel |

### 04-Von-Neumann-vs-Harvard (02-02-04)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-02-04-von-neumann-vs-harvard-ueberblick | Von-Neumann vs. Harvard-Architektur im Überblick |
| 02-02-04-von-neumann-detail | Von-Neumann-Architektur im Detail |
| 02-02-04-von-neumann-befehlszyklus | Befehlszyklus: Fetch → Decode → Execute → Write Back |
| 02-02-04-harvard-detail | Harvard-Architektur mit getrennten Speicherpfaden |
| 02-02-04-modified-harvard | Modified Harvard: Getrennte L1-Caches, gemeinsamer Speicher |

### 06-CPU-Architekturen (02-02-06)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-02-06-intel-8088-pinout | Intel 8088 Pinbelegung im DIP-40-Gehäuse |
| 02-02-06-intel-8088-blockdiagramm | Intel 8088: Execution Unit und Bus Interface Unit |
| 02-02-06-intel-80286-blockdiagramm | Intel 80286 mit Protection Unit (Protected Mode) |
| 02-02-06-intel-80386-blockdiagramm | Intel 80386: Erster 32-Bit-x86, Paging Unit |
| 02-02-06-intel-80486-blockdiagramm | Intel 80486: On-Chip Cache, FPU und 5-stufige Pipeline |
| 02-02-06-intel-pentium-blockdiagramm | Intel Pentium: Erster superskalarer x86 (U-Pipe/V-Pipe) |
| 02-02-06-intel-p6-mikroarchitektur | P6-Mikroarchitektur: Out-of-Order, µOps, Register Renaming |
| 02-02-06-amd-k7-blockdiagramm | AMD K7/Athlon: 64-KB-L1-Cache, getrennte Scheduler |
| 02-02-06-amd64-register-layout | AMD64 Register-Layout: RAX enthält EAX, AX, AH, AL |
| 02-02-06-intel-core2duo-blockdiagramm | Intel Core 2 Duo: Zwei Kerne mit gemeinsamem L2-Cache |
| 02-02-06-amd-zen3-ccx | Zen 3 Core Complex: 8 Kerne, unified 32 MB L3, Infinity Fabric |
| 02-02-06-amd-zen3-kern | Zen 3 Kern: Frontend, Execution, Load/Store |
| 02-02-06-amd-chiplet-architektur | AMD Chiplet-Architektur: CCDs + I/O Die (Ryzen 9 5950X) |

---

## 02-Betriebssysteme / 03-Prozesse

### 01-Prozessmodell (02-03-01)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-03-01-programm-vs-prozess | Programm vs. Prozess: Vom Quellcode zur Ausführung |
| 02-03-01-prozesszustaende | Prozesszustände: neu, bereit, laufend, wartend, terminiert |
| 02-03-01-kontextwechsel | Kontextwechsel zwischen Prozess A und B |
| 02-03-01-pcb-aufbau | Aufbau des Process Control Blocks (PCB) |
| 02-03-01-dispatcher-ablauf | Dispatcher-Ablauf beim Prozesswechsel |
| 02-03-01-prozess-adressraum | Adressraumlayout: Text, Data, Heap, Stack |
| 02-03-01-fork-exec | fork() und exec() zur Prozesserzeugung |
| 02-03-01-fork-copy-on-write | Copy-on-Write bei fork() |
| 02-03-01-interrupt-swimlane | Interrupt-Ablauf: CPU, Hardware, Kernel |
| 02-03-01-timer-interrupt | Timer-Interrupt und Time-Quantum |
| 02-03-01-process-hierarchy | Prozesshierarchie: init/systemd und Kindprozesse |
| 02-03-01-zombie-process | Zombie-Prozess: Kind terminiert, Eltern wartet nicht |
| 02-03-01-prozess-synchronisation | Prozess-Synchronisation und kritische Abschnitte |

### 02-Scheduling (02-03-02)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-03-02-scheduler-overview | Scheduler-Übersicht mit Warteschlange und Zuständen |
| 02-03-02-fcfs-example | FCFS-Scheduling: First-Come-First-Served Beispiel |
| 02-03-02-round-robin-example | Round-Robin-Scheduling mit Zeitquantum |
| 02-03-02-sjf-example | Shortest-Job-First (SJF) Scheduling |
| 02-03-02-srtf-example | Shortest-Remaining-Time-First (SRTF) Scheduling |
| 02-03-02-mlfq | Multi-Level Feedback Queue (MLFQ) |

### 03-Threads (02-03-03)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-03-03-process-threads-context | Threads innerhalb eines Prozesses: Gemeinsame Daten, eigene Stacks |
| 02-03-03-user-level-threads | User-Level Threads: Kernel sieht nur einen Thread |
| 02-03-03-kernel-level-threads | Kernel-Level Threads: Jeder User-Thread hat Kernel-Thread |
| 02-03-03-threading-model-1to1 | 1:1 Threading-Modell: One-to-One |
| 02-03-03-threading-model-nto1 | N:1 Threading-Modell: Many-to-One |
| 02-03-03-threading-model-mton | M:N Threading-Modell: Many-to-Many |
| 02-03-03-thread-states | Thread-Zustandsübergänge |
| 02-03-03-multi-comparison | Multithreading vs. Multitasking vs. Multiprocessing |

### 04-Interprozesskommunikation (02-03-04)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-03-04-ipc-scenarios | Kommunikationsszenarien: Lokal (Single/Multi-CPU) und Netzwerk |
| 02-03-04-ipc-approaches | IPC-Grundansätze: Shared Memory vs. Message Passing |
| 02-03-04-ipc-pipe | Anonyme Pipe: Unidirektionaler Datenfluss |
| 02-03-04-ipc-message-queue | Message Queue: Mehrere Sender, strukturierte Nachrichten |
| 02-03-04-ipc-shared-memory | Shared Memory: Direkter Speicherzugriff |
| 02-03-04-ipc-sockets | Socket Client-Server: Verbindungsablauf |
| 02-03-04-ipc-signals | Signal: Prozess A sendet SIGTERM an Prozess B |
| 02-03-04-ipc-sync | Synchrone Kommunikation: Sender wartet |
| 02-03-04-ipc-async | Asynchrone Kommunikation: Sender arbeitet weiter |
| 02-03-04-ipc-decision | Entscheidungsbaum zur IPC-Mechanismus-Auswahl |

---

## 02-Betriebssysteme / 05-Speicherverwaltung

### 01-Adressräume (02-05-01)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-05-01-arbeitsspeicher-belegung | Typische Belegung des Arbeitsspeichers mit externer Fragmentierung |
| 02-05-01-adressumrechnung | Adressumrechnung durch die MMU: Logische → Physische Adressen |
| 02-05-01-speicherschutz-grenzregister | Speicherschutz mit Base- und Limit-Registern |
| 02-05-01-prozess-adressraum | Typischer Aufbau eines Prozess-Adressraums (Text, Data, BSS, Heap, Stack) |

### 02-Virtueller-Speicher (02-05-02)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-05-02-virtueller-speicher | Virtueller Speicher: Zusammenhängender Adressraum mit Swap-Auslagerung |
| 02-05-02-speicherhierarchie | Speicherhierarchie als Pyramide: Register → Cache → RAM → SSD → HDD |
| 02-05-02-swapping | Swapping: Ganze Prozesse zwischen RAM und Swap verschieben |
| 02-05-02-demand-paging | Demand Paging: Pages werden erst bei Zugriff geladen |
| 02-05-02-working-set | Working Set: Aktive Pages innerhalb eines Zeitfensters |

### 03-Paging (02-05-03)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-05-03-paging-konzept | Paging-Konzept: Pages → Frames über Page Table |
| 02-05-03-adressumrechnung | Adressumrechnung bei Paging: Page Number → Frame Number + Offset |
| 02-05-03-tlb | TLB-Ablauf: Hit liefert direkt, Miss konsultiert Page Table |
| 02-05-03-zweistufig | Zweistufige Page Table mit Page Directory |
| 02-05-03-x86-64-paging | x86-64 vierstufiges Paging (PML4 → PDP → PD → PT) |
| 02-05-03-clock-algorithmus | Clock-Algorithmus zur Seitenersetzung |

### 04-Segmentierung (02-05-04)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 05-04-01-segmentierung-konzept | Segmentierung: Logische Segmente → Physischer Speicher |
| 05-04-02-segmentierung-adressumrechnung | Adressumrechnung bei Segmentierung mit Grenzprüfung |
| 05-04-03-segmentierung-fragmentierung | Externe Fragmentierung und Lösung durch Kompaktierung |
| 05-04-04-segmentierung-paging | Kombinierte Adressumrechnung: Segmentierung mit Paging |

---

## 02-Betriebssysteme / 06-Ein-Ausgabe

### 01-IO-Grundlagen (02-06-01)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-06-01-io-controller | Aufbau eines I/O-Controllers mit seinen Registern |
| 02-06-01-polling-busy-waiting | Polling – CPU fragt wiederholt den Gerätestatus ab, bis es bereit ist |
| 02-06-01-interrupt-driven-io | Interrupt-gesteuertes I/O – CPU arbeitet weiter, bis das Gerät per Interrupt meldet |
| 02-06-01-dma-transfer | DMA – Daten werden ohne CPU-Beteiligung zwischen Gerät und RAM übertragen |
| 02-06-01-io-software-schichten | Die Schichten der I/O-Software von User-Space bis Hardware |
| 02-06-01-double-buffering | Double Buffering – zwei Puffer werden abwechselnd gefüllt und verarbeitet |
| 02-06-01-spooling | Spooling – Jobs werden in einer Warteschlange gesammelt und nacheinander abgearbeitet |

---

## 02-Betriebssysteme / 07-Dateisysteme

### 01-Historie-Festplatten (02-07-01)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-07-01-ibmramac305 | IBM RAMAC 305 (1956) – die erste kommerzielle Festplatte der Welt |
| 02-07-01-ibm3340 | IBM 3340 Winchester Festplatten (1973) – Grundlage aller modernen HDDs |
| 02-07-01-ibm-old-hdd | IBM-Festplatte aus der frühen PC-Ära |
| 02-07-01-shugart-sa1004 | Shugart SA1004 – 8-Zoll-Festplatte (1982) mit 10 MB Kapazität |
| 02-07-01-525inch-mfm-hdd | 5,25-Zoll MFM-Festplatte (Full Height) im Größenvergleich mit 2,5-Zoll-HDD |
| 02-07-01-quantum-bigfoot | Quantum Bigfoot – eine der letzten 5,25-Zoll-Festplatten (Half Height) |
| 02-07-01-35inch-hdd-closed | 3,5-Zoll-Desktop-Festplatte (geschlossen) mit PATA-Anschluss |
| 02-07-01-hdd-formfaktoren | Größenvergleich verschiedener HDD-Formfaktoren (5,25", 3,5", 2,5", PCMCIA) |
| 02-07-01-hdd-aufbau | Festplattenaufbau – Draufsicht und Seitenansicht mit Plattenstapel und Aktuator |
| 02-07-01-chs-adressierung | CHS-Adressierung – Zylinder, Köpfe und Sektoren |
| 02-07-01-hdd-zugriffszeit | Zugriffszeit einer HDD – Seek Time, Rotational Latency und Transfer Time |
| 02-07-01-storage-size-comparison | Evolution der Speichermedien – Größenvergleich HDD → SSD → microSD |
| 02-07-01-hdd-vs-ssd | HDD vs. SSD – mechanischer vs. elektronischer Speicher |
| 02-07-01-ssd-architektur | SSD-Architektur – Host, Controller mit FTL, und NAND Flash Chips |
| 02-07-01-ssd-formfaktoren | Moderne SSD-Formfaktoren – mSATA, M.2 SATA, M.2 NVMe |

### 02-Grundlagen (02-07-02)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-07-02-dateisystem-abstraktion | Die drei Abstraktionsebenen eines Dateisystems |
| 02-07-02-verzeichnis-evolution | Evolution der Verzeichnisstruktur – von flach bis zum azyklischen Graphen |
| 02-07-02-hard-vs-soft-links | Hard Links vs. Symbolic Links – zwei Wege zur gemeinsamen Dateinutzung |
| 02-07-02-open-file-tables | Drei-Ebenen-Struktur der Open File Tables |
| 02-07-02-unix-permissions | Aufbau der Unix-Dateiberechtigungen |
| 02-07-02-vfs | Das Virtual File System als einheitliche Abstraktionsschicht |
| 02-07-02-mount-concept | Vor und nach dem Mounten eines USB-Sticks |

### 03-Implementierung (02-07-03)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-07-03-disk-layout | Typische Aufteilung eines Speichermediums in funktionale Bereiche |
| 02-07-03-contiguous-alloc | Zusammenhängende Blockallokation – Dateien belegen aufeinanderfolgende Blöcke |
| 02-07-03-linked-alloc | Verkettete Blockallokation – jeder Block enthält Zeiger auf den nächsten |
| 02-07-03-fat-alloc | File Allocation Table – zentrale Tabelle im RAM mit Verkettungsinformationen |
| 02-07-03-inode-alloc | Inode-Struktur mit Direct Blocks und mehrstufiger Indirektion |
| 02-07-03-dir-linear | Verzeichnis als lineare Liste mit Name-Inode-Zuordnungen |
| 02-07-03-dir-hash | Verzeichnis mit Hash-Tabelle und Kollisionsbehandlung durch Verkettung |
| 02-07-03-bitmap-free | Bitmap-basierte Freispeicherverwaltung – ein Bit pro Block |
| 02-07-03-freelist | Verkettete Freispeicherliste – freie Blöcke zeigen auf den nächsten freien Block |
| 02-07-03-buffer-cache | Buffer Cache als Vermittler zwischen Anwendung und Festplatte |

### 04-Journaling (02-07-04)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 02-07-04-journaling-prinzip | Vergleich – ohne vs. mit Journaling bei einem Systemabsturz |
| 02-07-04-journal-transaktion | Ablauf einer Journal-Transaktion mit den 5 Phasen |
| 02-07-04-metadata-journaling | Metadata-Only Journaling – nur Metadaten werden geloggt |
| 02-07-04-ordered-mode | Ordered Mode – Reihenfolge garantiert: Daten vor Metadaten |
| 02-07-04-full-data-journaling | Full Data Journaling – alle Daten werden zweimal geschrieben |
| 02-07-04-crash-recovery | Ablauf der Crash Recovery nach einem Systemabsturz |
| 02-07-04-ext4-journal | Struktur des ext4 Journals (JBD2) als Ring Buffer |
| 02-07-04-copy-on-write | Vergleich von In-Place Update und Copy-on-Write |

---

**Gesamtzahl der Abbildungen:** 204

| Kapitel | Anzahl |
|---------|--------|
| 02-01-01 Historie | 32 |
| 02-01-02 Definition | 6 |
| 02-01-03 Aufgaben | 2 |
| 02-02-01 Kerneltypen | 8 |
| 02-02-02 Schichtenmodell | 8 |
| 02-02-03 Systemaufrufe | 9 |
| 02-02-04 Von-Neumann-vs-Harvard | 5 |
| 02-02-06 CPU-Architekturen | 13 |
| 02-03-01 Prozessmodell | 13 |
| 02-03-02 Scheduling | 6 |
| 02-03-03 Threads | 8 |
| 02-03-04 Interprozesskommunikation | 10 |
| 02-05-01 Adressräume | 4 |
| 02-05-02 Virtueller Speicher | 5 |
| 02-05-03 Paging | 6 |
| 02-05-04 Segmentierung | 4 |
| 02-06-01 IO-Grundlagen | 7 |
| 02-07-01 Historie-Festplatten | 15 |
| 02-07-02 Grundlagen | 7 |
| 02-07-03 Implementierung | 10 |
| 02-07-04 Journaling | 8 |
| 03-03-01 OSI-Modell | 2 |
| 03-03-02 TCP-IP-Modell | 1 |
| 03-03-03 Schichtenvergleich | 1 |
| 03-03-04 Arbeitsweise-Schichtenmodell | 14 |

---

## 03-Rechnernetze / 03-Referenzmodelle

### 01-OSI-Modell (03-03-01)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 03-03-01-osi-schichten | Die 7 Schichten des OSI-Referenzmodells |
| 03-03-01-protokoll-schichten | Protokollzuordnung zu den OSI-Schichten |

### 02-TCP-IP-Modell (03-03-02)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 03-03-02-tcp-ip-schichten | Die 4 Schichten des TCP/IP-Modells (DoD-Modell) |

### 03-Schichtenvergleich (03-03-03)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 03-03-03-protokoll-schichten | Vergleich OSI vs. TCP/IP mit Protokollzuordnung |

### 04-Arbeitsweise-Schichtenmodell (03-03-04)

| Abbildungs-ID | Beschreibung |
|---------------|--------------|
| 03-03-04-schichtendurchlauf | Schichtendurchlauf vom Client über Router zum Server |
| 03-03-04-datenfluss | Datenfluss durch die Schichten mit Ein- und Entkapselung |
| 03-03-04-szenario | Netzwerkszenario mit Client, Router und Webserver |
| 03-03-04-einkapselung | Einkapselung (Encapsulation) – schrittweises Hinzufügen von Headern |
| 03-03-04-schicht-anwendung | Anwendungsschicht erzeugt HTTP-Request |
| 03-03-04-schicht-transport | Transportschicht fügt TCP-Header hinzu |
| 03-03-04-schicht-internet | Internetschicht fügt IP-Header hinzu |
| 03-03-04-schicht-netzzugang | Netzzugangsschicht fügt Ethernet-Header und FCS hinzu |
| 03-03-04-router-verarbeitung | Router-Verarbeitung – Empfang, Routing-Entscheidung und Versand |
| 03-03-04-router-schichten | Router verarbeiten nur Layer 1-3 |
| 03-03-04-entkapselung | Entkapselung (Decapsulation) – schrittweises Entfernen der Header |
| 03-03-04-empfangsprozess | Detaillierter Empfangsprozess – Verarbeitung auf jeder Schicht |
| 03-03-04-paketfluss | Kompletter Paketfluss vom Client über Router zum Server |
| 03-03-04-pdu | PDU-Bezeichnungen (Protocol Data Units) pro Schicht |

---

**Gesamtzahl der Abbildungen:** 204
