---
author: Andreas Hümmer
title: Systemaufrufe (System Calls)
tags:
  - content
- bs
- syscalls
- architektur
- kernel
- api
created: '2026-10-07'
modified: '2026-10-07'
bereich: BS
---
author: Andreas Hümmer

# Systemaufrufe (System Calls)

> [!info] **Lernziele**
> Nach dem Durcharbeiten dieses Kapitels sollten Sie:
> 1. **Verstehen**, warum Systemaufrufe notwendig sind und welche Rolle sie im Betriebssystem spielen
> 2. **Erklären** können, wie der Trap-Mechanismus funktioniert und warum ein Kontextwechsel erforderlich ist
> 3. **Unterscheiden** können zwischen User-Mode (Ring 3) und Kernel-Mode (Ring 0)


---
author: Andreas Hümmer

## Überblick

Anwendungen laufen aus Sicherheitsgründen im unprivilegierten User-Mode und dürfen die Hardware nicht direkt ansprechen. Jede Operation, die privilegierten Zugriff erfordert – eine Datei lesen, Speicher anfordern, über das Netzwerk senden – muss daher beim Kernel angefragt werden. Diese Anfrage ist der Systemaufruf, und der Weg dorthin führt über mehrere klar getrennte Ebenen:

![[.assets/syscall-schnittstelle.png]]

*Ein Systemaufruf durchläuft mehrere Ebenen: Das Anwendungsprogramm ruft eine Bibliotheksfunktion (z. B. `printf`) auf, die ihrerseits eine libc-Funktion wie `write()` nutzt. Über die Systemaufruf-Schnittstelle löst eine TRAP-/SYSCALL-Instruktion den Wechsel in den Kernel aus. Dort ordnet der Syscall-Dispatcher den Aufruf anhand der `sys_call_table` der passenden Kernel-Funktion (`sys_read`, `sys_write`, `sys_fork`, …) zu.*

## Definition

**Systemaufrufe** (engl. *System Calls* oder *Syscalls*) sind die fundamentale Schnittstelle zwischen Anwendungsprogrammen im User-Space und dem Betriebssystem-Kernel. Sie ermöglichen es Programmen, privilegierte Operationen anzufordern, die nur der Kernel ausführen darf.

> [!info] **Warum Systemaufrufe?**
> Ohne Systemaufrufe könnten Anwendungen nicht auf Hardware zugreifen, keine Dateien öffnen, keine Netzwerkverbindungen herstellen und keine neuen Prozesse erzeugen. Sie sind das "Tor" zum Kernel.

---
author: Andreas Hümmer

## Der Trap-Mechanismus im Detail

Der Übergang vom User- in den Kernel-Mode kann nicht durch einen gewöhnlichen Funktionsaufruf erfolgen – das würde die Privilegientrennung aushebeln. Stattdessen löst eine spezielle CPU-Instruktion einen *Trap* aus: einen kontrollierten, von der Hardware überwachten Sprung an eine feste Einsprungstelle im Kernel. Erst dort wechselt die CPU in Ring 0.

### Ablauf eines Systemaufrufs

![[.assets/syscall-ablauf-detail.png]]

*Ein Systemaufruf durchläuft acht Stationen, aufgeteilt auf zwei Ebenen: Im **User Mode** (Ring 3) ruft die Anwendung eine libc-Funktion auf (1), der Wrapper legt Syscall-Nummer und Parameter in Register (2) und löst die SYSCALL-Instruktion aus (3). Der **Kontextwechsel** bringt die CPU in den **Kernel Mode** (Ring 0): Dort sichert der Syscall-Handler die Register (4), der Dispatcher findet über die `sys_call_table` die zuständige Funktion (5), diese führt die Operation aus (6) und legt den Rückgabewert in RAX ab (7). Mit `SYSRET`/`IRET` kehrt die Ausführung in den User Mode zurück, und die Anwendung erhält das Ergebnis (8).*

