---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - standards
---

# Crypto Agility

> [!info] **Lernziele**
> - Das Konzept Crypto-Agility verstehen
> - Erkennen, warum sie zunehmend wichtig ist
> - Prinzipien agiler Krypto-Architektur kennen

---

## Inhalt

### Was ist Crypto-Agility?

**Crypto-Agility** ist die Fähigkeit eines Systems, kryptographische Verfahren (Algorithmen, Schlüssellängen, Protokolle) **auszutauschen, ohne die Architektur grundlegend umzubauen**. Ein krypto-agiles System kann auf neue Bedrohungen oder Standards schnell reagieren.

### Warum jetzt besonders wichtig?

> [!tip] **Treiber: Post-Quanten-Migration**
> Die anstehende Umstellung auf Post-Quanten-Verfahren (→ Modul 13) ist der aktuell größte Treiber für Crypto-Agility. Wer heute agil baut, kann ML-KEM/ML-DSA (und künftige Verfahren) einführen, ohne jedes System neu zu schreiben. Auch frühere Wechsel (DES→AES, SHA-1→SHA-2, RSA→ECC) zeigten den Bedarf.

### Prinzipien agiler Krypto-Architektur

- **Abstraktion:** Anwendungen rufen **Krypto-Dienste** über eine Schnittstelle auf, nicht direkt feste Algorithmen.
- **Konfigurierbarkeit:** Verfahren und Parameter sind konfigurierbar, nicht hartcodiert.
- **Algorithmus-Kennzeichnung:** Chiffretexte/Signaturen vermerken das verwendete Verfahren und die Version (z. B. „Algorithmus-ID"), damit alte Daten weiter lesbar bleiben.
- **Versionierung und Übergänge:** mehrere Verfahren parallel unterstützen (vgl. hybride PQC, → [[09-Hybride-kryptographische-Verfahren]]).
- **Zentrale Richtlinie:** erlaubte Verfahren an einer Stelle pflegen (→ [[08-Kryptographische-Richtlinien-in-Unternehmen]]).

### Spannungsfeld

> [!warning] **Agilität vs. Angriffsfläche**
> Mehr Flexibilität (viele verhandelbare Verfahren) kann die Angriffsfläche erhöhen (vgl. Downgrade-Angriffe → [[08-Downgrade-Angriffe]]). Crypto-Agility heißt daher nicht „alles erlauben", sondern **schnell und kontrolliert wechseln** können – mit sicheren Defaults und abgeschalteten Altverfahren.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Crypto-Agility = Verfahren austauschen können, ohne die Architektur neu zu bauen
> - Wichtigster aktueller Treiber: PQC-Migration
> - Prinzipien: Abstraktion, Konfigurierbarkeit, Algorithmus-Kennzeichnung, Versionierung, zentrale Richtlinie
> - Balance zu wahren: Agilität ja, aber ohne unnötige Angriffsfläche (keine Altverfahren)

---

## Übungen

1. Was bedeutet Crypto-Agility?
2. Warum ist sie im Kontext der PQC-Migration besonders relevant?
3. Welcher Zielkonflikt besteht zwischen Agilität und Angriffsfläche?

---

← [[06-DSGVO-und-Verschluesselung|← Zurück]] | [[00-Standards-Index|Übersicht]] | [[08-Kryptographische-Richtlinien-in-Unternehmen|Weiter →]]
