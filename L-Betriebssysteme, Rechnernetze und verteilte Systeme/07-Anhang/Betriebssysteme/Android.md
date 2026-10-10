---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Android

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Mobiles Linux-Betriebssystem |
| **Entwickler** | Google (Open Handset Alliance) |
| **Erstveröffentlichung** | 23. September 2008 |
| **Aktuelle Version** | Android 15 (2024) |
| **Lizenz** | Apache 2.0 (AOSP), proprietäre Google-Dienste |
| **Basis** | Linux Kernel |

## Zusammenfassung

Android ist das weltweit meistgenutzte mobile Betriebssystem mit über 70% Marktanteil. Es basiert auf dem Linux-Kernel, verwendet aber eine eigene Runtime (ART) statt der GNU-Userland-Tools.

### Architektur

```
Android Software Stack
┌─────────────────────────────────────┐
│         System Apps                 │
│    (Phone, Contacts, Settings)      │
├─────────────────────────────────────┤
│       Application Framework         │
│  (Activity, Content, Notification)  │
├─────────────────────────────────────┤
│    Native Libraries │ Android Runtime│
│  (WebKit, OpenGL,   │    (ART)       │
│   SQLite, SSL)      │                │
├─────────────────────┴────────────────┤
│     HAL (Hardware Abstraction)       │
├─────────────────────────────────────┤
│           Linux Kernel              │
│   (Binder IPC, Power, Wakelocks)    │
└─────────────────────────────────────┘
```

### Versionsgeschichte (Codenames)

| Version | Codename | Jahr |
|---------|----------|------|
| 1.5 | Cupcake | 2009 |
| 2.2 | Froyo | 2010 |
| 4.0 | Ice Cream Sandwich | 2011 |
| 4.4 | KitKat | 2013 |
| 5.0 | Lollipop | 2014 |
| 6.0 | Marshmallow | 2015 |
| 8.0 | Oreo | 2017 |
| 10 | (keine Codenames mehr) | 2019 |
| 12 | Snow Cone (intern) | 2021 |
| 14 | Upside Down Cake (intern) | 2023 |

### Android Runtime (ART)

ART ersetzt seit Android 5.0 die Dalvik VM:
- Ahead-of-Time (AOT) Kompilierung
- Verbesserter Garbage Collector
- Profile-guided Compilation (PGC)

### Open Source vs. Google

```
Android Lizenzmodell
┌─────────────────────────────────────┐
│      Google Mobile Services         │
│   (Play Store, Maps, Gmail, etc.)   │
│          PROPRIETÄR                 │
├─────────────────────────────────────┤
│     Android Open Source Project     │
│            (AOSP)                   │
│         APACHE 2.0                  │
├─────────────────────────────────────┤
│         Linux Kernel                │
│           GPL v2                    │
└─────────────────────────────────────┘
```

### Derivate

- **LineageOS**: Community-ROM
- **GrapheneOS**: Sicherheitsfokussiert
- **/e/OS**: Privacy-fokussiert
- **Amazon Fire OS**: Kindle-Tablets
- **Wear OS**: Smartwatches
- **Android Automotive**: Fahrzeuge

## Siehe auch

- [[Linux]]
- [[iOS]]

## Quellen

- [Android Open Source Project](https://source.android.com/)
- [Android Developers](https://developer.android.com/)
- [Wikipedia: Android](https://en.wikipedia.org/wiki/Android_(operating_system))
