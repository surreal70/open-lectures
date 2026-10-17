---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - angriffe
---

# Fehlerhafte Zufallszahlengeneratoren

> [!info] **Lernziele**
> - Verstehen, warum schwacher Zufall ganze Systeme kompromittiert
> - Reale RNG-Vorfälle einordnen
> - Gegenmaßnahmen kennen

---

## Inhalt

### Zufall ist ein Single Point of Failure

Fast jedes kryptographische Verfahren braucht Zufall – für Schlüssel, Nonces, IVs, Salts, Signatur-Nonces. Ist der Zufall **vorhersehbar**, bricht die Sicherheit zusammen, egal wie stark der Algorithmus ist (→ [[02-Sichere-Schluesselgenerierung]]).

### Reale Vorfälle

> [!warning] **Prüfungsrelevant: RNG-Desaster**
> - **Debian-OpenSSL (2008):** Ein Patch reduzierte die Entropie auf ~15 Bit → nur ~32.768 mögliche Schlüssel. Millionen Schlüssel waren vorhersagbar.
> - **Sony PlayStation 3 (2010):** **konstante** ECDSA-Nonce → der private Signaturschlüssel ließ sich direkt berechnen (→ [[03-ECDSA]]).
> - **Dual_EC_DRBG:** ein standardisierter RNG mit mutmaßlicher NSA-Hintertür.
> - **Schwache IoT-Schlüssel:** Geräte erzeugen Schlüssel beim ersten Boot ohne genug Entropie → viele teilen dieselben Primzahlen/Schlüssel.

### Warum passiert das?

- Verwendung **nicht-kryptographischer** PRNGs (vorhersagbar).
- **Zu wenig Entropie** beim Seeding (frisch gebootete oder embedded Systeme).
- **Wiederverwendung** von Zufallswerten (Nonce-Reuse → [[07-Nonce-Reuse-und-Schluesselwiederverwendung]]).

### Gegenmaßnahmen

> [!tip] **Richtige Zufallsquellen**
> - Immer den **OS-CSPRNG** nutzen (`getrandom()`, `/dev/urandom`, `BCryptGenRandom`) bzw. geprüfte Bibliotheken.
> - Vor der Schlüsselerzeugung auf **ausreichende Entropie** warten.
> - **Deterministische** Nonce-Verfahren einsetzen, wo sinnvoll (RFC 6979 für ECDSA, EdDSA von Haus aus).
> - Keine selbstgebauten RNGs oder `Math.random()`.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Schwacher Zufall kompromittiert jedes Verfahren, unabhängig vom Algorithmus
> - Reale Desaster: Debian-OpenSSL, PS3-ECDSA-Nonce, Dual_EC_DRBG, IoT-Schlüssel
> - Ursachen: Nicht-CSPRNG, zu wenig Entropie, Wiederverwendung
> - Abwehr: OS-CSPRNG, Entropie sicherstellen, deterministische Nonces (RFC 6979/EdDSA)

---

## Übungen

1. Warum ist der RNG ein Single Point of Failure in der Kryptographie?
2. Beschreiben Sie zwei reale RNG-Vorfälle.
3. Wie verhindert RFC 6979 den PS3-artigen ECDSA-Fehler?

---

← [[05-Side-Channel-Angriffe|← Zurück]] | [[00-Angriffe-Index|Übersicht]] | [[07-Nonce-Reuse-und-Schluesselwiederverwendung|Weiter →]]
