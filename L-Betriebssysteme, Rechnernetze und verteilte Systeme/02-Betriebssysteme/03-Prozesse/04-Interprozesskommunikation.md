---
author: Andreas Hümmer
title: Interprozesskommunikation
tags:
  - content
  - bs
  - prozesse
  - ipc
  - pipes
  - sockets
  - shared-memory
created: '2026-10-07'
modified: '2026-10-09'
bereich: BS
---

# Interprozesskommunikation

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die verschiedenen IPC-Mechanismen kennen und unterscheiden können
> - Shared Memory vs. Message Passing erklären können
> - Unix IPC-Mechanismen (Pipes, Signals, Sockets) kennen
> - Die Vor- und Nachteile der verschiedenen Kommunikationsarten verstehen
> - Wissen, wann welcher IPC-Mechanismus sinnvoll ist
> - Praktische Anwendungsfälle für die verschiedenen IPC-Methoden kennen

---

## Definition

> [!quote] **Formale Definition**
> **Interprozesskommunikation (IPC)** bezeichnet Mechanismen zur Zusammenarbeit mehrerer Prozesse – sowohl zur Kommunikation (Datenaustausch) als auch zur Koordination.

### Warum brauchen Prozesse Kommunikation?

Prozesse sind durch ihre getrennten Adressräume **isoliert** – das ist gewollt für Sicherheit und Stabilität, aber manchmal müssen Prozesse zusammenarbeiten:

| Anwendungsfall | Beispiel |
|----------------|----------|
| **Datenübergabe** | Shell-Pipeline: `cat file \| grep pattern \| wc -l` |
| **Arbeitsteilung** | Webserver: Master verteilt Anfragen an Worker |
| **Benachrichtigung** | Daemon informiert über Ereignisse |
| **Ressourcenteilung** | Datenbankserver mit mehreren Clients |
| **Modulare Architektur** | Microservices kommunizieren über APIs |

> [!example] **Alltägliches Beispiel**
> Wenn du `ls | grep .txt` in der Shell eingibst, kommunizieren zwei Prozesse:
> - `ls` schreibt seine Ausgabe in eine Pipe
> - `grep` liest aus derselben Pipe
> 
> Ohne IPC wäre diese elegante Verkettung nicht möglich!

---

## Kommunikationsszenarien

Prozesse können in verschiedenen Konstellationen kommunizieren. Je nach Szenario stehen unterschiedliche IPC-Mechanismen zur Verfügung:

![[02-03-04-ipc-scenarios.png]]
<span class="fig-id">02-03-04-01</span> *Kommunikationsszenarien: Lokal (Single/Multi-CPU) und über Netzwerk*

### Szenario 1: Lokale Kommunikation (Single-CPU)

Prozesse auf **derselben CPU** kommunizieren zeitversetzt – während einer arbeitet, wartet der andere. Der Scheduler wechselt zwischen den Prozessen.

**Verfügbare Mechanismen:** Alle lokalen IPC (Pipes, Signals, Shared Memory, Message Queues, Unix Sockets)

**Beispiel:** Shell-Pipeline `cat file | grep pattern`
- Scheduler wechselt zwischen `cat` und `grep`
- Pipe puffert Daten dazwischen
- Quasi-parallele Ausführung durch schnelles Umschalten

### Szenario 2: Lokale Kommunikation (Multi-CPU/Multi-Core)

Auf **Mehrkernsystemen** können Prozesse tatsächlich parallel laufen. Die Kommunikation erfolgt über gemeinsamen Hauptspeicher.

**Besonderheiten:**
- **Cache-Kohärenz:** CPUs haben eigene Caches → Änderungen müssen synchronisiert werden
- **Memory Barriers:** Spezielle Instruktionen garantieren Sichtbarkeit von Änderungen
- **Atomare Operationen:** Ununterbrechbare Lese-Schreib-Zyklen

**Verfügbare Mechanismen:** Wie Szenario 1, aber Shared Memory besonders effizient

**Beispiel:** Webserver mit Worker-Pool
- Master-Prozess nimmt Anfragen an
- Worker-Prozesse auf verschiedenen Kernen verarbeiten parallel
- Kommunikation über Shared Memory Queue

### Szenario 3: Verteilte Kommunikation (Netzwerk)

