---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - schluessel
---

# Cloud Key Management Services KMS

> [!info] **Lernziele**
> - Funktion eines Cloud-KMS verstehen
> - Envelope Encryption im Cloud-Kontext einordnen
> - Vor- und Nachteile sowie BYOK/HYOK kennen

---

## Inhalt

### Was ist ein Cloud-KMS?

Ein **Key Management Service (KMS)** ist ein von einem Cloud-Anbieter verwalteter Dienst zur zentralen Erzeugung, Speicherung und Nutzung kryptographischer Schlüssel (z. B. AWS KMS, Google Cloud KMS, Azure Key Vault). Die Schlüssel liegen in HSMs des Anbieters; der Zugriff erfolgt über API und wird per IAM-Rechten gesteuert.

### Envelope Encryption im KMS

Cloud-KMS setzen das KEK/DEK-Muster (→ [[03-Schluesselverteilung-und-Speicherung]]) um:

```
1. App fordert vom KMS einen Daten-Schlüssel (DEK) an
2. KMS liefert DEK im Klartext + DEK verschlüsselt mit dem KEK (im KMS)
3. App verschlüsselt Daten mit dem DEK, verwirft den Klartext-DEK
4. Der verschlüsselte DEK wird bei den Daten gespeichert
5. Zum Entschlüsseln: verschlüsselten DEK ans KMS → KMS entschlüsselt ihn mit dem KEK
```

Der **KEK** verlässt das KMS nie – wie bei einem HSM.

### Vor- und Nachteile

| Vorteil | Nachteil / Risiko |
|---------|-------------------|
| kein eigener HSM-Betrieb nötig | Vertrauen in den Cloud-Anbieter |
| Skalierung, Verfügbarkeit, Auditing | Anbieter hat (potenziell) Zugriff auf KEK |
| IAM-Integration, Automatisierung | Vendor-Lock-in |

### BYOK und HYOK

> [!tip] **Kontrolle über eigene Schlüssel**
> - **BYOK (Bring Your Own Key):** Der Kunde importiert eigenes Schlüsselmaterial in das KMS – mehr Kontrolle über die Herkunft.
> - **HYOK (Hold Your Own Key):** Der Schlüssel verbleibt in einem **eigenen** HSM außerhalb der Cloud; der Anbieter kann ihn nicht einsehen. Höchste Kontrolle, aber mehr Aufwand.

### Best Practices

- Zugriff strikt per IAM (Least Privilege) und protokolliert.
- Automatische Rotation aktivieren (→ [[05-Key-Rotation-und-Key-Revocation]]).
- Für höchste Anforderungen BYOK/HYOK bzw. „KMS mit eigenem HSM" erwägen.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Cloud-KMS verwaltet Schlüssel in anbieterseitigen HSMs, Zugriff per API/IAM
> - Envelope Encryption (KEK im KMS, DEK bei den Daten) ist das Kernmuster
> - Vorteil: kein eigener HSM-Betrieb; Risiko: Vertrauen in den Anbieter, Lock-in
> - BYOK/HYOK geben dem Kunden mehr Kontrolle über das Schlüsselmaterial

---

## Übungen

1. Wie funktioniert Envelope Encryption in einem Cloud-KMS?
2. Welches Schlüsselmaterial verlässt das KMS nie?
3. Worin unterscheiden sich BYOK und HYOK?

---

← [[07-Trusted-Platform-Module-TPM|← Zurück]] | [[00-Schluessel-Index|Übersicht]] | [[09-Secret-Sharing-und-Backup-Konzepte|Weiter →]]
