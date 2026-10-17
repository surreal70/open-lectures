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

# Public-Key-Kryptographie

> [!info] **Lernziele**
> - Das Prinzip asymmetrischer (Public-Key-)Kryptographie verstehen
> - Die Rollen von öffentlichem und privatem Schlüssel unterscheiden
> - Erkennen, wie Public-Key-Verfahren das Schlüsselaustauschproblem lösen

---

## Inhalt

### Die Grundidee

Die **Public-Key-Kryptographie** (1976 von Diffie und Hellman eingeführt) verwendet statt eines gemeinsamen Geheimnisses ein **Schlüsselpaar**:

- **Öffentlicher Schlüssel** $pk$ – frei verteilbar
- **Privater Schlüssel** $sk$ – streng geheim, verbleibt beim Besitzer

Beide hängen mathematisch zusammen, aber aus $pk$ lässt sich $sk$ praktisch nicht berechnen. Das löst das zentrale Problem symmetrischer Verfahren: Es muss **kein geheimer Schlüssel vorab ausgetauscht** werden.

### Zwei Anwendungsrichtungen

| Ziel | Verschlüsseln mit | Entschlüsseln/Prüfen mit |
|------|-------------------|--------------------------|
| **Vertraulichkeit** | öffentlichem Schlüssel des Empfängers | privatem Schlüssel des Empfängers |
| **Authentizität (Signatur)** | privatem Schlüssel des Senders | öffentlichem Schlüssel des Senders |

Für Vertraulichkeit verschlüsselt jeder mit dem **öffentlichen** Schlüssel des Empfängers – nur dieser kann mit seinem **privaten** Schlüssel entschlüsseln. Für Signaturen ist es genau umgekehrt (→ Modul 7).

### Mathematische Grundlage: Einwegfunktionen mit Falltür

Public-Key-Verfahren beruhen auf **Falltürfunktionen** (trapdoor functions): leicht in eine Richtung zu berechnen, praktisch unmöglich umzukehren – es sei denn, man kennt eine geheime „Falltür" (den privaten Schlüssel). Konkrete harte Probleme:

- **Faktorisierung** großer Zahlen → RSA (→ [[02-RSA-Funktionsweise-und-Sicherheit]])
- **Diskreter Logarithmus** → Diffie-Hellman (→ [[03-Diffie-Hellman-Schlüsselaustausch]]), ECC

### Vor- und Nachteile

- **Vorteil:** löst Schlüsselaustausch; $n$ Teilnehmer brauchen nur $n$ Schlüsselpaare statt $n(n-1)/2$ Schlüssel.
- **Nachteil:** deutlich **langsamer** als symmetrische Verfahren.

> [!tip] **Hybride Verschlüsselung**
> In der Praxis kombiniert man beide Welten: Public-Key tauscht einen symmetrischen Sitzungsschlüssel aus, die Nutzdaten verschlüsselt dann schnelles AES (→ [[06-RSA-OAEP-und-hybride-Verschlüsselung]]).

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Asymmetrisch = Schlüsselpaar aus öffentlichem und privatem Schlüssel
> - Vertraulichkeit: mit öffentlichem Schlüssel verschlüsseln; Signatur: mit privatem signieren
> - Basis sind Falltürfunktionen (Faktorisierung, diskreter Logarithmus)
> - Löst den Schlüsselaustausch, ist aber langsam → hybride Verschlüsselung

---

## Übungen

1. Warum muss bei Public-Key-Kryptographie kein geheimer Schlüssel vorab ausgetauscht werden?
2. Mit welchem Schlüssel verschlüsselt man eine vertrauliche Nachricht an Bob?
3. Was ist eine Falltürfunktion, und welche Rolle spielt der private Schlüssel?

---

← [[00-Asymmetrisch-Index|Übersicht]] | [[02-RSA-Funktionsweise-und-Sicherheit|Weiter →]]