Prozesse auf **verschiedenen Systemen** können nur über das Netzwerk kommunizieren. Kein gemeinsamer Speicher möglich.

**Herausforderungen:**
- **Latenz:** Netzwerk ist langsamer als lokaler Speicher (ms statt ns)
- **Zuverlässigkeit:** Pakete können verloren gehen, Verbindungen abbrechen
- **Byte-Order:** Unterschiedliche Architekturen (Big/Little Endian)
- **Serialisierung:** Datenstrukturen müssen in Byteströme umgewandelt werden

**Verfügbare Mechanismen:** Nur Sockets (TCP/UDP)

**Beispiel:** Microservice-Architektur
- Service A (Bestellungen) auf Server 1
- Service B (Lager) auf Server 2
- Kommunikation über REST API (HTTP/TCP)

### Übersicht: Mechanismen nach Szenario

| Szenario | Pipes | Signals | Shared Mem | Msg Queue | Sockets |
|----------|-------|---------|------------|-----------|---------|
| Lokal (1 CPU) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Lokal (Multi-CPU) | ✓ | ✓ | ✓✓ | ✓ | ✓ |
| Über Netzwerk | ✗ | ✗ | ✗ | ✗ | ✓ |

✓✓ = besonders geeignet

---

## IPC-Methoden im Überblick

### Zwei Grundansätze

![[02-03-04-ipc-approaches.png]]
<span class="fig-id">02-03-04-02</span> *Die zwei Grundansätze der IPC: Shared Memory und Message Passing*

| Methode | Vorteile | Nachteile |
|---------|----------|-----------|
| **Shared Memory** | Schnell, direkter Zugriff | Erfordert Synchronisation |
| **Message Passing** | Sicher, portabel | Langsamer, Kopieraufwand |

### Shared Memory im Detail

Beim Shared Memory wird ein Speicherbereich in die Adressräume mehrerer Prozesse eingeblendet. Alle Prozesse können direkt lesen und schreiben – ohne Kernel-Beteiligung nach der initialen Einrichtung.

**Typischer Ablauf:**
1. Prozess A erstellt Shared-Memory-Segment (`shmget()` / `shm_open()`)
2. Prozess A mappt es in seinen Adressraum (`shmat()` / `mmap()`)
3. Prozess B verbindet sich zum selben Segment
4. Beide können nun direkt auf den Speicher zugreifen
5. **Kritisch:** Zugriffe müssen synchronisiert werden!

**POSIX Shared Memory Beispiel (C):**

```c
#include <sys/mman.h>
#include <fcntl.h>

// Shared Memory erstellen
int fd = shm_open("/my_shm", O_CREAT | O_RDWR, 0666);
ftruncate(fd, 4096);  // Größe festlegen

// In Adressraum einblenden
char *ptr = mmap(NULL, 4096, PROT_READ | PROT_WRITE, 
                 MAP_SHARED, fd, 0);

// Daten schreiben (ohne Kernel!)
strcpy(ptr, "Hello from Process A");

// Aufräumen
munmap(ptr, 4096);
shm_unlink("/my_shm");
```

### Message Passing im Detail

Beim Message Passing werden Daten explizit zwischen Prozessen **kopiert**. Der Kernel vermittelt die Übertragung.

**Vorteile:**
- Keine Race Conditions auf Nachrichtenebene
- Funktioniert auch über Netzwerk
- Klare Semantik (Senden/Empfangen)

**Nachteile:**
- Kopieroverhead (Daten: User → Kernel → User)
- Bei großen Datenmengen ineffizient

> [!note] **Moderne Trends**
> Viele moderne Systeme (Microservices, Erlang/Elixir, Go) bevorzugen Message Passing trotz des Overheads, weil es einfacher korrekt zu programmieren ist. Der Satz "Don't communicate by sharing memory; share memory by communicating" (Go-Philosophie) fasst das zusammen.

---

## Unix IPC-Mechanismen

Unix bietet eine reiche Palette an IPC-Mechanismen, die historisch gewachsen sind. Man unterscheidet zwischen **System V IPC** (älter) und **POSIX IPC** (neuer, portabler).

