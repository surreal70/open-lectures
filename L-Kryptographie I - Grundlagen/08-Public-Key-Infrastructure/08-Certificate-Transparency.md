---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - pki
---

# Certificate Transparency

> [!info] **Lernziele**
> - Ziel und Funktionsweise von Certificate Transparency verstehen
> - Die Rolle der öffentlichen Logs und Merkle-Trees einordnen
> - Den Beitrag zur Erkennung von Fehlausstellungen erkennen

---

## Inhalt

### Das Problem

Im Web-PKI-Modell kann jede vertrauenswürdige CA Zertifikate für jede Domain ausstellen (→ [[05-Zertifikatsketten-und-Vertrauensmodelle]]). Eine **fehlerhafte oder bösartige Ausstellung** (z. B. ein unautorisiertes Zertifikat für deine Domain) blieb früher oft lange unentdeckt.

### Die Idee: öffentliche, überprüfbare Logs

**Certificate Transparency (CT, RFC 6962)** verlangt, dass ausgestellte Zertifikate in **öffentliche, append-only Logs** eingetragen werden. Diese Logs sind:

- **Öffentlich einsehbar:** Jeder (besonders Domaininhaber) kann prüfen, welche Zertifikate für seine Domain existieren.
- **Append-only und manipulationssicher:** Sie basieren auf **Merkle-Trees** (→ [[08-Merkle-Trees]]), sodass sich nachträgliche Änderungen oder Löschungen beweisbar erkennen lassen.

### Ablauf

```
1. CA stellt Zertifikat aus und reicht es beim CT-Log ein
2. Das Log liefert einen signierten "SCT" (Signed Certificate Timestamp)
3. Der SCT wird im Zertifikat / TLS-Handshake mitgeliefert
4. Browser akzeptieren nur Zertifikate mit gültigen SCTs
```

Moderne Browser (z. B. Chrome) **verlangen** CT-Nachweise für neu ausgestellte öffentliche Zertifikate.

### Nutzen

- **Fehlausstellungen werden sichtbar:** Domaininhaber und Monitore (z. B. crt.sh) überwachen die Logs und schlagen Alarm.
- **Rechenschaft für CAs:** Eine CA kann keine Zertifikate mehr „heimlich" ausstellen.

> [!tip] **Zusammenspiel der Mechanismen**
> CT **verhindert** Fehlausstellungen nicht, macht sie aber **auffindbar**. In Kombination mit Sperrung (CRL/OCSP) und CAA-DNS-Records entsteht ein mehrschichtiger Schutz für die Web-PKI – ein Beispiel für Defense in Depth.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - CT verlangt die Eintragung ausgestellter Zertifikate in öffentliche, append-only Logs
> - Die Logs sind per Merkle-Tree manipulationssicher und von jedem prüfbar
> - Browser verlangen Signed Certificate Timestamps (SCT) für neue Zertifikate
> - CT macht Fehlausstellungen erkennbar und sorgt für CA-Rechenschaft

---

## Übungen

1. Welches Problem der Web-PKI adressiert Certificate Transparency?
2. Welche Datenstruktur macht CT-Logs manipulationssicher?
3. Was ist ein SCT und wozu dient er?

---

← [[07-Online-Certificate-Status-Protocol-OCSP|← Zurück]] | [[00-PKI-Index|Übersicht]] | [[09-Zertifikatsmanagement-und-ACME|Weiter →]]
