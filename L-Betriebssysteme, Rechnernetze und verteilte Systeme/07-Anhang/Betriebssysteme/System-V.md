---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# System V (Unix)

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | AT&T Bell Labs |
| **Erstveröffentlichung** | 1983 |
| **Letzte Version** | Release 4 (SVR4, 1988) |
| **Lizenz** | Proprietär |
| **Einfluss** | Solaris, HP-UX, AIX, SCO Unix |

## Zusammenfassung

System V (ausgesprochen "System Five") war die kommerziell bedeutendste Unix-Variante von AT&T. SVR4 vereinigte Features von BSD, SunOS und Xenix und wurde zur Basis der meisten kommerziellen Unix-Systeme.

### Hauptmerkmale

| Feature | Beschreibung |
|---------|--------------|
| **Init-System** | SysV init mit Runlevels (0-6) |
| **IPC** | Semaphore, Shared Memory, Message Queues |
| **Streams** | I/O-Framework für Netzwerke |
| **Curses** | Terminal-UI-Bibliothek |
| **ELF** | Executable and Linkable Format (ab SVR4) |

### Versionsgeschichte

| Version | Jahr | Neuerungen |
|---------|------|------------|
| System III | 1981 | Erste kommerzielle AT&T-Version |
| SVR1 | 1983 | Erste System V Release |
| SVR2 | 1984 | IPC, Shell-Funktionen |
| SVR3 | 1987 | STREAMS, shared libraries |
| SVR4 | 1988 | Vereinigung mit BSD, TCP/IP, NFS |

### System V vs. BSD

```
Unix-Stammbaum 1980er
                     ┌─────────────┐
                     │   UNIX V7   │
                     │   (1979)    │
                     └──────┬──────┘
              ┌─────────────┴─────────────┐
              │                           │
       ┌──────▼──────┐             ┌──────▼──────┐
       │  System V   │             │    BSD      │
       │  (AT&T)     │             │ (Berkeley)  │
       └──────┬──────┘             └──────┬──────┘
              │                           │
     ┌────────┼────────┐        ┌────────┼────────┐
     │        │        │        │        │        │
  HP-UX    AIX    Solaris    FreeBSD  NetBSD  OpenBSD
```

### Derivate

- [[Solaris]] (Sun Microsystems)
- [[HP-UX]] (Hewlett-Packard)
- [[AIX]] (IBM)
- [[IRIX]] (SGI)
- [[Xenix]] (Microsoft/SCO)
- [[SINIX]] (Siemens)
- [[SCO-Unix]]

## Siehe auch

- [[UNIX]]
- [[BSD]]

## Quellen

- [The Evolution of the Unix Time-sharing System (Dennis Ritchie)](https://www.bell-labs.com/usr/dmr/www/hist.html)
- [UNIX System V Release 4 (USL)](https://archive.org/details/unix-system-v-release-4)
- [Wikipedia: UNIX System V](https://en.wikipedia.org/wiki/UNIX_System_V)
