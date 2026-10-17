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

# ECDH und X25519

> [!info] **Lernziele**
> - ECDH als elliptische Variante des Diffie-Hellman-Austauschs verstehen
> - X25519 als modernen, robusten Standard einordnen
> - Die praktischen Vorteile gegenüber klassischem DH kennen

---

## Inhalt

### ECDH – Elliptic Curve Diffie-Hellman

**ECDH** überträgt das Diffie-Hellman-Prinzip (→ [[03-Diffie-Hellman-Schlüsselaustausch]]) auf elliptische Kurven. Statt mit Exponenten modulo $p$ arbeitet man mit **Skalarmultiplikation** von Kurvenpunkten:

```
Alice                            Bob
privat: a                        privat: b
A = a·G   ───────────►
          ◄───────────           B = b·G
S = a·B                          S = b·A
```

Beide erhalten denselben Punkt, denn $a \cdot B = a \cdot (b \cdot G) = b \cdot (a \cdot G) = b \cdot A$. Aus einer Koordinate dieses gemeinsamen Punktes wird – meist über eine Schlüsselableitungsfunktion (KDF) – der symmetrische Schlüssel gewonnen.

Der Vorteil gegenüber klassischem DH: gleiche Sicherheit bei viel kürzeren Schlüsseln (→ [[04-Elliptische-Kurven-Kryptographie-ECC]]).

### X25519

**X25519** ist eine konkrete, besonders robuste ECDH-Variante über der Kurve **Curve25519** (Daniel J. Bernstein). Sie hat sich als De-facto-Standard durchgesetzt.

Besonderheiten:

- **Hohe Geschwindigkeit** und einfache, konstante-Zeit-Implementierung (resistent gegen Timing-Seitenkanäle).
- **Wenige Fallstricke:** Das Design vermeidet viele Fehlerquellen klassischer Kurven (z. B. ungültige Kurvenpunkte).
- **32-Byte-Schlüssel:** kompakt und schnell zu übertragen.

### Einsatz in der Praxis

X25519 ist der bevorzugte Schlüsselaustausch in **TLS 1.3**, **SSH**, **Signal** und **WireGuard**. In Kombination mit ephemeren Schlüsseln (ECDHE) liefert es **Perfect Forward Secrecy** (→ Modul 9).

> [!tip] **Namenskonvention**
> `X25519` bezeichnet den Schlüsselaustausch über Curve25519; `Ed25519` die zugehörige Signaturvariante (→ Modul 7). Beide beruhen auf derselben Kurve, dienen aber unterschiedlichen Zwecken.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ECDH ist Diffie-Hellman mit Punkt-Skalarmultiplikation auf elliptischen Kurven
> - Gemeinsames Geheimnis: $a\cdot B = b\cdot A = ab\cdot G$
> - X25519 (Curve25519) ist der moderne, robuste Standard – schnell, konstante Zeit
> - Einsatz in TLS 1.3, SSH, Signal, WireGuard; mit ECDHE Forward Secrecy

---

## Übungen

1. Wie berechnen Alice und Bob bei ECDH dasselbe Geheimnis?
2. Nennen Sie zwei Eigenschaften, die X25519 besonders robust machen.
3. Worin unterscheiden sich X25519 und Ed25519?

---

← [[04-Elliptische-Kurven-Kryptographie-ECC|← Zurück]] | [[00-Asymmetrisch-Index|Übersicht]] | [[06-RSA-OAEP-und-hybride-Verschlüsselung|Weiter →]]