### Registerkonventionen (x86-64 Linux)

Unter x86-64/AMD64 werden Syscall-Nummer und Parameter in festgelegten Registern übergeben:

| Register | Bedeutung |
|----------|-----------|
| **RAX** | Syscall-Nummer (vor Aufruf) / Rückgabewert (nach Aufruf) |
| **RDI** | 1. Parameter |
| **RSI** | 2. Parameter |
| **RDX** | 3. Parameter |
| **R10** | 4. Parameter |
| **R8** | 5. Parameter |
| **R9** | 6. Parameter |

> [!example] Beispiel: `write(fd, buf, count)`
> ```text
> RAX = 1       (Syscall-Nr für write)
> RDI = fd      (File Descriptor)
> RSI = buf     (Zeiger auf Buffer)
> RDX = count   (Anzahl Bytes)
> ```

---
author: Andreas Hümmer

## Syscall-Mechanismen verschiedener Architekturen

Jede Prozessorarchitektur stellt einen eigenen Befehl für den Übergang in den Kernel bereit und legt fest, in welchen Registern Syscall-Nummer und Parameter übergeben werden:

| Architektur | Instruktion | Syscall-Nr. | Parameter-Register |
|-------------|-------------|-------------|--------------------|
| **x86 (32-bit)** | `INT 0x80` | EAX | EBX, ECX, EDX, ESI, EDI, EBP |
| **x86-64** | `SYSCALL` (schneller) | RAX | RDI, RSI, RDX, R10, R8, R9 |
| **ARM (32-bit)** | `SVC` / `SWI` | R7 | R0–R6 |
| **ARM64 (AArch64)** | `SVC #0` | X8 | X0–X5 |
| **RISC-V** | `ECALL` | A7 | A0–A5 |
| **MIPS** | `SYSCALL` | $v0 | $a0–$a3 |

### Evolution: INT 0x80 vs. SYSCALL/SYSENTER

Mit der Zeit wurde der Systemaufruf-Mechanismus deutlich beschleunigt. Die ursprüngliche Methode nutzte den allgemeinen Software-Interrupt-Pfad, während moderne CPUs einen dedizierten, schlanken Befehl bereitstellen:

| Aspekt | `INT 0x80` (alt) | `SYSCALL` / `SYSENTER` (modern) |
|--------|------------------|----------------------------------|
| **Mechanismus** | Software-Interrupt über IDT-Lookup | Direkter Sprung via MSR-Register |
| **Ablauf** | INT 0x80 → IDT-Lookup → Interrupt-Handler → Dispatch | SYSCALL → Handler (direkt) |
| **Kosten** | ca. 100–300 CPU-Zyklen | ca. 20–50 CPU-Zyklen |
| **Overhead** | Volle Interrupt-Logik, Stack-Frames | Kein IDT-Lookup, optimierter Kontextwechsel |
| **Verfügbarkeit** | Alle x86-CPUs (sehr kompatibel) | Intel: SYSENTER/SYSEXIT (ab Pentium II), AMD: SYSCALL/SYSRET (Standard für x86-64) |

> [!tip] Kernaussage
> Der Wechsel von `INT 0x80` zu `SYSCALL` reduziert den Overhead eines Systemaufrufs um etwa das Fünf- bis Zehnfache – entscheidend, da Syscalls millionenfach pro Sekunde auftreten können.

---
author: Andreas Hümmer

## Kategorien von Systemaufrufen

Systemaufrufe lassen sich nach ihrem Aufgabenbereich gruppieren. Die folgenden Kategorien decken die wichtigsten POSIX-Syscalls ab.

### Prozessverwaltung

