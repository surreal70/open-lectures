---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Secret Sharing und Backup-Konzepte

> [!info] **Lernziele**
> - Das Prinzip von Secret Sharing verstehen
> - Shamir's Secret Sharing einordnen
> - Sichere Backup-Konzepte für Schlüssel kennen

---

## Inhalt

### Das Dilemma der Schlüssel-Backups

Ein geheimer Schlüssel muss zwei widersprüchliche Anforderungen erfüllen:

- **Verfügbarkeit:** Geht er verloren, sind alle damit geschützten Daten unwiederbringlich verloren.
- **Vertraulichkeit:** Eine Kopie erhöht das Risiko, dass er gestohlen wird.

Eine einfache Kopie „in den Safe" konzentriert das Risiko auf eine einzige Stelle. **Secret Sharing** löst dieses Dilemma eleganter.

### Shamir's Secret Sharing (SSS)

**Shamir's Secret Sharing** teilt ein Geheimnis in $n$ Teile („Shares") auf, von denen beliebige **$t$** (Schwellwert) ausreichen, um es zu rekonstruieren – weniger als $t$ verraten **nichts**.

```
Schema (t, n):  z. B. (3, 5)
  → 5 Shares verteilt, 3 beliebige rekonstruieren das Geheimnis
  → 2 oder weniger Shares geben null Information preis
```

Mathematisch beruht es auf **Polynominterpolation**: Das Geheimnis ist der konstante Term eines zufälligen Polynoms vom Grad $t-1$; jeder Share ist ein Punkt darauf. Mit $t$ Punkten ist das Polynom (und damit das Geheimnis) eindeutig bestimmt, mit weniger nicht.

### Anwendung

> [!tip] **Mehr-Augen-Prinzip**
> SSS realisiert ein **„m-of-n"**-Prinzip: Kein Einzelner kann allein an den Schlüssel, aber eine definierte Mehrheit kann ihn wiederherstellen. Einsatz z. B. bei Root-CA-Schlüsseln, Kryptowährungs-Treasuries oder HSM-Freischaltung (mehrere Admins nötig).

### Sichere Backup-Konzepte

- **Geografische Verteilung:** Shares an verschiedenen Orten lagern (kein Single Point of Failure).
- **Getrennte Verantwortliche:** verschiedene Personen/Rollen halten die Shares (Gewaltenteilung).
- **Verschlüsselte Backups:** falls doch eine Vollkopie nötig ist, nur verschlüsselt und mit separatem KEK (→ [[03-Schluesselverteilung-und-Speicherung]]).
- **Regelmäßige Wiederherstellungstests:** ein Backup, das nie getestet wurde, ist kein verlässliches Backup.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Schlüssel-Backups müssen Verfügbarkeit und Vertraulichkeit ausbalancieren
> - Shamir's Secret Sharing teilt ein Geheimnis in n Shares, t davon rekonstruieren es
> - Weniger als t Shares geben keinerlei Information preis (Polynominterpolation)
> - Backups: geografisch verteilt, getrennte Rollen, verschlüsselt, regelmäßig getestet

---

## Übungen

1. Welches Dilemma lösen Secret-Sharing-Verfahren?
2. Was bedeutet ein (3,5)-Schwellwertschema?
3. Warum geben weniger als $t$ Shares keine Information über das Geheimnis preis?

---

← [[08-Cloud-Key-Management-Services-KMS|← Zurück]] | [[00-Schluessel-Index|Übersicht]] | [[00-Praxis-Index|Nächstes Modul →]]