| API-Familie | Mechanismen | Charakteristik |
|-------------|-------------|----------------|
| **System V IPC** | Semaphore, Shared Memory, Message Queues | Ältere API, weite Verbreitung |
| **POSIX IPC** | sem_*, shm_*, mq_* | Modernere API, einheitlicher |
| **Basis-Unix** | Pipes, Signals, Sockets | Fundamental, überall verfügbar |

### 1. Signals

Asynchrone Benachrichtigungen zwischen Prozessen. Signals sind die einfachste Form der IPC – sie transportieren nur eine **Nummer**, keine Daten.

![[02-03-04-ipc-signals.png]]
<span class="fig-id">02-03-04-07</span> *Signal: Prozess A sendet SIGTERM an Prozess B*

**Wichtige Signale:**

| Signal | Nummer | Beschreibung | Abfangbar? |
|--------|--------|--------------|------------|
| `SIGHUP` | 1 | Hangup (Terminal geschlossen) | Ja |
| `SIGINT` | 2 | Interrupt (Ctrl+C) | Ja |
| `SIGQUIT` | 3 | Quit (Ctrl+\\) | Ja |
| `SIGKILL` | 9 | Sofortige Terminierung | **Nein** |
| `SIGSEGV` | 11 | Segmentation Fault | Ja |
| `SIGTERM` | 15 | Terminierung anfragen | Ja |
| `SIGSTOP` | 19 | Prozess anhalten | **Nein** |
| `SIGCONT` | 18 | Prozess fortsetzen | Ja |
| `SIGUSR1/2` | 10/12 | Benutzerdefiniert | Ja |

**Signal Handler in C:**

```c
#include <signal.h>
#include <stdio.h>

void handler(int sig) {
    printf("Signal %d empfangen!\n", sig);
}

int main() {
    // Handler für SIGINT registrieren
    signal(SIGINT, handler);
    
    // Oder moderner mit sigaction():
    struct sigaction sa;
    sa.sa_handler = handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sigaction(SIGTERM, &sa, NULL);
    
    while(1) pause();  // Warten auf Signals
}
```

**Signal an Prozess senden:**

```bash
# Über PID
kill -SIGTERM 1234
kill -15 1234

# Über Name
pkill -SIGTERM firefox
killall -SIGTERM firefox
```

> [!warning] **Signal-Sicherheit**
> Signal Handler unterbrechen den normalen Programmfluss asynchron. Im Handler dürfen nur **async-signal-safe** Funktionen verwendet werden (siehe `man signal-safety`). `printf()` gehört streng genommen nicht dazu!

Siehe: `man 7 signal`, `man 2 kill`, `man 2 sigaction`

---

### 2. Pipes

Unidirektionale Kommunikation zwischen verwandten Prozessen. Pipes sind der klassische Unix-IPC-Mechanismus.

![[02-03-04-ipc-pipe.png]]
<span class="fig-id">02-03-04-03</span> *Anonyme Pipe: Unidirektionaler Datenfluss zwischen Eltern- und Kindprozess*

**Charakteristiken:**
- **Unidirektional:** Daten fließen nur in eine Richtung
- **FIFO-Puffer:** First-In-First-Out, typisch 64KB (Linux)
- **Blockierend:** `read()` blockiert bei leerer Pipe, `write()` bei voller Pipe
- **Lebenszeit:** Pipe existiert nur, solange ein Prozess sie offen hat

**Pipe in C erstellen:**

```c
#include <unistd.h>

int main() {
    int pipefd[2];  // [0] = Lesen, [1] = Schreiben
    
    pipe(pipefd);   // Pipe erstellen
    
    if (fork() == 0) {
        // Kind: liest aus der Pipe
        close(pipefd[1]);  // Schreibende schließen
        char buf[100];
        read(pipefd[0], buf, sizeof(buf));
        printf("Kind empfing: %s\n", buf);
        close(pipefd[0]);
    } else {
        // Eltern: schreibt in die Pipe
        close(pipefd[0]);  // Leseende schließen
        write(pipefd[1], "Hallo Kind!", 12);
        close(pipefd[1]);
        wait(NULL);
    }
    return 0;
}
```

**Shell-Pipeline intern:**

Wenn du `ls | grep .txt | wc -l` eingibst, passiert folgendes:

