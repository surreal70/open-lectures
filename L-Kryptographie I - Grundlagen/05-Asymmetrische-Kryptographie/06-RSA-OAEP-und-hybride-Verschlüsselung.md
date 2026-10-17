---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - asymmetrisch
  - public-key
---

# RSA-OAEP und hybride Verschlüsselung

> [!info] **Lernziele**
> - Verstehen, warum RSA ein sicheres Padding wie OAEP braucht
> - Das Prinzip der hybriden Verschlüsselung nachvollziehen
> - Erkennen, wie asymmetrische und symmetrische Verfahren zusammenspielen

---

## Inhalt

### Warum RSA-OAEP?

„Textbook-RSA" ohne Padding ist unsicher: Es ist deterministisch und besitzt mathematische Strukturen (Homomorphie), die Angriffe ermöglichen (→ [[02-RSA-Funktionsweise-und-Sicherheit]]).

**OAEP (Optimal Asymmetric Encryption Padding)** behebt das: Es mischt die Nachricht vor der RSA-Operation mit Zufall und Hashfunktionen, sodass

- die Verschlüsselung **probabilistisch** wird (gleiche Nachricht → unterschiedliche Chiffretexte),
- die mathematische Struktur zerstört wird,
- das Verfahren beweisbar **IND-CCA**-Sicherheit erreicht (→ [[05-Kryptographische-Angriffsmodelle]]).

Für neue Anwendungen gilt: RSA-Verschlüsselung **nur** mit OAEP (das ältere PKCS#1 v1.5 ist anfällig für Bleichenbacher-Angriffe).

### Das Problem der direkten RSA-Verschlüsselung

RSA kann nur Daten verschlüsseln, die **kleiner als der Modul** sind – bei RSA-2048 also wenige hundert Byte. Große Dateien direkt mit RSA zu verschlüsseln ist sowohl **unmöglich** (Größenlimit) als auch **viel zu langsam**.

### Hybride Verschlüsselung

Die Lösung kombiniert beide Welten:

```
1. Zufälligen symmetrischen Sitzungsschlüssel K erzeugen
2. Nutzdaten schnell mit AES-GCM unter K verschlüsseln
3. K selbst mit RSA-OAEP (öffentlicher Schlüssel des Empfängers) verschlüsseln
4. Senden: [RSA-OAEP(K)] + [AES-GCM(Daten)]

Empfänger:
1. K mit privatem RSA-Schlüssel entschlüsseln
2. Daten mit K (AES-GCM) entschlüsseln
```

So vereint man die Stärken: RSA löst den **Schlüsselaustausch**, AES übernimmt die **schnelle Massenverschlüsselung**. Genau dieses Prinzip steckt hinter TLS, PGP/GPG und verschlüsselten Dateiformaten.

> [!tip] **KEM – moderne Sicht**
> Der moderne Begriff dafür ist **KEM/DEM** (Key Encapsulation Mechanism + Data Encapsulation Mechanism). Auch die Post-Quanten-Verfahren (z. B. ML-KEM, → Modul 13) folgen diesem Muster: Sie kapseln einen symmetrischen Schlüssel, der dann die Daten schützt.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - OAEP macht RSA probabilistisch und IND-CCA-sicher – Pflicht statt Textbook-RSA
> - RSA kann nur kleine Datenmengen direkt verschlüsseln und ist langsam
> - Hybride Verschlüsselung: RSA-OAEP kapselt einen AES-Sitzungsschlüssel
> - Prinzip KEM/DEM – auch Grundlage der Post-Quanten-Verfahren

---

## Übungen

1. Welche zwei Probleme löst OAEP gegenüber Textbook-RSA?
2. Warum verschlüsselt man große Dateien nicht direkt mit RSA?
3. Beschreiben Sie die Schritte einer hybriden Verschlüsselung.

---

← [[05-ECDH-und-X25519|← Zurück]] | [[00-Asymmetrisch-Index|Übersicht]] | [[07-Schlüssellängen-und-Sicherheitsniveaus|Weiter →]]
