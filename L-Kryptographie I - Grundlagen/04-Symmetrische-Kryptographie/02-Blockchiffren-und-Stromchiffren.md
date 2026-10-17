---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - symmetrisch
---

# Blockchiffren und Stromchiffren

> [!info] **Lernziele**
> - Block- und Stromchiffren unterscheiden
> - Ihre Funktionsweise und typischen Einsatzgebiete kennen
> - Vor- und Nachteile beider Ansätze einordnen

---

## Inhalt

### Blockchiffren

Eine **Blockchiffre** verschlüsselt Daten in **festen Blöcken** fester Länge (bei AES 128 Bit). Jeder Block wird mit demselben Schlüssel durch dieselbe Transformation verarbeitet.

- Nachrichten, die nicht ein ganzzahliges Vielfaches der Blockgröße sind, brauchen **Padding** (→ [[08-Padding-Nonces-und-IVs]]).
- Für Nachrichten über einen Block hinaus ist ein **Betriebsmodus** nötig (→ [[05-Betriebsmodi-ECB-CBC-CTR-GCM]]).
- Beispiele: AES, DES/3DES.

Intern sind Blockchiffren oft als **iterierte Rundenchiffren** aufgebaut: dieselbe Rundenfunktion wird mehrfach mit Rundenschlüsseln angewandt. Zwei verbreitete Konstruktionen sind das **Feistel-Netzwerk** (DES) und das **Substitutions-Permutations-Netzwerk** (AES).

### Stromchiffren

Eine **Stromchiffre** erzeugt aus dem Schlüssel (und einer Nonce) einen pseudozufälligen **Schlüsselstrom**, der bit- oder byteweise per XOR mit dem Klartext verknüpft wird:

$$c_i = m_i \oplus s_i$$

- Keine Blockgröße, kein Padding nötig – ideal für Datenströme (z. B. Echtzeit-Kommunikation).
- Beispiele: ChaCha20 (→ [[06-ChaCha20-und-ChaCha20-Poly1305]]), historisch RC4 (unsicher).

> [!danger] **Schlüsselstrom nie wiederverwenden**
> Wird derselbe Schlüsselstrom für zwei Nachrichten genutzt, gilt $c_1 \oplus c_2 = m_1 \oplus m_2$ – der Schlüssel fällt heraus und der Angreifer gewinnt Information über die Klartexte. Deshalb ist pro Schlüssel eine eindeutige **Nonce** zwingend.

### Vergleich

| Merkmal | Blockchiffre | Stromchiffre |
|---------|--------------|--------------|
| Verarbeitung | feste Blöcke | kontinuierlicher Strom |
| Padding | oft nötig | nicht nötig |
| Typische Nutzung | Dateien, Datenbanken | Echtzeit, Netzwerk |
| Beispiel | AES | ChaCha20 |

Die Grenze verschwimmt: Eine Blockchiffre im **CTR-Modus** verhält sich effektiv wie eine Stromchiffre.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Blockchiffren verarbeiten feste Blöcke, brauchen Betriebsmodus und ggf. Padding
> - Stromchiffren XOR-en den Klartext mit einem Schlüsselstrom, kein Padding nötig
> - Schlüsselstrom/Nonce darf pro Schlüssel nie wiederholt werden
> - CTR-Modus macht aus einer Blockchiffre faktisch eine Stromchiffre

---

## Übungen

1. Warum benötigen Blockchiffren oft Padding, Stromchiffren aber nicht?
2. Was passiert, wenn ein Schlüsselstrom zweimal verwendet wird?
3. Nennen Sie je ein typisches Einsatzgebiet für Block- und Stromchiffren.

---

← [[01-Grundlagen-symmetrischer-Verschlüsselung|← Zurück]] | [[00-Symmetrisch-Index|Übersicht]] | [[03-DES-und-Triple-DES|Weiter →]]
