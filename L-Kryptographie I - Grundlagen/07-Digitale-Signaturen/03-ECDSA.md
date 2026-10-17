---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - signaturen
---

# ECDSA

> [!info] **Lernziele**
> - ECDSA als elliptische Signaturvariante verstehen
> - Die zentrale Bedeutung der Nonce $k$ erkennen
> - Reale Angriffe durch Nonce-Fehler einordnen

---

## Inhalt

### Was ist ECDSA?

**ECDSA (Elliptic Curve Digital Signature Algorithm)** ist die elliptische Variante des Signaturstandards DSA. Dank elliptischer Kurven (→ [[04-Elliptische-Kurven-Kryptographie-ECC]]) bietet es gleiche Sicherheit bei deutlich kürzeren Schlüsseln als RSA – daher ist es weit verbreitet (TLS-Zertifikate, Bitcoin/Ethereum, Smartcards).

### Funktionsweise (vereinfacht)

Zum Signieren einer Nachricht mit Hash $h$ und privatem Schlüssel $d$ auf einer Kurve mit Generatorpunkt $G$ (Ordnung $n$):

```
1. Zufällige Nonce k wählen (1 ≤ k < n)
2. R = k·G,   r = x-Koordinate von R (mod n)
3. s = k⁻¹ · (h + r·d)  mod n
4. Signatur = (r, s)
```

Geprüft wird mit dem öffentlichen Schlüssel $Q = d\cdot G$ über eine Rekonstruktion des Punktes $R$.

### Die kritische Rolle der Nonce $k$

> [!danger] **Nonce-Wiederverwendung bricht den privaten Schlüssel**
> Wird dieselbe Nonce $k$ für zwei verschiedene Nachrichten verwendet, kann ein Angreifer aus den beiden Signaturen den **privaten Schlüssel direkt berechnen**. Genau dieser Fehler führte 2010 zum Bruch der **Sony-PlayStation-3-Signatur** (konstante Nonce) und zu gestohlenen Bitcoin-Wallets. Die Nonce muss **einzigartig und unvorhersehbar** sein.

### Deterministisches ECDSA (RFC 6979)

Da fehlerhafte Zufallsgeneratoren eine große Gefahr sind, leitet **deterministisches ECDSA (RFC 6979)** die Nonce $k$ reproduzierbar aus Schlüssel und Nachrichten-Hash ab (per HMAC). Das eliminiert die Abhängigkeit von einem guten RNG, ohne die Sicherheit zu schwächen – heute die empfohlene Variante.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - ECDSA: elliptische Signatur, kurze Schlüssel, weit verbreitet (TLS, Kryptowährungen)
> - Signatur $(r, s)$ nutzt pro Signatur eine frische Nonce $k$
> - Nonce-Wiederverwendung oder -Vorhersagbarkeit legt den privaten Schlüssel offen
> - Deterministisches ECDSA (RFC 6979) vermeidet RNG-Risiken

---

## Übungen

1. Welche Werte bilden eine ECDSA-Signatur?
2. Was passiert bei Wiederverwendung der Nonce $k$?
3. Welchen Vorteil bietet deterministisches ECDSA nach RFC 6979?

---

← [[02-RSA-PSS|← Zurück]] | [[00-Signaturen-Index|Übersicht]] | [[04-EdDSA-und-Ed25519|Weiter →]]