| Syscall | Beschreibung |
|---------|--------------|
| `fork()` | Neuen Prozess erzeugen (Kopie des Elternprozesses) |
| `exec*()` | Programm in Prozess laden und ausführen |
| `exit()` | Prozess beenden |
| `wait()` / `waitpid()` | Auf Kindprozess warten |
| `getpid()` | Prozess-ID abfragen |
| `getppid()` | Elternprozess-ID abfragen |
| `kill()` | Signal an Prozess senden |
| `nice()` | Priorität ändern |
| `clone()` | Thread/Prozess mit geteilten Ressourcen erzeugen |

![[.assets/syscall-fork-exec-shell.png]]

*Beispiel: Die Shell führt ein Kommando aus. Mit `fork()` erzeugt sie eine Kopie ihrer selbst; das Kind ersetzt sein Programm per `exec()` durch `ls`, während die Eltern-Shell mit `wait()` blockiert. Nach dem `exit(0)` des Kindes kehrt `wait()` zurück und die Shell macht weiter.*

### Dateisystem-Operationen

| Syscall | Beschreibung |
|---------|--------------|
| `open()` | Datei öffnen, File Descriptor erhalten |
| `close()` | File Descriptor schließen |
| `read()` | Daten aus Datei lesen |
| `write()` | Daten in Datei schreiben |
| `lseek()` | Position in Datei ändern |
| `stat()` / `fstat()` | Datei-Metadaten abfragen |
| `mkdir()` | Verzeichnis erstellen |
| `rmdir()` | Verzeichnis löschen |
| `unlink()` | Datei löschen (Link entfernen) |
| `rename()` | Datei umbenennen |
| `chmod()` | Berechtigungen ändern |
| `chown()` | Eigentümer ändern |

![[.assets/file-descriptor-tabelle.png]]

*Jeder Prozess besitzt eine Filedeskriptor-Tabelle. Die Deskriptoren 0, 1 und 2 sind standardmäßig mit stdin, stdout und stderr belegt; weitere entstehen beim Öffnen von Dateien oder Sockets und verweisen auf das jeweilige Ziel.*

### Speicherverwaltung

| Syscall | Beschreibung |
|---------|--------------|
| `brk()` / `sbrk()` | Heap-Grenze (Program Break) verschieben |
| `mmap()` | Speicherbereich einblenden (Dateien, anonym) |
| `munmap()` | Speicherbereich ausblenden |
| `mprotect()` | Zugriffsrechte für Speicherbereich ändern |
| `mlock()` | Speicher vor Auslagerung schützen |

![[.assets/prozess-adressraum.png]]

*Der Adressraum eines Prozesses ist in Segmente gegliedert: Text (Code), initialisierte und uninitialisierte Daten (Data/BSS), der nach oben wachsende Heap (`brk()`), der Bereich für Memory-Mapped Files und Shared Libraries (`mmap()`), der nach unten wachsende Stack und ganz oben der dem Kernel vorbehaltene Bereich.*

### Geräteverwaltung

| Syscall | Beschreibung |
|---------|--------------|
| `ioctl()` | Gerätesteuerung (catch-all für spezielle Operationen) |
| `read()` / `write()` | Auch für Geräte (alles ist eine Datei!) |
| `mknod()` | Gerätedatei erstellen |

> [!info] Unix-Philosophie: "Everything is a file"
> Geräte werden wie Dateien angesprochen:
> `/dev/sda` (Festplatte) · `/dev/null` (verwirft alles) · `/dev/zero` (liefert Nullbytes) · `/dev/random` (Zufallszahlen) · `/dev/tty` (Terminal) · `/dev/fb0` (Framebuffer)

### Kommunikation / IPC

| Syscall | Beschreibung |
|---------|--------------|
| `pipe()` | Unidirektionale Pipe erzeugen |
| `socket()` | Netzwerk-Socket erzeugen |
| `connect()` | Verbindung aufbauen |
| `bind()` | Socket an Adresse binden |
| `listen()` | Auf Verbindungen warten |
| `accept()` | Verbindung akzeptieren |
| `send()` / `recv()` | Daten senden/empfangen |
| `shmget()` | Shared Memory Segment erzeugen |
| `shmat()` | Shared Memory anbinden |
| `semget()` | Semaphor erzeugen |
| `msgget()` | Message Queue erzeugen |

