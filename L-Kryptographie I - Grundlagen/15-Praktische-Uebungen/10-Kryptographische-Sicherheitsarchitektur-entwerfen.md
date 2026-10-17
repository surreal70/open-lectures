---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - praxis
---

# Kryptographische Sicherheitsarchitektur entwerfen

> [!info] **Lernziele**
> - Das Wissen des Kurses in einem Architekturentwurf zusammenführen
> - Für ein Szenario passende Verfahren auswählen und begründen
> - Ein Abschlussprojekt strukturiert bearbeiten

---

## Inhalt

### Das Abschlussprojekt

Diese letzte Übung ist ein **Abschlussprojekt**: Du entwirfst für ein vorgegebenes Szenario eine vollständige kryptographische Sicherheitsarchitektur und begründest jede Wahl mit dem Gelernten.

### Beispiel-Szenario

> [!example] **Szenario: Gesundheits-App**
> Eine mobile App überträgt Patientendaten an einen Cloud-Server, speichert sie dort und erlaubt Ärzten den Zugriff. Entwirf die Kryptographie für Übertragung, Speicherung, Authentifizierung und Schlüsselmanagement.

### Leitfragen für den Entwurf

| Aspekt | Zu entscheiden | Verweis |
|--------|----------------|---------|
| **Transport** | Welche TLS-Version/Cipher? | [[01-TLS-1.2-und-TLS-1.3]] |
| **Data at Rest** | Welche Verschlüsselung in der DB/Storage? | [[06-Datenbankverschluesselung]] |
| **Ende-zu-Ende** | Sollen Daten für den Betreiber unlesbar sein? | [[04-Ende-zu-Ende-Verschluesselung]] |
| **Authentifizierung** | Signaturen/Zertifikate/mTLS? | [[07-Schluesselvereinbarung-und-Authentifizierung]] |
| **Schlüsselmanagement** | HSM/KMS, Rotation, Backup? | Modul 10 |
| **Passwörter** | Hashing-Verfahren? | [[06-Passwort-Hashing-PBKDF2-bcrypt-scrypt-Argon2id]] |
| **Zukunftssicherheit** | PQC/Crypto-Agility? | Modul 13, [[07-Crypto-Agility]] |
| **Compliance** | DSGVO, Standards? | Modul 14 |

### Vorgehen

1. **Bedrohungsmodell** erstellen: Wer greift an, was ist zu schützen? (→ Modul 20)
2. **Schutzziele** priorisieren (Vertraulichkeit, Integrität, Authentizität).
3. **Verfahren wählen** – moderne Defaults: TLS 1.3, AES-256-GCM/ChaCha20-Poly1305, Ed25519, Argon2id, ML-KEM hybrid.
4. **Schlüsselmanagement** festlegen (KMS/HSM, Rotation, Trennung).
5. **Begründen und dokumentieren** – jede Wahl mit Bezug zu Schutzzielen und Standards.

> [!tip] **Bewertungskriterien**
> Ein guter Entwurf nutzt **sichere Defaults**, vermeidet veraltete Verfahren, plant **Crypto-Agility** ein und begründet Entscheidungen nachvollziehbar – statt „möglichst viel Krypto" einzusetzen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Abschlussprojekt: vollständige Krypto-Architektur für ein Szenario entwerfen
> - Alle Ebenen abdecken: Transport, Speicherung, Auth, Schlüsselmanagement, Zukunft, Compliance
> - Vorgehen: Bedrohungsmodell → Schutzziele → Verfahren → Schlüsselmanagement → Begründung
> - Ziel sind sichere, begründete Defaults mit Crypto-Agility, nicht „viel Krypto"

---

## Übungen

1. Erstellen Sie für das Szenario ein kurzes Bedrohungsmodell.
2. Entwerfen Sie die Architektur entlang der Leitfragen und begründen Sie jede Wahl.
3. Benennen Sie, wo Sie Crypto-Agility und eine künftige PQC-Migration einplanen.

---

← [[09-Fehlkonfigurationen-identifizieren|← Zurück]] | [[00-Uebungen-Index|Übersicht]] | [[00-ZKP-Index|Nächstes Modul →]]
