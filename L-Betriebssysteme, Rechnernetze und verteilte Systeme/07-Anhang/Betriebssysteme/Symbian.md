---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Symbian

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Mobiles Betriebssystem |
| **Entwickler** | Symbian Ltd., später Nokia |
| **Erstveröffentlichung** | 1997 (als EPOC32) |
| **Letzte Version** | Nokia Belle (2012) |
| **Lizenz** | Proprietär, später EPL |
| **Status** | Eingestellt |

## Zusammenfassung

Symbian war das dominierende Smartphone-Betriebssystem vor dem iPhone. Es lief auf Nokia-, Sony Ericsson- und Samsung-Geräten und erreichte zeitweise über 50% Marktanteil bei Smartphones.

### Marktanteil-Entwicklung

```
Smartphone-OS Marktanteile
2007: ████████████████████████  Symbian 63%
2009: █████████████████████     Symbian 47%
2011: ███████████               Symbian 27%
2013: █                         Symbian 0.6%

(Android und iOS übernahmen den Markt)
```

### Geschichte

| Jahr | Ereignis |
|------|----------|
| 1997 | EPOC32 (Psion) |
| 1998 | Symbian Ltd. gegründet |
| 2000 | Erstes Symbian-Phone (Ericsson R380) |
| 2002 | Nokia 7650 (erstes S60-Gerät) |
| 2008 | Nokia kauft Symbian komplett |
| 2010 | Open Source (Symbian Foundation) |
| 2011 | Nokia wechselt zu Windows Phone |
| 2013 | Letzte Symbian-Geräte |

### Plattformen

| Plattform | Hersteller | Beschreibung |
|-----------|------------|--------------|
| S60 | Nokia | Smartphones |
| UIQ | Sony Ericsson | Touch-Geräte |
| MOAP | NTT DoCoMo | Japan |

### Architektur

```
Symbian OS Architektur
┌─────────────────────────────────────────┐
│          Anwendungen                    │
│   (C++, Qt, Java ME, Web Runtime)       │
├─────────────────────────────────────────┤
│      Application Framework (S60/UIQ)    │
├─────────────────────────────────────────┤
│         Symbian OS Services             │
│   (Telephony, Messaging, PIM)           │
├─────────────────────────────────────────┤
│         Symbian OS Kernel (EKA2)        │
│       (Echtzeit-Mikrokernel)            │
├─────────────────────────────────────────┤
│              Hardware                   │
└─────────────────────────────────────────┘
```

### Technische Merkmale

| Feature | Beschreibung |
|---------|--------------|
| **EKA2** | Echtzeit-Kernel |
| **Client-Server** | Capability-basierte Sicherheit |
| **Active Objects** | Asynchrones Programmiermodell |
| **Descriptors** | Sichere Strings |

### Niedergang

Ursachen für das Ende:
- iPhone (2007) revolutionierte Smartphones
- Android bot offene Alternative
- Veraltete Benutzeroberfläche
- Schwierige Entwicklungsumgebung

## Siehe auch

- [[iOS]]
- [[Android]]

## Quellen

- [Symbian Foundation Archive](https://web.archive.org/web/2010*/symbian.org)
- [Wikipedia: Symbian](https://en.wikipedia.org/wiki/Symbian)