1. Shell erstellt zwei Pipes
2. Shell forkt drei Kindprozesse
3. Jeder Prozess schließt ungenutzte Enden
4. stdout von `ls` → Pipe 1 → stdin von `grep`
5. stdout von `grep` → Pipe 2 → stdin von `wc`

### Named Pipes (FIFOs)

Für nicht-verwandte Prozesse, haben einen Namen im Dateisystem.

```bash
# FIFO erstellen
mkfifo /tmp/mypipe

# Terminal 1 (blockiert bis Leser da ist)
echo "Hello" > /tmp/mypipe

# Terminal 2
cat /tmp/mypipe  # Gibt "Hello" aus
```

**Unterschied zu anonymen Pipes:**

| Eigenschaft | Anonyme Pipe | Named Pipe (FIFO) |
|-------------|--------------|-------------------|
| Erstellung | `pipe()` | `mkfifo()` oder `mknod()` |
| Im Dateisystem | Nein | Ja (als Special File) |
| Verwandte Prozesse | Erforderlich | Nicht erforderlich |
| Persistenz | Bis alle schließen | Bleibt im Dateisystem |

**Named Pipe in C:**

```c
#include <sys/stat.h>
#include <fcntl.h>

// Erstellen
mkfifo("/tmp/myfifo", 0666);

// Öffnen zum Schreiben
int fd = open("/tmp/myfifo", O_WRONLY);
write(fd, "Nachricht", 10);
close(fd);

// Aufräumen
unlink("/tmp/myfifo");
```

---

### 3. Message Queues

Nachrichtenwarteschlangen für strukturierte Kommunikation. Im Gegensatz zu Pipes können Nachrichten hier **priorisiert** und **typisiert** werden.

![[02-03-04-ipc-message-queue.png]]
<span class="fig-id">02-03-04-04</span> *Message Queue: Mehrere Sender können Nachrichten an einen Empfänger schicken*

**Vorteile gegenüber Pipes:**
- Nachrichten haben **Grenzen** (nicht nur Bytestrom)
- Mehrere Sender und Empfänger möglich
- Nachrichten können nach **Typ** gefiltert werden
- Queue existiert unabhängig von den Prozessen

**POSIX Message Queue Beispiel:**

```c
#include <mqueue.h>
#include <fcntl.h>

// Sender
mqd_t mq = mq_open("/myqueue", O_CREAT | O_WRONLY, 0666, NULL);
mq_send(mq, "Hello", 6, 0);  // Priorität 0
mq_close(mq);

// Empfänger
mqd_t mq = mq_open("/myqueue", O_RDONLY);
char buf[256];
unsigned int prio;
mq_receive(mq, buf, 256, &prio);
printf("Empfangen: %s (Prio %u)\n", buf, prio);
mq_close(mq);
mq_unlink("/myqueue");
```

**Kompilieren:** `gcc -lrt program.c`

> [!note] **System V vs. POSIX Message Queues**
> - **System V:** `msgget()`, `msgsnd()`, `msgrcv()` – älter, komplexer
> - **POSIX:** `mq_open()`, `mq_send()`, `mq_receive()` – einfacher, empfohlen

---

### 4. Shared Memory

Der schnellste IPC-Mechanismus für große Datenmengen. Nach einmaliger Einrichtung erfolgt kein Syscall mehr beim Datenzugriff.

![[02-03-04-ipc-shared-memory.png]]
<span class="fig-id">02-03-04-05</span> *Shared Memory: Beide Prozesse greifen auf denselben Speicherbereich zu*

**Performance-Vorteil:**

| Operation | Pipe/Message Queue | Shared Memory |
|-----------|-------------------|---------------|
| 1 MB übertragen | ~2 Kopien (User→Kernel→User) | 0 Kopien |
| Syscalls pro Zugriff | Jedes Mal | Nur bei Setup |
| Latenz | Höher | Minimal |

**POSIX Shared Memory – Vollständiges Beispiel:**

