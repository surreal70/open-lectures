---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Windows 2000

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | 32-bit NT-Betriebssystem |
| **Entwickler** | Microsoft |
| **Erstveröffentlichung** | 17. Februar 2000 |
| **Support-Ende** | 13. Juli 2010 |
| **Lizenz** | Proprietär |
| **Kernel** | NT 5.0 |

## Zusammenfassung

Windows 2000 war der Nachfolger von Windows NT 4.0 und brachte Active Directory, Plug-and-Play und erhebliche Stabilitätsverbesserungen. Es bildete die technische Basis für Windows XP.

### Editionen

| Edition | Zielgruppe |
|---------|------------|
| **Professional** | Workstations, Desktops |
| **Server** | Kleine Server |
| **Advanced Server** | Cluster, Failover |
| **Datacenter Server** | Großrechner, 32 CPUs |

### Wichtige Neuerungen

| Feature | Beschreibung |
|---------|--------------|
| **Active Directory** | LDAP-basierter Verzeichnisdienst |
| **Plug and Play** | Automatische Hardware-Erkennung |
| **WDM** | Windows Driver Model |
| **EFS** | Encrypting File System |
| **Kerberos** | Sichere Authentifizierung |
| **IntelliMirror** | Desktop-Management |

### Active Directory

```
Active Directory Struktur
┌─────────────────────────────────────┐
│            Forest                   │
│  ┌───────────────────────────────┐  │
│  │         Domain                │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │   Organizational Unit   │  │  │
│  │  │  ┌─────┐ ┌─────┐       │  │  │
│  │  │  │User │ │Group│       │  │  │
│  │  │  └─────┘ └─────┘       │  │  │
│  │  │  ┌─────────┐           │  │  │
│  │  │  │Computer │           │  │  │
│  │  │  └─────────┘           │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

### Stabilität

Windows 2000 galt als sehr stabil:
- Durchschnittliche Uptime in Tests: 6+ Monate
- Deutlich weniger Bluescreens als NT 4.0
- Besseres Speichermanagement

### Übergang zu Consumer

Microsoft plante ursprünglich, Windows 2000 auch im Consumer-Markt einzuführen. Diese Pläne wurden zu Windows XP, das die NT-Basis mit Consumer-Features vereinte.

## Siehe auch

- [[Windows-NT]]
- [[Windows-XP]]
- [[Windows-ME]]

## Quellen

- [Windows 2000 Resource Kit](https://archive.org/details/windows2000resourcekit)
- [Microsoft Docs: Windows 2000](https://learn.microsoft.com/en-us/previous-versions/windows/)
- [Wikipedia: Windows 2000](https://en.wikipedia.org/wiki/Windows_2000)