### Informationsabfragen

| Syscall | Beschreibung |
|---------|--------------|
| `time()` / `gettimeofday()` | Systemzeit abfragen |
| `uname()` | Systeminformationen (OS, Version, Arch) |
| `getuid()` / `getgid()` | Benutzer-/Gruppen-ID |
| `getcwd()` | Aktuelles Arbeitsverzeichnis |
| `getrlimit()` | Ressourcenlimits abfragen |

---
author: Andreas Hümmer

## Die wichtigsten POSIX-Systemaufrufe im Detail

Einige Systemaufrufe tauchen in nahezu jedem Programm auf. Besonders das Zusammenspiel von `fork()`, `exec()` und den Datei-Operationen bildet das Fundament, auf dem Shells, Server und praktisch alle Unix-Werkzeuge aufbauen. Die folgenden Abschnitte betrachten sie genauer.

### fork() - Prozess erzeugen

`fork()` erzeugt einen neuen Prozess als Kopie des aufrufenden. Beide Prozesse laufen anschließend dieselbe Stelle im Code weiter – unterschieden werden sie nur am Rückgabewert: Der Elternprozess erhält die PID des Kindes, das Kind erhält `0`.

![[.assets/fork-copy-on-write.png]]

> [!note] Copy-on-Write (COW)
> Nach `fork()` teilen sich Eltern- und Kindprozess zunächst dieselben Speicherseiten. Erst wenn einer der beiden schreibt, wird die betroffene Seite kopiert. Das macht `fork()` schnell und speichereffizient, selbst bei großen Prozessen.

**Typische Verwendung:**

```c
pid_t pid = fork();
if (pid == 0) {
    // Kind-Prozess
    execlp("ls", "ls", NULL);
} else if (pid > 0) {
    // Eltern-Prozess
    wait(NULL);
} else {
    // Fehler
    perror("fork");
}
```

### exec() Familie - Programm laden

Alle `exec`-Funktionen ersetzen das Programm des aktuellen Prozesses durch ein neues. Bei Erfolg kehren sie **nicht** zurück – der alte Programmcode existiert danach nicht mehr. Es gibt sechs Varianten, die sich in der Argumentübergabe unterscheiden:

| Funktion | Beschreibung |
|----------|--------------|
| `execl()` | Liste von Argumenten, Pfad direkt |
| `execlp()` | Liste von Argumenten, sucht in PATH |
| `execle()` | Liste + eigene Umgebungsvariablen |
| `execv()` | Array von Argumenten, Pfad direkt |
| `execvp()` | Array von Argumenten, sucht in PATH |
| `execve()` | Array + Umgebung (der eigentliche Syscall!) |

> [!tip] Merkregel für die Namenssuffixe
> **l** = Liste (Argumente einzeln) · **v** = Vektor (Array) · **p** = PATH-Suche · **e** = Environment

**Wichtig:** `exec()` behält die PID und die offenen File Descriptors bei – nur Code und Daten werden durch das neue Programm ersetzt. Ruft z. B. die Shell (PID 101) `exec("/bin/ls")` auf, läuft danach `ls` unter derselben PID 101 weiter.

**Beispiele:**

```c
execl("/bin/ls", "ls", "-la", NULL);
execlp("ls", "ls", "-la", NULL);          // sucht in PATH

char *args[] = {"ls", "-la", NULL};
execv("/bin/ls", args);
execvp("ls", args);                        // sucht in PATH
```

### open(), read(), write(), close()

Dateien werden über einen File Descriptor angesprochen, den `open()` zurückgibt. Das Verhalten von `open()` wird über Flags gesteuert:

