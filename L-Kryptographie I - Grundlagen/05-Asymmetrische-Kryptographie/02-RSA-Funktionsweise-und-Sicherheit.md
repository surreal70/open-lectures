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

# RSA Funktionsweise und Sicherheit

> [!info] **Lernziele**
> - Die RSA-Schlüsselerzeugung Schritt für Schritt nachvollziehen
> - Ver-/Entschlüsselung und Signatur mit RSA verstehen
> - Sicherheitsgrundlage und praktische Fallstricke einordnen

---

## Inhalt

### Schlüsselerzeugung

RSA (Rivest, Shamir, Adleman, 1977) beruht auf der Schwierigkeit, große Zahlen zu faktorisieren. Die Schlüssel entstehen so:

1. Zwei große Primzahlen $p$ und $q$ wählen.
2. Modul berechnen: $n = p \cdot q$.
3. Eulersche Funktion: $\varphi(n) = (p-1)(q-1)$.
4. Öffentlichen Exponenten $e$ wählen mit $\gcd(e, \varphi(n)) = 1$ (üblich: $e = 65537$).
5. Privaten Exponenten als Inverses berechnen: $d \equiv e^{-1} \pmod{\varphi(n)}$ (mit erweitertem euklidischem Algorithmus, → [[03-Euklidischer-Algorithmus]]).

- **Öffentlicher Schlüssel:** $(n, e)$
- **Privater Schlüssel:** $(n, d)$

### Ver- und Entschlüsselung

$$C = M^e \bmod n \qquad M = C^d \bmod n$$

Die Korrektheit folgt aus dem Satz von Euler. Berechnet wird effizient per Square-and-Multiply (→ [[01-Zahlentheorie-und-modulare-Arithmetik]]).

### Durchgerechnetes Mini-Beispiel

```
p = 11, q = 13      → n = 143,  φ(n) = 10·12 = 120
e = 7   (gcd(7,120)=1)
d = 103 (da 7·103 = 721 = 6·120 + 1 ≡ 1 mod 120)

Verschlüsseln M = 9:  C = 9^7  mod 143 = 48
Entschlüsseln C = 48: M = 48^103 mod 143 = 9  ✓
```

### Signatur

RSA kann auch signieren – mit vertauschten Rollen: Der Sender „verschlüsselt" einen Hash mit seinem **privaten** Schlüssel, jeder prüft mit dem **öffentlichen** (→ Modul 7, insbesondere RSA-PSS).

### Sicherheit und Fallstricke

Die Sicherheit beruht darauf, dass aus $n$ die Faktoren $p, q$ nicht rückgewinnbar sind. Daraus folgt: $n$ muss groß genug sein (mind. **2048 Bit**, besser 3072).

> [!danger] **„Textbook-RSA" ist unsicher**
> Reines RSA ohne Padding ist deterministisch und angreifbar (gleiche Nachricht → gleicher Chiffretext, kleine Nachrichten, homomorphe Eigenschaft). In der Praxis **immer** mit einem sicheren Padding wie **OAEP** (Verschlüsselung) bzw. **PSS** (Signatur) verwenden (→ [[06-RSA-OAEP-und-hybride-Verschlüsselung]]).

> [!tip] **Quantenbedrohung**
> Der Shor-Algorithmus faktorisiert effizient auf einem Quantencomputer – RSA gilt daher als langfristig gefährdet (→ Modul 13).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Schlüssel: $n=pq$, $e$ öffentlich, $d \equiv e^{-1} \bmod \varphi(n)$ privat
> - Verschlüsseln $C=M^e \bmod n$, Entschlüsseln $M=C^d \bmod n$
> - Sicherheit = Faktorisierungsproblem; mind. 2048-Bit-Modul
> - Nie Textbook-RSA: immer OAEP/PSS-Padding; quantengefährdet

---

## Übungen

1. Führen Sie die RSA-Schlüsselerzeugung mit $p=5$, $q=11$, $e=3$ durch.
2. Warum ist Textbook-RSA ohne Padding unsicher?
3. Welche Schlüssellänge gilt heute als Mindestmaß, und warum?

---

← [[01-Public-Key-Kryptographie|← Zurück]] | [[00-Asymmetrisch-Index|Übersicht]] | [[03-Diffie-Hellman-Schlüsselaustausch|Weiter →]]