```c
// === Prozess A (Schreiber) ===
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    // Shared Memory erstellen
    int fd = shm_open("/demo_shm", O_CREAT | O_RDWR, 0666);
    ftruncate(fd, 4096);
    
    // Einblenden
    char *ptr = mmap(NULL, 4096, PROT_READ | PROT_WRITE, 
                     MAP_SHARED, fd, 0);
    
    // Schreiben
    strcpy(ptr, "Daten von Prozess A");
    
    // NICHT aufräumen - B muss noch lesen!
    munmap(ptr, 4096);
    close(fd);
    return 0;
}

// === Prozess B (Leser) ===
int main() {
    // Existierendes Segment öffnen
    int fd = shm_open("/demo_shm", O_RDONLY, 0);
    
    char *ptr = mmap(NULL, 4096, PROT_READ, MAP_SHARED, fd, 0);
    
    printf("Empfangen: %s\n", ptr);
    
    munmap(ptr, 4096);
    close(fd);
    shm_unlink("/demo_shm");  // Aufräumen
    return 0;
}
```

**Kompilieren:** `gcc -lrt program.c`

> [!danger] **Achtung: Synchronisation erforderlich!**
> Bei Shared Memory muss der Zugriff synchronisiert werden, sonst entstehen Race Conditions! Typische Lösungen:
> - **Semaphore** (POSIX: `sem_open()`, `sem_wait()`, `sem_post()`)
> - **Mutex** in Shared Memory (mit `PTHREAD_PROCESS_SHARED`)
> - **Atomare Operationen** (C11 `<stdatomic.h>`)
> 
> → Siehe [[01-Kritische-Abschnitte|Kritische Abschnitte]] und [[02-Semaphore|Semaphore]]

**Shared Memory anzeigen (Linux):**

```bash
# POSIX Shared Memory
ls -la /dev/shm/

# System V Shared Memory
ipcs -m
```

---

### 5. Sockets

Netzwerkfähige Kommunikation, auch lokal (Unix Domain Sockets). Sockets sind der universellste IPC-Mechanismus.

![[02-03-04-ipc-sockets.png]]
<span class="fig-id">02-03-04-06</span> *Socket-Kommunikation: Client-Server-Ablauf mit den wichtigsten Systemaufrufen*

**Socket-Typen:**

| Socket-Typ | Protokoll | Beschreibung |
|------------|-----------|--------------|
| `SOCK_STREAM` | TCP | Verbindungsorientiert, zuverlässig, Reihenfolge garantiert |
| `SOCK_DGRAM` | UDP | Verbindungslos, schnell, keine Garantien |
| `SOCK_SEQPACKET` | SCTP | Verbindungsorientiert mit Nachrichtengrenzen |

**Socket-Familien:**

| Familie | Konstante | Verwendung |
|---------|-----------|------------|
| IPv4 | `AF_INET` | Netzwerk (Internet) |
| IPv6 | `AF_INET6` | Netzwerk (Internet, moderner) |
| Unix | `AF_UNIX` / `AF_LOCAL` | Nur lokal, sehr schnell |

**TCP Server Beispiel (C):**

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    // Socket erstellen
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    
    // Adresse konfigurieren
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = INADDR_ANY
    };
    
    // Socket an Adresse binden
    bind(server_fd, (struct sockaddr*)&addr, sizeof(addr));
    
    // Auf Verbindungen warten
    listen(server_fd, 5);  // Max 5 in der Warteschlange
    
    // Verbindung annehmen
    int client_fd = accept(server_fd, NULL, NULL);
    
    // Daten empfangen und senden
    char buf[1024];
    int n = recv(client_fd, buf, sizeof(buf), 0);
    send(client_fd, "OK", 2, 0);
    
    close(client_fd);
    close(server_fd);
    return 0;
}
```

**Unix Domain Socket – Lokale Hochleistungs-IPC:**

```c
// Server
struct sockaddr_un addr;
addr.sun_family = AF_UNIX;
strcpy(addr.sun_path, "/tmp/mysocket");

int fd = socket(AF_UNIX, SOCK_STREAM, 0);
bind(fd, (struct sockaddr*)&addr, sizeof(addr));
listen(fd, 5);
// ...