| Flag | Bedeutung |
|------|-----------|
| `O_RDONLY` | nur lesen |
| `O_WRONLY` | nur schreiben |
| `O_RDWR` | lesen und schreiben |
| `O_CREAT` | erstellen, wenn nicht vorhanden |
| `O_TRUNC` | auf Länge 0 kürzen |
| `O_APPEND` | am Ende anhängen |

![[.assets/open-file-table.png]]

*Der vom Prozess gehaltene File Descriptor (hier `fd = 3`) verweist auf einen Eintrag in der systemweiten Open File Table des Kernels. Dieser Eintrag speichert u. a. die aktuelle Position und die Zugriffs-Flags und zeigt auf den Inode, der die eigentliche Datei auf dem Datenträger repräsentiert.*

**Lesen, Schreiben, Schließen:**

```c
// Datei öffnen
int fd = open("/etc/passwd", O_RDONLY);

// Lesen
char buffer[1024];
ssize_t bytes_read = read(fd, buffer, sizeof(buffer));

// Schreiben
const char *msg = "Hello";
ssize_t bytes_written = write(fd, msg, strlen(msg));

// Datei schließen
close(fd);
```

> [!warning] Fehlerbehandlung nicht vergessen!
> Ein Rückgabewert von `-1` signalisiert einen Fehler; der genaue Code steht in `errno`, und `perror()` gibt eine lesbare Meldung aus.
> ```c
> if (fd == -1) {
>     perror("open failed");
>     // errno == ENOENT → Datei existiert nicht
>     // errno == EACCES → keine Berechtigung
>     // errno == EINTR  → unterbrochen durch Signal
> }
> ```

---
author: Andreas Hümmer

## System Call Table

Jeder Systemaufruf hat unter Linux (x86-64) eine feste Nummer, über die der Dispatcher ihn in der `sys_call_table` findet. Ein Auszug:

| Nr. | Name | Beschreibung |
|-----|------|--------------|
| 0 | `read` | Aus Datei/Socket lesen |
| 1 | `write` | In Datei/Socket schreiben |
| 2 | `open` | Datei öffnen |
| 3 | `close` | File Descriptor schließen |
| 4 | `stat` | Datei-Status abfragen |
| 5 | `fstat` | Status über File Descriptor |
| 6 | `lstat` | Status (folgt Symlinks nicht) |
| 7 | `poll` | Auf Events warten (mehrere FDs) |
| 8 | `lseek` | Position in Datei ändern |
| 9 | `mmap` | Speicher einblenden |
| 10 | `mprotect` | Speicherschutz ändern |
| 11 | `munmap` | Speicher ausblenden |
| 12 | `brk` | Heap-Grenze setzen |
| 39 | `getpid` | Prozess-ID abfragen |
| 41 | `socket` | Socket erstellen |
| 42 | `connect` | Verbindung aufbauen |
| 43 | `accept` | Verbindung akzeptieren |
| 44 | `sendto` | Daten senden |
| 45 | `recvfrom` | Daten empfangen |
| 56 | `clone` | Thread/Prozess erzeugen |
| 57 | `fork` | Prozess duplizieren |
| 59 | `execve` | Programm ausführen |
| 60 | `exit` | Prozess beenden |
| 61 | `wait4` | Auf Kindprozess warten |
| 62 | `kill` | Signal senden |

> [!note] Vollständige Liste
> Alle Syscall-Nummern stehen in `/usr/include/asm/unistd_64.h`; eine Beschreibung liefert `man syscalls`.

---
author: Andreas Hümmer

## Syscalls in verschiedenen Betriebssystemen

Dieselben Grundoperationen heißen je nach Betriebssystem anders. Während Unix-artige Systeme (Linux, macOS) weitgehend dieselben POSIX-Namen verwenden, nutzt Windows NT eine eigene Namenskonvention:

| Operation | Linux | Windows NT | macOS |
|-----------|-------|------------|-------|
| Prozess erzeugen | `fork`+`exec` | `CreateProcess` | `fork`+`exec` |
| Thread erzeugen | `clone` | `CreateThread` | `pthread_create` |
| Datei öffnen | `open` | `NtCreateFile` | `open` |
| Datei lesen | `read` | `NtReadFile` | `read` |
| Speicher allokieren | `mmap`/`brk` | `VirtualAlloc` | `mmap` |
| Prozess beenden | `exit` | `ExitProcess` | `exit` |
| Socket erstellen | `socket` | `WSASocket` | `socket` |

**Ungefähre Anzahl der Systemaufrufe:**

| System | Anzahl (ca.) |
|--------|--------------|
| Linux 6.x | ~450 |
| Windows 11 | ~500 (nicht dokumentiert) |
| FreeBSD | ~550 |
| macOS | ~500 |

---
author: Andreas Hümmer

## Die Wrapper-Bibliothek (libc/glibc)

Anwendungen rufen Systemaufrufe fast nie direkt auf, sondern über die C-Bibliothek (libc, unter Linux meist glibc). Sie kapselt die rohen Syscalls in bequeme, portable Funktionen und erledigt viel Arbeit bereits im User-Space.

![[.assets/libc-wrapper.png]]

*Am Beispiel `printf("Zahl: %d\n", 42)`: Die eigentliche Formatierung des Strings erledigt die libc vollständig im User-Space – ganz ohne Syscall. Erst die Ausgabe erfolgt über den dünnen `write()`-Wrapper, der die Register setzt, die SYSCALL-Instruktion ausführt und den Rückgabewert prüft. Im Kernel schreibt `sys_write()` die Daten schließlich ins Dateisystem oder Terminal.*

**Aufgaben der libc:**

- Bietet eine portable POSIX-API
- Kapselt architekturspezifische Syscall-Aufrufe
- Implementiert komplexe Funktionen im User-Space
- Setzt `errno` bei Fehlern
- Puffert I/O für bessere Performance (stdio)
- Bietet Komfortfunktionen (`fopen`, `fprintf`, `malloc`)

**Direkte Syscalls (ohne libc)** sind mit `syscall()` oder Inline-Assembler möglich:

```c
#include <sys/syscall.h>
long ret = syscall(SYS_write, 1, "Hello\n", 6);
```

---
author: Andreas Hümmer

## vDSO (Virtual Dynamic Shared Object)

**Problem:** Manche Systemaufrufe sind sehr häufig und klein – der Kontextwechsel kostet dann unverhältnismäßig viel:

- `gettimeofday()` – tausende Male pro Sekunde
- `clock_gettime()` – performance-kritisch
- `getcpu()` – Thread-Affinität

**Lösung:** Das **vDSO** ist ein kleiner Codebereich, den der Kernel direkt in den Adressraum jedes Prozesses einblendet. Für die betroffenen Funktionen muss die CPU dann gar nicht mehr in den Kernel wechseln.

![[.assets/vdso-schnelle-syscalls.png]]

*Ohne vDSO durchläuft selbst ein `gettimeofday()` den vollen Trap-Pfad in den Kernel und zurück. Mit vDSO liest die Funktion die Zeit direkt aus einem gemeinsamen Speicherbereich, den der Kernel regelmäßig aktualisiert – ganz ohne Kontextwechsel.*

**Ergebnis:** Kein Kontextwechsel, dadurch rund **10× schneller** als ein echter Systemaufruf.

---
author: Andreas Hümmer

## Syscall-Tracing und Debugging

Weil Systemaufrufe die Grenze zwischen Programm und Kernel markieren, sind sie ein idealer Beobachtungspunkt: Wer sehen will, was ein Programm *wirklich* tut – welche Dateien es öffnet, welche Netzwerkverbindungen es aufbaut –, verfolgt seine Syscalls. Dafür gibt es spezialisierte Werkzeuge.

### strace – Syscalls eines Prozesses verfolgen

`strace` zeigt alle Systemaufrufe, die ein Prozess absetzt, samt Argumenten und Rückgabewerten:

