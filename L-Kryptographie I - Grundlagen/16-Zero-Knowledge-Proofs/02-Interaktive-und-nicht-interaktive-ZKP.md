---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - zkp
  - vertiefung
---

# Interaktive und nicht-interaktive ZKP

> [!info] **Lernziele**
> - Interaktive und nicht-interaktive ZKP unterscheiden
> - Die Fiat-Shamir-Heuristik verstehen
> - Die praktischen Vorteile nicht-interaktiver Beweise einordnen

---

## Inhalt

### Interaktive ZKP

Beim **interaktiven** Zero-Knowledge-Proof findet ein **Dialog** zwischen Beweiser und Prüfer statt: mehrere Runden aus Herausforderung (Challenge) und Antwort (Response). Das Höhlen-Beispiel (→ [[01-Grundlagen-Zero-Knowledge-Proofs]]) ist interaktiv – erst viele Runden überzeugen den Prüfer.

Typischer Ablauf (Sigma-Protokoll):

```
1. Commitment  – Beweiser legt sich fest
2. Challenge   – Prüfer schickt Zufallswert
3. Response    – Beweiser antwortet passend zum Geheimnis
→ Prüfer akzeptiert oder nicht
```

Nachteil: beide Parteien müssen **gleichzeitig online** sein und mehrere Nachrichten austauschen.

### Nicht-interaktive ZKP (NIZK)

Ein **nicht-interaktiver** Beweis besteht aus **einer einzigen Nachricht**: Der Beweiser erzeugt den Beweis, jeder kann ihn später prüfen – ohne Dialog. Das ist für viele Anwendungen (Blockchain, Signaturen) essenziell.

### Die Fiat-Shamir-Heuristik

> [!tip] **Von interaktiv zu nicht-interaktiv**
> Die **Fiat-Shamir-Heuristik** verwandelt ein interaktives in ein nicht-interaktives Protokoll: Statt dass der Prüfer die Challenge schickt, berechnet der Beweiser sie selbst als **Hash** des Commitments (und des Kontexts). Da der Hash nicht vorhersehbar ist, kann der Beweiser nicht schummeln. Dieses Prinzip steckt auch hinter vielen Signaturverfahren (z. B. Schnorr, EdDSA).

### Einordnung

| Typ | Interaktion | Beispiel |
|-----|-------------|----------|
| interaktiv | Dialog, beide online | Sigma-Protokolle, Identifikation |
| nicht-interaktiv | ein Beweis, offline prüfbar | zk-SNARKs (→ [[03-zk-SNARKs]]), zk-STARKs (→ [[04-zk-STARKs]]) |

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Interaktive ZKP: mehrrundiger Dialog (Commitment–Challenge–Response), beide online
> - Nicht-interaktive ZKP (NIZK): ein einziger, später prüfbarer Beweis
> - Fiat-Shamir macht aus interaktiv nicht-interaktiv (Challenge = Hash)
> - zk-SNARKs/zk-STARKs sind nicht-interaktiv

---

## Übungen

1. Worin unterscheiden sich interaktive und nicht-interaktive ZKP?
2. Beschreiben Sie die drei Schritte eines Sigma-Protokolls.
3. Wie funktioniert die Fiat-Shamir-Heuristik?

---

← [[01-Grundlagen-Zero-Knowledge-Proofs|← Zurück]] | [[00-ZKP-Index|Übersicht]] | [[03-zk-SNARKs|Weiter →]]
