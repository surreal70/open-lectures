---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
  - sicherheit
  - angriffsmodelle
---

# Kryptographische Angriffsmodelle

> [!info] **Lernziele**
> - Die verschiedenen Angriffsmodelle verstehen
> - Sicherheitsniveaus einschätzen können
> - Die Bedeutung des Angriffsmodells für die Sicherheitsbewertung kennen

---

## Inhalt

Ein **Angriffsmodell** legt fest, welche Fähigkeiten ein Angreifer besitzt. Die Sicherheit eines Verfahrens kann immer nur **relativ zu einem Angriffsmodell** bewertet werden. Die folgenden Modelle sind nach aufsteigender Angreiferstärke geordnet: Wer gegen ein stärkeres Modell sicher ist, ist es auch gegen alle schwächeren.

### Ciphertext-Only Attack (COA)

Der Angreifer kennt **nur den Chiffretext** (bzw. mehrere Chiffretexte) und versucht daraus Klartext oder Schlüssel zu gewinnen.

- Schwächstes Modell – entspricht dem passiven Abhören einer Leitung.
- Historisches Beispiel: Häufigkeitsanalyse gegen die Caesar- oder Vigenère-Chiffre.
- Ein modernes Verfahren, das hiergegen nicht sicher ist, gilt als völlig unbrauchbar.

### Known-Plaintext Attack (KPA)

Der Angreifer kennt zusätzlich **Paare aus Klartext und zugehörigem Chiffretext** und will daraus auf den Schlüssel oder weitere Klartexte schließen.

- Realistisch, da Nachrichten oft vorhersehbare Teile enthalten (Dateikopf, Briefformeln, Protokoll-Header).
- Historisches Beispiel: In Bletchley Park nutzte man vermutete Standardphrasen („Cribs") der Enigma-Funksprüche.

### Chosen-Plaintext Attack (CPA)

Der Angreifer kann sich **selbst gewählte Klartexte verschlüsseln lassen** und die resultierenden Chiffretexte beobachten.

- Modelliert Situationen, in denen der Angreifer ein Verschlüsselungs-„Orakel" nutzen kann (z. B. ein Server, der eingereichte Daten verschlüsselt).
- Konsequenz: Verschlüsselung muss **probabilistisch** sein (per IV/Nonce), sonst erkennt der Angreifer identische Klartexte an identischen Chiffretexten.

### Chosen-Ciphertext Attack (CCA)

Der Angreifer kann sich **selbst gewählte Chiffretexte entschlüsseln lassen** (außer dem eigentlichen Zielchiffretext) und aus den Reaktionen Rückschlüsse ziehen.

- Praxisrelevant durch **Padding-Oracle-Angriffe**: Ein Server, der verrät, ob ein entschlüsselter Chiffretext ein gültiges Padding hatte, liefert dem Angreifer genau dieses Orakel.
- Starkes, aber realistisches Modell für interaktive Systeme.

### Adaptive Angriffe

Beim **adaptiven** Chosen-Ciphertext-Angriff (**CCA2**) darf der Angreifer seine Anfragen **schrittweise an bisherige Antworten anpassen** – er agiert interaktiv statt alle Anfragen vorab festzulegen.

- Stärkstes der gängigen Standardmodelle.
- Moderne Verschlüsselung soll CCA2-Sicherheit bieten; dies erreicht man in der Praxis durch **Authenticated Encryption** (z. B. AES-GCM, ChaCha20-Poly1305), die manipulierte Chiffretexte erkennt und ablehnt.

### Sicherheitsdefinitionen

Formal koppelt man Angriffsmodelle an **Ununterscheidbarkeit (Indistinguishability, IND)**. Im zugrunde liegenden Spiel wählt der Angreifer zwei gleich lange Klartexte; einer wird zufällig verschlüsselt, und der Angreifer soll erraten, welcher es war. Gelingt ihm das nur mit vernachlässigbar besserer Wahrscheinlichkeit als Raten, gilt das Verfahren als sicher.

| Definition | Bedeutung |
|------------|-----------|
| **IND-CPA** | Ununterscheidbarkeit unter Chosen-Plaintext-Angriff; Mindeststandard für Vertraulichkeit |
| **IND-CCA(2)** | Ununterscheidbarkeit unter (adaptivem) Chosen-Ciphertext-Angriff; heutiger Zielstandard |

> [!example] Zuordnung
> - Deterministische Chiffren (gleicher Klartext → gleicher Chiffretext) sind **nicht** IND-CPA-sicher.
> - AES im CBC-Modus ohne Integritätsschutz ist anfällig für Padding-Oracle-Angriffe und damit **nicht** IND-CCA-sicher.
> - AES-GCM (Authenticated Encryption) erfüllt IND-CCA.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Stärkere Angriffsmodelle ⇒ höhere Sicherheitsanforderungen
> - Moderne Verfahren müssen CCA-sicher sein
> - Das Angriffsmodell bestimmt die Sicherheitsgarantien

---

## Übungen

1. Ordnen Sie historische Angriffe den Modellen zu
2. Warum reicht CPA-Sicherheit in der Praxis oft nicht aus?

---

← [[04-Verschluesselung-Hashing-Kodierung-Signierung|← Zurück]] | [[00-Einfuehrung-Index|Übersicht]] | [[06-Kerckhoffs-Prinzip|Weiter →]]
