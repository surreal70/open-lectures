# Verschlüsselung, Hashing, Kodierung und Signierung

#kryptographie #verschlüsselung #hashing #signatur #kodierung

## Lernziele

- Die vier Verfahren klar unterscheiden können
- Anwendungsfälle für jedes Verfahren kennen
- Typische Fehler bei der Verwechslung vermeiden

---

## Inhalt

> [!note] Kapitel in Bearbeitung
> Dieses Kapitel wird noch ausgearbeitet.

### Verschlüsselung (Encryption)

<!-- TODO: Umkehrbar mit Schlüssel, Vertraulichkeit -->

### Hashing

<!-- TODO: Einwegfunktion, Integrität, Fingerabdruck -->

### Kodierung (Encoding)

<!-- TODO: Base64, Hex – KEINE Sicherheit! -->

### Signierung (Signing)

<!-- TODO: Authentizität, Nichtabstreitbarkeit -->

### Vergleichstabelle

| Verfahren | Umkehrbar | Schlüssel | Schutzziel |
|-----------|-----------|-----------|------------|
| Verschlüsselung | Ja | Ja | Vertraulichkeit |
| Hashing | Nein | Nein | Integrität |
| Kodierung | Ja | Nein | Keines |
| Signierung | – | Ja (asymm.) | Authentizität |

---

## Zusammenfassung

> [!summary] Kernpunkte
> - Kodierung ≠ Verschlüsselung (häufiger Fehler!)
> - Hashing ist eine Einwegfunktion
> - Signieren = Hashen + mit privatem Schlüssel verschlüsseln

---

## Übungen

1. Warum ist Base64 keine Verschlüsselung?
2. Erklären Sie, warum man Passwörter hasht statt verschlüsselt

---

← [[03-Schutzziele|← Zurück]] | [[01-Einfuehrung-Index|Übersicht]] | [[05-Kryptographische-Angriffsmodelle|Weiter →]]