```text
$ strace ls -la
execve("/bin/ls", ["ls", "-la"], ...) = 0
brk(NULL)                             = 0x55a3b2c3d000
mmap(NULL, 8192, ...)                 = 0x7f2b3c5d2000
openat(AT_FDCWD, ".", O_RDONLY|...)   = 3
getdents64(3, ...)                    = 512
write(1, "drwxr-xr-x...", 45)         = 45
close(3)                              = 0
exit_group(0)                         = ?
```

Nützliche Optionen:

| Option | Wirkung |
|--------|---------|
| `-e trace=file` | Nur Datei-Syscalls |
| `-e trace=process` | Nur Prozess-Syscalls |
| `-e trace=network` | Nur Netzwerk-Syscalls |
| `-c` | Statistik am Ende |
| `-p PID` | An laufenden Prozess anhängen |
| `-f` | Auch Kindprozesse verfolgen |
| `-t` | Zeitstempel anzeigen |

### ltrace – Bibliotheksaufrufe verfolgen

`ltrace` arbeitet analog, verfolgt aber die Aufrufe von Bibliotheksfunktionen statt der rohen Syscalls:

```text
$ ltrace ls
__libc_start_main(...)
setlocale(LC_ALL, "")              = "de_DE.UTF-8"
bindtextdomain("coreutils", ...)   = "/usr/share/locale"
opendir(".")                       = 0x55a3b2c3e000
readdir(0x55a3b2c3e000)            = 0x55a3b2c3e020
```

---
author: Andreas Hümmer

## Sicherheitsaspekte

Da jeder Systemaufruf ein kontrollierter Übergang in den privilegierten Kernel ist, prüft der Kernel bei jedem Aufruf mehrere Dinge, bevor er ihn ausführt:

- **Berechtigungsprüfung** (UID, GID, Capabilities)
- **Parametervalidierung** (zeigt ein Pointer wirklich in den User-Space?)
- **Ressourcenlimits** (`rlimit`)
- **Mandatory Access Control** (SELinux, AppArmor)

### seccomp (Secure Computing Mode)

**seccomp** erlaubt es, die für einen Prozess zulässigen Syscalls einzuschränken – die Grundlage für Sandboxing. Es gibt zwei Modi:

| Modus | Verhalten |
|-------|-----------|
| **Strict** | Nur `read()`, `write()`, `exit()`, `sigreturn()` erlaubt |
| **Filter (BPF)** | Ein BPF-Programm entscheidet pro Syscall: `ALLOW`, `KILL`, `ERRNO`, `TRACE`, `LOG` |

> [!example] Praktischer Einsatz
> seccomp-Profile begrenzen die Angriffsfläche in **Containern** (Docker), **Browser-Sandboxes** (Chrome, Firefox) und **systemd-Services**.

### Capabilities (Linux)

Statt der groben Alles-oder-nichts-Rechte von `root` erlauben **Capabilities** eine feingranulare Vergabe einzelner Privilegien:

| Capability | Erlaubt |
|------------|---------|
| `CAP_NET_BIND_SERVICE` | Ports < 1024 binden |
| `CAP_NET_RAW` | Raw Sockets |
| `CAP_SYS_ADMIN` | Viele Admin-Operationen |
| `CAP_DAC_OVERRIDE` | Dateiberechtigungen umgehen |
| `CAP_KILL` | Signale an beliebige Prozesse senden |

---
author: Andreas Hümmer

## Praxisbeispiel: Minimaler HTTP-Server

Ein minimaler HTTP-Server zeigt die wichtigsten Syscalls im Zusammenspiel – ganz ohne Framework, nur mit der nackten POSIX-Socket-API:

