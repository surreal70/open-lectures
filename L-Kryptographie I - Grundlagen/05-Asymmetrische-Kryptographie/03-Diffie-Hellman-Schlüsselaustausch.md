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

# Diffie-Hellman-Schlüsselaustausch

> [!info] **Lernziele**
> - Den Diffie-Hellman-Schlüsselaustausch verstehen und durchrechnen
> - Das Problem des diskreten Logarithmus als Sicherheitsgrundlage erkennen
> - Die Anfälligkeit für Man-in-the-Middle-Angriffe einordnen

---

## Inhalt

### Das Problem

Zwei Parteien wollen über einen **unsicheren Kanal** einen gemeinsamen geheimen Schlüssel vereinbaren, ohne ihn jemals direkt zu übertragen. Genau das löst der **Diffie-Hellman-Schlüsselaustausch (DH, 1976)** – der erste praktikable Public-Key-Mechanismus.

### Funktionsweise

Öffentlich bekannt sind eine große Primzahl $p$ und ein Generator $g$.

```
Alice                           Bob
wählt geheim a                  wählt geheim b
A = g^a mod p   ───────────►
                ◄───────────    B = g^b mod p
s = B^a mod p                   s = A^b mod p
```

Beide berechnen denselben Wert, denn:

$$s = B^a = (g^b)^a = g^{ab} = (g^a)^b = A^b \pmod p$$

Der gemeinsame geheime Wert $s = g^{ab} \bmod p$ dient dann als symmetrischer Schlüssel. Übertragen werden nur $A$ und $B$ – niemals $a$, $b$ oder $s$.

### Durchgerechnetes Beispiel

```
p = 23, g = 5
Alice: a = 6  → A = 5^6  mod 23 = 8
Bob:   b = 15 → B = 5^15 mod 23 = 19
Alice: s = 19^6  mod 23 = 2
Bob:   s = 8^15  mod 23 = 2   ✓  gemeinsames Geheimnis = 2
```

### Sicherheitsgrundlage

Ein Angreifer kennt $p$, $g$, $A$ und $B$. Um $s$ zu berechnen, müsste er aus $A = g^a$ den Exponenten $a$ gewinnen – das **Problem des diskreten Logarithmus**, das für große $p$ als praktisch unlösbar gilt.

### Man-in-the-Middle-Schwäche

> [!danger] **DH ist nicht authentifiziert**
> Reines Diffie-Hellman schützt **nicht** vor einem Man-in-the-Middle: Ein Angreifer kann sich dazwischenschalten und mit beiden Seiten je ein eigenes Geheimnis aushandeln. DH muss daher mit **Authentifizierung** (Signaturen, Zertifikate) kombiniert werden – so geschieht es in TLS.

> [!tip] **Ephemeral DH und Forward Secrecy**
> Verwenden beide Seiten pro Sitzung **frische, kurzlebige** Schlüssel (ephemeral, DHE/ECDHE), erhält man **Perfect Forward Secrecy**: Ein später kompromittierter Langzeitschlüssel gibt vergangene Sitzungen nicht preis (→ Modul 9).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - DH vereinbart ein gemeinsames Geheimnis $g^{ab} \bmod p$ über einen offenen Kanal
> - Übertragen werden nur $g^a$ und $g^b$, nie die geheimen Exponenten
> - Sicherheit = Problem des diskreten Logarithmus
> - Ungeschützt anfällig für MitM → Authentifizierung nötig; ephemeral DH liefert Forward Secrecy

---

## Übungen

1. Führen Sie DH mit $p=11$, $g=2$, $a=4$, $b=3$ durch und bestimmen Sie $s$.
2. Welches mathematische Problem schützt den gemeinsamen Schlüssel?
3. Warum ist reines Diffie-Hellman gegen Man-in-the-Middle verwundbar?

---

← [[02-RSA-Funktionsweise-und-Sicherheit|← Zurück]] | [[00-Asymmetrisch-Index|Übersicht]] | [[04-Elliptische-Kurven-Kryptographie-ECC|Weiter →]]
