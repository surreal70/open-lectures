---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Key Derivation Functions KDF

> [!info] **Lernziele**
> - Zweck von Key Derivation Functions verstehen
> - Verschiedene KDF-Typen und ihre Einsatzgebiete unterscheiden
> - KDFs von Passwort-Hashing abgrenzen

---

## Inhalt

### Was ist eine KDF?

Eine **Key Derivation Function (KDF)** leitet aus einem Eingabegeheimnis einen oder mehrere kryptographisch starke Schlüssel ab. Typische Aufgaben:

- aus einem Diffie-Hellman-Ergebnis einen Sitzungsschlüssel gewinnen,
- aus einem Masterschlüssel mehrere Zweck-Schlüssel ableiten,
- aus einem Passwort einen Schlüssel erzeugen.

### Zwei Kategorien

**1. KDFs für hochentropische Eingaben** (z. B. DH-Ergebnisse):

- **HKDF** (HMAC-based KDF, RFC 5869) ist der Standard. Es arbeitet in zwei Schritten:
  - **Extract:** gleicht die Eingabe zu gleichmäßigem Schlüsselmaterial aus.
  - **Expand:** erzeugt daraus so viele Schlüssel beliebiger Länge wie nötig.

**2. KDFs für niedrigentropische Eingaben** (Passwörter) – absichtlich **langsam**:

- **PBKDF2, scrypt, Argon2** (→ [[06-Passwort-Hashing-PBKDF2-bcrypt-scrypt-Argon2id]]).

### Warum unterscheiden?

> [!warning] **Prüfungsrelevant: richtige KDF wählen**
> - Für **hohe Entropie** (Schlüssel, DH-Ergebnisse): schnelle KDF wie **HKDF**.
> - Für **niedrige Entropie** (Passwörter): absichtlich langsame, speicherharte KDF wie **Argon2**.
> Eine schnelle KDF auf ein Passwort anzuwenden wäre unsicher; eine langsame KDF auf einen DH-Schlüssel wäre unnötig teuer.

### Kontext und Salt

Gute KDFs binden einen **Kontext/Info-Parameter** und einen **Salt** ein, damit aus demselben Eingabegeheimnis für unterschiedliche Zwecke **verschiedene**, unabhängige Schlüssel entstehen (Schlüsseltrennung).

```
sessionKey = HKDF(sharedSecret, salt, info="tls13 session key", length=32)
```

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - KDFs leiten starke Schlüssel aus einem Geheimnis ab
> - Hohe Entropie → schnelle KDF (HKDF: Extract-then-Expand)
> - Niedrige Entropie (Passwörter) → langsame KDF (PBKDF2/scrypt/Argon2)
> - Salt und Kontextparameter sorgen für Schlüsseltrennung

---

## Übungen

1. Wozu dient der Extract-Schritt von HKDF?
2. Welche KDF-Art verwendet man für ein Passwort, welche für ein DH-Ergebnis?
3. Welche Rolle spielt der Info-/Kontextparameter?

---

← [[03-Schluesselverteilung-und-Speicherung|← Zurück]] | [[00-Schluessel-Index|Übersicht]] | [[05-Key-Rotation-und-Key-Revocation|Weiter →]]
