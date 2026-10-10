---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Xenix

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Unix-Betriebssystem |
| **Entwickler** | Microsoft, später SCO |
| **Erstveröffentlichung** | 1980 |
| **Letzte Version** | 2.3.4 (1992) |
| **Lizenz** | Proprietär |
| **Basis** | AT&T UNIX Version 7 |

## Zusammenfassung

Xenix war Microsofts Unix-Implementierung und in den 1980er Jahren das meistinstallierte Unix-System weltweit. Microsoft lizenzierte Unix von AT&T und portierte es zunächst auf Z8000, später auf 8086/286/386.

### Geschichte

| Jahr | Ereignis |
|------|----------|
| 1979 | Microsoft lizenziert UNIX V7 |
| 1980 | Xenix für Z8000 |
| 1983 | Xenix für IBM PC (8086) |
| 1985 | Xenix 286 für AT-Kompatible |
| 1987 | Microsoft verkauft Xenix an SCO |
| 1989 | SCO Xenix für 386 |

### Warum nicht MS-UNIX?

Microsoft durfte den Namen "UNIX" nicht verwenden (Markenrecht AT&T), daher der Name "Xenix". Das System war auf günstigerer Hardware lauffähig als andere Unix-Versionen und ermöglichte Multi-User-Betrieb auf PCs.

### Technische Merkmale

- Lief auf 8086 mit nur 256 KB RAM
- Multi-User-Betrieb mit Terminals
- Volle UNIX-Kompatibilität
- Später System V-kompatibel
- 386-Version mit Protected Mode

### Verbreitung

```
Xenix Marktanteil ~1985
┌────────────────────────────────────┐
│ Xenix         ████████████  45%    │
│ BSD variants  ██████        22%    │
│ System V      █████         18%    │
│ Andere        ████          15%    │
└────────────────────────────────────┘
(geschätzte installierte Basis)
```

### Ende und Vermächtnis

Nach dem Verkauf an SCO konzentrierte sich Microsoft auf OS/2 (mit IBM) und später Windows NT. SCO führte Xenix als SCO UNIX weiter.

## Siehe auch

- [[System-V]]
- [[SCO-Unix]]
- [[MS-DOS]]
- [[UNIX]]

## Quellen

- [Microsoft Xenix History](https://www.microsoft.com/en-us/research/publication/xenix-and-the-history-of-microsoft/)
- [The SCO Group History](https://archive.org/details/sco-history)
- [Wikipedia: Xenix](https://en.wikipedia.org/wiki/Xenix)