// Aufräumen
unlink("/tmp/mysocket");
```

**Unix Domain Sockets in der Praxis:**

```bash
# Viele Dienste nutzen Unix Sockets
ls -la /var/run/*.sock
# z.B.: /var/run/docker.sock, /var/run/mysqld/mysqld.sock

# Socket-Statistiken
ss -x  # Unix Domain Sockets anzeigen
ss -t  # TCP Sockets anzeigen
```

> [!tip] **Wann welchen Socket-Typ?**
> - **TCP (`SOCK_STREAM`):** Wenn Zuverlässigkeit wichtig ist (HTTP, Datenbank)
> - **UDP (`SOCK_DGRAM`):** Für Echtzeit-Daten (Gaming, Streaming, DNS)
> - **Unix Domain:** Wenn beide Prozesse auf demselben System sind (schneller als TCP localhost!)

---

## Synchron vs. Asynchron

| Modus | Beschreibung | Beispiel |
|-------|--------------|----------|
| **Synchron (blockierend)** | Sender wartet auf Empfang/Bestätigung | Telefonat, `read()` auf leerer Pipe |
| **Asynchron (nicht-blockierend)** | Sender wartet nicht | E-Mail, Signals, `O_NONBLOCK` |

**Synchrone Kommunikation:**

![[02-03-04-ipc-sync.png]]
<span class="fig-id">02-03-04-08</span> *Synchrone Kommunikation: Sender wartet auf Antwort*

**Asynchrone Kommunikation:**

![[02-03-04-ipc-async.png]]
<span class="fig-id">02-03-04-09</span> *Asynchrone Kommunikation: Sender arbeitet sofort weiter*

**Non-blocking I/O in C:**

```c
#include <fcntl.h>

// Socket auf non-blocking setzen
int flags = fcntl(fd, F_GETFL, 0);
fcntl(fd, F_SETFL, flags | O_NONBLOCK);

// Jetzt kehrt recv() sofort zurück
// Wenn keine Daten: errno == EAGAIN oder EWOULDBLOCK
```

---

## Moderne IPC-Mechanismen

Neben den klassischen Unix-IPC-Methoden gibt es moderne Ansätze:

| Mechanismus | Beschreibung | Anwendung |
|-------------|--------------|-----------|
| **D-Bus** | Message Bus für Desktop-Anwendungen | Linux Desktop (GNOME, KDE) |
| **ZeroMQ** | High-Performance Messaging Library | Verteilte Systeme |
| **gRPC** | Remote Procedure Calls mit Protocol Buffers | Microservices |
| **Unix Domain Sockets** | Lokale Sockets ohne Netzwerk-Overhead | Docker, Databases |
| **eventfd** | Leichtgewichtige Event-Notification | Kernel-Userspace |
| **io_uring** | Asynchrone I/O (Linux 5.1+) | High-Performance Server |

---

## Praktische Entscheidungshilfe

**Welchen IPC-Mechanismus wählen?**

![[02-03-04-ipc-decision.png]]
<span class="fig-id">02-03-04-10</span> *Entscheidungsbaum zur Auswahl des passenden IPC-Mechanismus*

| Anwendungsfall | Empfohlener Mechanismus |
|----------------|------------------------|
| Shell-Pipeline | Anonyme Pipe |
| Daemon → Client Notification | Signals oder Unix Socket |
| Hochfrequenter Datenaustausch (lokal) | Shared Memory |
| Request-Response (lokal) | Unix Domain Socket |
| Request-Response (Netzwerk) | TCP Socket |
| Broadcast/Multicast | UDP Socket |
| Lose gekoppelte Prozesse | Message Queue |

---

## Zusammenfassung der IPC-Mechanismen

| Mechanismus | Richtung | Verwandte Prozesse | Netzwerkfähig | Typische Anwendung |
|-------------|----------|-------------------|---------------|-------------------|
| Signals | Unidirektional | Nein | Nein | Prozesssteuerung, Events |
| Pipes | Unidirektional | Ja | Nein | Shell-Pipelines |
| Named Pipes | Unidirektional | Nein | Nein | Einfache Prozess-Verbindung |
| Message Queues | Bidirektional | Nein | Nein | Strukturierte Nachrichten |
| Shared Memory | Bidirektional | Nein | Nein | Große Datenmengen, Performance |
| Sockets | Bidirektional | Nein | Ja | Client-Server, Netzwerk |

---

## Praktische Kommandos

### IPC-Ressourcen anzeigen (Linux)

```bash
# System V IPC Ressourcen
ipcs           # Alle anzeigen
ipcs -m        # Shared Memory
ipcs -q        # Message Queues
ipcs -s        # Semaphore

# System V IPC löschen
ipcrm -m <shmid>   # Shared Memory Segment
ipcrm -q <msqid>   # Message Queue
ipcrm -s <semid>   # Semaphore Set

# POSIX Shared Memory
ls -la /dev/shm/

# Unix Domain Sockets
ss -x          # Alle Unix Sockets
ss -xlp        # Mit Prozess-Info

# Offene Dateien (inkl. Pipes, Sockets)
lsof -p <PID>

# Named Pipes finden
find /tmp -type p 2>/dev/null
```

### Pipe-Beispiel in der Shell

```bash
# Einfache Pipeline
cat /var/log/syslog | grep error | wc -l

# Named Pipe für Prozess-Kommunikation
mkfifo /tmp/testpipe
# Terminal 1:
tail -f /var/log/syslog > /tmp/testpipe
# Terminal 2:
grep --line-buffered error < /tmp/testpipe

# Cleanup
rm /tmp/testpipe
```

---

## Zusammenhänge

- [[01-Prozessmodell|Prozessmodell]] → Prozesse müssen kommunizieren
- [[01-Kritische-Abschnitte|Kritische Abschnitte]] → Synchronisation bei Shared Memory
- [[03-Deadlocks|Deadlocks]] → Können bei IPC auftreten!
- [[02-Semaphore|Semaphore]] → Für Shared Memory Synchronisation

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied Shared Memory vs. Message Passing (Kopieren vs. gemeinsamer Zugriff)
> - Unix IPC-Mechanismen (Pipes, Signals, Sockets, Shared Memory, Message Queues)
> - Vor- und Nachteile der verschiedenen Mechanismen
> - Wann braucht man Synchronisation? (Bei Shared Memory!)
> - Synchrone vs. asynchrone Kommunikation
> - Socket-Typen (TCP vs. UDP, Unix Domain)

> [!question] **Häufige Prüfungsfragen**
> 1. Nennen und erklären Sie drei IPC-Mechanismen unter Unix!
> 2. Was ist der Unterschied zwischen Shared Memory und Message Passing?
> 3. Warum benötigt Shared Memory Synchronisation, Message Passing aber nicht?
> 4. Was ist der Unterschied zwischen anonymen Pipes und Named Pipes?
> 5. Welche IPC-Methode würden Sie für Netzwerkkommunikation wählen und warum?
> 6. Erklären Sie den Unterschied zwischen TCP und UDP Sockets!
> 7. Was ist ein Unix Domain Socket und wann würde man ihn verwenden?
> 8. Was passiert, wenn ein Prozess auf eine leere Pipe liest?

> [!tip] **Merkhilfen**
> - **Pipe** = "Rohrpost" (nur eine Richtung, nur verwandte, First-In-First-Out)
> - **Shared Memory** = "Gemeinsame Kreidetafel" (schnell, aber alle müssen aufpassen wer schreibt)
> - **Socket** = "Telefon" (bidirektional, auch über Distanz, Verbindung muss aufgebaut werden)
> - **Signal** = "Klopfzeichen" (nur Benachrichtigung, keine Daten, asynchron)
> - **Message Queue** = "Briefkasten" (Nachrichten mit Grenzen, mehrere Absender möglich)
> - **FIFO** = "Named Pipe" = Pipe mit Namen im Dateisystem

---

## Weiterführende Ressourcen

> [!note] **Videos (YouTube)**
> 
> | | Video | Beschreibung |
> |---|-------|--------------|
> | 🎬 | [CoreDumped – Inter Process Communication](https://www.youtube.com/watch?v=Y2mDwW2pMv4) | IPC-Mechanismen: Pipes, Shared Memory, Signals |

> [!tip] **Weiterführende Links**
> - [Beej's Guide to Unix IPC](https://beej.us/guide/bgipc/) – Ausgezeichnetes Tutorial
> - [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/) – Socket-Programmierung
> - [Linux man-pages: ipc(7)](https://man7.org/linux/man-pages/man7/ipc.7.html)
> - [The Linux Programming Interface](https://man7.org/tlpi/) – Kapitel 43-57

---

## Quellen

- IU Skript: Betriebssysteme, Rechnernetze und verteilte Systeme - Teil 5 (Ressourcen)
- Tanenbaum: Modern Operating Systems
