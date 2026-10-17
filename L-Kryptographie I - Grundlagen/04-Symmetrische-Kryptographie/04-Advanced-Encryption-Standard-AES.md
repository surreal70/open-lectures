---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - symmetrisch
---

# Advanced Encryption Standard AES

> [!info] **Lernziele**
> - Herkunft und Bedeutung von AES verstehen
> - Den inneren Aufbau (SPN, Runden, Transformationen) nachvollziehen
> - Schlüssellängen und Sicherheitsstatus einordnen

---

## Inhalt

### Herkunft

**AES (Advanced Encryption Standard)** entstand aus einem offenen NIST-Wettbewerb (1997–2001). Gewinner war der Algorithmus **Rijndael** der belgischen Kryptographen **Joan Daemen** und **Vincent Rijmen**. AES ist heute die weltweit meistgenutzte symmetrische Chiffre und in moderner CPU-Hardware (AES-NI) direkt implementiert.

### Eckdaten

| Parameter | Wert |
|-----------|------|
| Blockgröße | 128 Bit (16 Byte) |
| Schlüssellängen | 128, 192 oder 256 Bit |
| Runden | 10 (AES-128), 12 (AES-192), 14 (AES-256) |
| Struktur | Substitutions-Permutations-Netzwerk (SPN) |

Der 128-Bit-Block wird als $4 \times 4$-Byte-Matrix („State") verarbeitet.

### Die vier Transformationen pro Runde

Jede Runde (außer kleineren Abweichungen in erster/letzter) kombiniert vier Schritte, die Confusion und Diffusion umsetzen:

1. **SubBytes** – nichtlineare Byte-Substitution über eine S-Box (Confusion). Mathematisch basiert sie auf der Inversen im Körper $\mathrm{GF}(2^8)$ (→ [[04-Gruppen-Ringe-und-endliche-Koerper]]).
2. **ShiftRows** – zyklisches Verschieben der Zeilen (Diffusion).
3. **MixColumns** – spaltenweise Matrixmultiplikation in $\mathrm{GF}(2^8)$ (Diffusion).
4. **AddRoundKey** – XOR mit dem aus dem Hauptschlüssel abgeleiteten Rundenschlüssel.

Die Rundenschlüssel entstehen durch die **Schlüsselexpansion (Key Schedule)**.

### Sicherheit

AES gilt als **sicher**: Es sind keine praktikablen Angriffe bekannt, die wesentlich besser als Brute Force sind. Theoretische Related-Key-Angriffe auf AES-256 haben keine praktische Relevanz.

> [!note] **Wichtig: AES allein genügt nicht**
> AES verschlüsselt nur einen einzelnen 128-Bit-Block. Für reale Nachrichten braucht es einen **Betriebsmodus** (→ [[05-Betriebsmodi-ECB-CBC-CTR-GCM]]) und zur Manipulationssicherung **Authenticated Encryption** (→ [[07-Authenticated-Encryption-AEAD]]). Die häufigsten realen AES-Schwachstellen liegen nicht im Algorithmus, sondern in falscher Modus-Wahl oder Nonce-Fehlern.

> [!tip] **Post-Quanten**
> Gegen Quantencomputer (Grover-Algorithmus) halbiert sich die effektive Sicherheit. Daher gilt **AES-256** als quantenresistente Wahl mit ~128 Bit Sicherheit (→ Modul 13).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - AES = Rijndael, Sieger des offenen NIST-Wettbewerbs, heutiger Standard
> - 128-Bit-Block, Schlüssel 128/192/256 Bit, SPN mit 10/12/14 Runden
> - Vier Rundenschritte: SubBytes, ShiftRows, MixColumns, AddRoundKey
> - Algorithmus sicher; Risiken liegen in Betriebsmodus/Nonce; AES-256 ist quantenresistent

---

## Übungen

1. Welche Schlüssellängen und Rundenzahlen kennt AES?
2. Ordnen Sie die vier Rundentransformationen den Prinzipien Confusion/Diffusion zu.
3. Warum ist AES allein noch keine vollständige Verschlüsselungslösung?

---

← [[03-DES-und-Triple-DES|← Zurück]] | [[00-Symmetrisch-Index|Übersicht]] | [[05-Betriebsmodi-ECB-CBC-CTR-GCM|Weiter →]]
