---
title: Baumdiagramme
chapter: "14"
section: "14.8"
type: lecture
created: 2026-10-13
modified: 2026-10-13
status: draft - review pending
tags:
  - mathematik/wahrscheinlichkeit
  - baumdiagramm
---

# Baumdiagramme

## Einführung

> [!info] Lernziele
> Nach dieser Lektion können Sie:
> - Baumdiagramme für mehrstufige Experimente erstellen
> - Pfade ablesen und beschreiben

## Aufbau

```
        Start
       /     \
     K(½)    Z(½)     ← 1. Stufe
    /  \    /  \
  K(½) Z(½) K(½) Z(½)  ← 2. Stufe
```

## Elemente

| Element | Bedeutung |
|---------|-----------|
| Knoten | Zustand nach einer Stufe |
| Kante | Übergang zum nächsten Zustand |
| Pfad | Weg vom Start zum Endergebnis |
| Kantengewicht | Wahrscheinlichkeit des Übergangs |

## Beispiel: Zweimal Münze werfen

Pfade:
- K → K (Kopf-Kopf)
- K → Z (Kopf-Zahl)
- Z → K (Zahl-Kopf)
- Z → Z (Zahl-Zahl)

---

**Navigation:** [[07-Gegenereignisse|← Gegenereignisse]] | [[09-Pfadregeln|Pfadregeln →]]
