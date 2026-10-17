---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - grundlagen
  - terminologie
---

# Grundbegriffe und Terminologie

> [!info] **Lernziele**
> - Kryptographische Fachbegriffe korrekt verwenden
> - Zwischen Klartext, Chiffretext, Schlüssel und Algorithmus unterscheiden
> - Die Notation kryptographischer Systeme verstehen

---

## Inhalt

### Grundlegende Begriffe

Die Kryptographie beschreibt den Weg einer Nachricht vom lesbaren Original zur geschützten Form und zurück:

- **Klartext (Plaintext, `M`):** Die ursprüngliche, lesbare Nachricht.
- **Chiffretext (Ciphertext, `C`):** Die verschlüsselte, unlesbare Form.
- **Verschlüsselung (Encryption):** Die Umwandlung von Klartext in Chiffretext.
- **Entschlüsselung (Decryption):** Die Rückumwandlung von Chiffretext in Klartext.
- **Schlüssel (Key, `K`):** Der geheime Parameter, der Ver- und Entschlüsselung steuert.

```
          Schlüssel K                     Schlüssel K
              │                               │
              ▼                               ▼
  Klartext ──► [ Verschlüsselung ] ──► Chiffretext ──► [ Entschlüsselung ] ──► Klartext
     M                                    C                                     M
```

Zwei weitere zentrale Begriffe:

- **Kryptographie:** Das Entwerfen sicherer Verfahren.
- **Kryptoanalyse:** Das Brechen bzw. Analysieren dieser Verfahren. Beides zusammen bildet die **Kryptologie**.

### Schlüssel und Algorithmen

Man unterscheidet zwei grundlegende Familien:

| Merkmal | Symmetrisch | Asymmetrisch |
|---------|-------------|--------------|
| Schlüssel | **ein** gemeinsamer geheimer Schlüssel | **Schlüsselpaar**: öffentlich + privat |
| Ver-/Entschlüsselung | gleicher Schlüssel für beides | öffentlicher Schlüssel verschlüsselt, privater entschlüsselt |
| Geschwindigkeit | schnell | langsam (rechenintensiv) |
| Hauptproblem | Schlüsselaustausch | Vertrauen in die Zuordnung (Authentizität) |
| Beispiele | AES, ChaCha20 | RSA, ECC, Diffie-Hellman |

Die **Schlüssellänge** (in Bit) bestimmt die Größe des Schlüsselraums und damit den Aufwand eines Brute-Force-Angriffs. Wichtig: Schlüssellängen verschiedener Verfahren sind **nicht direkt vergleichbar** – ein 256-Bit-AES-Schlüssel bietet ein anderes Sicherheitsniveau als ein 256-Bit-RSA-Modul (RSA benötigt hier mindestens 3072 Bit).

### Kryptographische Primitive

Primitive sind die elementaren Bausteine, aus denen komplexere Protokolle zusammengesetzt werden:

- **Blockchiffre:** Verschlüsselt Daten in festen Blöcken (z. B. AES mit 128 Bit pro Block). Benötigt einen **Betriebsmodus** (z. B. CBC, GCM) für längere Nachrichten.
- **Stromchiffre:** Verschlüsselt Daten bit- oder byteweise durch Kombination mit einem Schlüsselstrom (z. B. ChaCha20).
- **Hashfunktion:** Bildet beliebig lange Eingaben auf einen festen Ausgabewert ab (Einwegfunktion, z. B. SHA-256).
- **MAC (Message Authentication Code):** Erzeugt mit einem geheimen Schlüssel eine Prüfsumme zur Integritäts- und Authentizitätssicherung (z. B. HMAC).

### Notation und Symbole

In der Fachliteratur hat sich eine kompakte Notation etabliert:

| Notation | Bedeutung |
|----------|-----------|
| $C = E(K, M)$ | Verschlüsselung von Klartext $M$ mit Schlüssel $K$ |
| $M = D(K, C)$ | Entschlüsselung von Chiffretext $C$ mit Schlüssel $K$ |
| $h = H(M)$ | Hashwert $h$ der Nachricht $M$ |
| $t = \text{MAC}(K, M)$ | Authentisierungs-Tag $t$ über $M$ mit Schlüssel $K$ |
| $(pk, sk)$ | Schlüsselpaar: öffentlich (public key) / privat (secret key) |

Für korrekte Verfahren gilt stets die **Korrektheitsbedingung** $D(K, E(K, M)) = M$: Was mit dem passenden Schlüssel verschlüsselt wurde, lässt sich auch wieder zum Original entschlüsseln.

Zwei häufig verwechselte Hilfswerte:

- **IV (Initialisierungsvektor):** Ein (oft öffentlicher) Startwert, der dafür sorgt, dass gleiche Klartexte unterschiedliche Chiffretexte ergeben.
- **Nonce (number used once):** Ein Wert, der pro Schlüssel nur **einmal** verwendet werden darf; eine Wiederverwendung kann die Sicherheit vollständig zerstören (z. B. bei Stromchiffren und GCM).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Präzise Terminologie ist in der Kryptographie essentiell
> - Unterscheidung zwischen Algorithmus und Protokoll
> - Standardnotation erleichtert die Kommunikation

---

## Übungen

1. Definieren Sie die Begriffe: Klartext, Chiffretext, Schlüssel, Nonce, IV
2. Erklären Sie den Unterschied zwischen Verschlüsselung und Kodierung

---

← [[01-Geschichte-der-Kryptographie|← Zurück]] | [[00-Einfuehrung-Index|Übersicht]] | [[03-Schutzziele|Weiter →]]