```c
// Minimaler HTTP-Server nur mit Syscalls
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

int main() {
    // 1. Socket erstellen (socket)
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);

    // 2. Adresse binden (bind)
    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = INADDR_ANY
    };
    bind(server_fd, (struct sockaddr*)&addr, sizeof(addr));

    // 3. Lauschen (listen)
    listen(server_fd, 10);

    while (1) {
        // 4. Verbindung akzeptieren (accept)
        int client = accept(server_fd, NULL, NULL);

        // 5. Anfrage lesen (read)
        char buffer[1024];
        read(client, buffer, sizeof(buffer));

        // 6. Antwort senden (write)
        const char *response =
            "HTTP/1.1 200 OK\r\n"
            "Content-Length: 12\r\n\r\n"
            "Hello World!";
        write(client, response, strlen(response));

        // 7. Verbindung schließen (close)
        close(client);
    }
}
```

**Verwendete Syscalls:** `socket`, `bind`, `listen`, `accept`, `read`, `write`, `close`.

---
author: Andreas Hümmer

## Zusammenfassung

| Aspekt | Details |
|--------|---------|
| **Definition** | Schnittstelle zwischen User-Space und Kernel |
| **Mechanismus** | Trap/Interrupt → Kontextwechsel → Kernel-Handler |
| **Performance** | SYSCALL/SYSENTER ~20-50 Zyklen (früher INT 0x80 ~100-300) |
| **Kategorien** | Prozess, Datei, Speicher, Gerät, Kommunikation, Info |
| **POSIX** | Standardisierte API für Portabilität |
| **Sicherheit** | Berechtigungsprüfung, seccomp, Capabilities |

---
author: Andreas Hümmer

## Zusammenhänge

- → [[02-01-Kerneltypen|Kerneltypen]] - Syscalls als Schnittstelle zu verschiedenen Kernel-Architekturen
- → [[02-02-Schichtenmodell|Schichtenmodell]] - Syscalls als Schichtübergang
- → [[03-01-Prozessmodell|Prozessmodell]] - fork(), exec(), wait()
- → [[03-03-Threads|Threads]] - clone() und pthread
- → [[03-04-Interprozesskommunikation|IPC]] - pipe(), socket(), shmget()
- → [[05-01-Adressraeume|Adressräume]] - mmap(), brk()
- → [[07-01-Grundlagen|Dateisysteme]] - open(), read(), write()

### Betriebssystem-Referenzen

- → [[07-Anhang/Betriebssysteme/Linux|Linux]] - POSIX-kompatibel mit ~450 Syscalls
- → [[07-Anhang/Betriebssysteme/FreeBSD|FreeBSD]] - BSD-Syscall-Konventionen
- → [[07-Anhang/Betriebssysteme/Windows-NT|Windows NT]] - Native API (NtXxx-Funktionen)
- → [[07-Anhang/Betriebssysteme/UNIX|UNIX]] - Ursprung der Syscall-Konzepte

---
author: Andreas Hümmer

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
> - Unterschied User-Mode vs. Kernel-Mode


> [!question] **Häufige Prüfungsfragen**
> 1. Erklären Sie den Ablauf eines Systemaufrufs (mit Diagramm)
> 2. Warum ist ein Kontextwechsel bei Syscalls nötig?
> 3. Was ist der Unterschied zwischen User-Mode und Kernel-Mode?

> [!tip] **Merkhilfen**
> - **fork()** = Kopiere den Prozess (wie Zellteilung)
> - **exec()** = Ersetze das Programm (Metamorphose)
> - **File Descriptor** = Nummer für offene Datei (0=stdin, 1=stdout, 2=stderr)
> - **POSIX** = Portable Operating System Interface (Portabilität!)

---
author: Andreas Hümmer

## Quellen

- Tanenbaum, A. S.: Modern Operating Systems, 4th Edition, Kapitel 1.6
- Kerrisk, M.: The Linux Programming Interface, Kapitel 3
- Linux man-pages: syscalls(2), intro(2)
- Intel® 64 and IA-32 Architectures Software Developer's Manual
- Linux Kernel Source: arch/x86/entry/syscalls/
