---
author: Open Lectures
title: Addition von Brüchen
status: draft - review pending
tags:
  - content
  - mathematik
  - bruchrechnung
created: 2026-10-13
modified: 2026-10-16
---

# Addition von Brüchen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Brüche mit gleichem Nenner addieren können
> - Brüche mit verschiedenen Nennern addieren können
> - Gemischte Zahlen addieren können

---

## Überblick

Um Brüche zu addieren, müssen sie denselben Nenner haben. Bei gleichem Nenner werden nur die Zähler addiert; bei verschiedenen Nennern muss zuerst ein gemeinsamer Nenner gefunden werden.

Die Addition von Brüchen ist einer der Gründe, warum wir das Erweitern und den Hauptnenner gelernt haben. Ohne diese Werkzeuge könnten wir Brüche mit verschiedenen Nennern nicht zusammenzählen.

Im Alltag begegnet uns die Bruchaddition oft: Wenn du $\frac{1}{4}$ Liter Milch und $\frac{1}{2}$ Liter Milch zusammenschüttest, wie viel hast du dann? Diese Frage lässt sich nur mit Bruchaddition beantworten.

---

## Gleiche Nenner

$$\frac{a}{c} + \frac{b}{c} = \frac{a + b}{c}$$

**Beispiel:**
$$\frac{2}{5} + \frac{1}{5} = \frac{2 + 1}{5} = \frac{3}{5}$$

> [!note] **Anschauliche Erklärung**
> Stell dir vor, du hast 2 Fünftel einer Pizza und bekommst noch 1 Fünftel dazu. Dann hast du 3 Fünftel – die Stücke sind gleich groß, also zählst du sie einfach zusammen.
>
> ```
> ┌───┬───┬───┬───┬───┐     ┌───┬───┬───┬───┬───┐
> │ ▓ │ ▓ │   │   │   │  +  │ ▓ │   │   │   │   │
> └───┴───┴───┴───┴───┘     └───┴───┴───┴───┴───┘
>        ²⁄₅          +            ¹⁄₅
>
>                    ↓
>
> ┌───┬───┬───┬───┬───┐
> │ ▓ │ ▓ │ ▓ │   │   │  =  ³⁄₅
> └───┴───┴───┴───┴───┘
> ```

> [!warning] **Achtung**
> Nur die **Zähler** werden addiert! Der Nenner bleibt gleich.
> 
> **Falsch:** $\frac{2}{5} + \frac{1}{5} = \frac{3}{10}$ ✗
>
> **Richtig:** $\frac{2}{5} + \frac{1}{5} = \frac{3}{5}$ ✓

> [!warning] **Häufiger Fehler: Nenner addieren**
> Ein sehr verbreiteter Fehler ist, auch die Nenner zu addieren:
>
> **Falsch:** $\frac{1}{3} + \frac{1}{4} = \frac{2}{7}$ ✗
>
> Das ergibt keinen Sinn! $\frac{1}{3}$ ist etwa 0,33 und $\frac{1}{4}$ ist 0,25 – zusammen etwa 0,58. Aber $\frac{2}{7} \approx 0,29$ – viel weniger als jeder einzelne Bruch!

---

## Verschiedene Nenner

Bei verschiedenen Nennern müssen wir erst einen gemeinsamen Nenner herstellen:

1. Hauptnenner bestimmen (kgV der Nenner)
2. Brüche erweitern
3. Zähler addieren
4. Ggf. kürzen

**Beispiel:** $\frac{1}{3} + \frac{1}{4}$

$$= \frac{4}{12} + \frac{3}{12} = \frac{7}{12}$$

**Schritt für Schritt:**
1. Hauptnenner: kgV(3, 4) = 12
2. $\frac{1}{3}$ erweitern mit 4: $\frac{1 \cdot 4}{3 \cdot 4} = \frac{4}{12}$
3. $\frac{1}{4}$ erweitern mit 3: $\frac{1 \cdot 3}{4 \cdot 3} = \frac{3}{12}$
4. Addieren: $\frac{4}{12} + \frac{3}{12} = \frac{7}{12}$
5. Kürzen? $\frac{7}{12}$ ist bereits vollständig gekürzt (7 ist prim)

> [!tip] **Merkregel: Drei Schritte**
> 1. **Gleich**namig machen (Hauptnenner)
> 2. **Zähler** addieren
> 3. **Kürzen** wenn möglich

---

## Beispiele

| Rechnung | Hauptnenner | Ergebnis |
|----------|-------------|----------|
| $\frac{1}{2} + \frac{1}{4}$ | 4 | $\frac{2}{4} + \frac{1}{4} = \frac{3}{4}$ |
| $\frac{2}{3} + \frac{3}{5}$ | 15 | $\frac{10}{15} + \frac{9}{15} = \frac{19}{15} = 1\frac{4}{15}$ |
| $\frac{5}{6} + \frac{1}{4}$ | 12 | $\frac{10}{12} + \frac{3}{12} = \frac{13}{12} = 1\frac{1}{12}$ |

> [!note] **Ergebnis prüfen**
> Ein schneller Plausibilitätscheck: Das Ergebnis muss größer sein als jeder einzelne Bruch.
> - $\frac{1}{2} + \frac{1}{4} = \frac{3}{4}$ ✓ (größer als $\frac{1}{2}$ und $\frac{1}{4}$)
> - Als Dezimal: $0{,}5 + 0{,}25 = 0{,}75$ ✓

---

## Gemischte Zahlen addieren

Es gibt zwei Methoden, gemischte Zahlen zu addieren:

**Methode 1:** Getrennt addieren (bei einfachen Bruchteilen)

$$2\frac{1}{4} + 1\frac{2}{4} = (2 + 1) + (\frac{1}{4} + \frac{2}{4}) = 3\frac{3}{4}$$

Diese Methode ist schnell, wenn die Bruchteile denselben Nenner haben und ihre Summe einen echten Bruch ergibt.

**Methode 2:** In unechte Brüche umwandeln (sicherer)

$$2\frac{1}{4} + 1\frac{2}{4} = \frac{9}{4} + \frac{6}{4} = \frac{15}{4} = 3\frac{3}{4}$$

> [!tip] **Welche Methode wählen?**
> - **Methode 1** eignet sich, wenn die Bruchteile denselben Nenner haben und ihre Summe < 1 ist
> - **Methode 2** ist sicherer und funktioniert immer – besonders wenn die Summe der Bruchteile > 1 ist

**Beispiel, wo Methode 1 komplizierter wird:**

$$3\frac{3}{4} + 2\frac{1}{2}$$

Mit Methode 1:
- Ganze: $3 + 2 = 5$
- Brüche: $\frac{3}{4} + \frac{1}{2} = \frac{3}{4} + \frac{2}{4} = \frac{5}{4} = 1\frac{1}{4}$
- Zusammen: $5 + 1\frac{1}{4} = 6\frac{1}{4}$

Mit Methode 2:
$$\frac{15}{4} + \frac{5}{2} = \frac{15}{4} + \frac{10}{4} = \frac{25}{4} = 6\frac{1}{4}$$

---

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[06-Hauptnenner-bestimmen|Hauptnenner]] – Grundlage für Addition verschiedener Nenner
- → [[08-Subtraktion-von-Bruechen|Subtraktion von Brüchen]] – Funktioniert analog
- → [[03-Gemischte-Zahlen|Gemischte Zahlen]] – Umwandlung für Methode 2

> [!warning] **Prüfungsrelevant**
> - Gleicher Nenner: nur Zähler addieren
> - Verschiedene Nenner: erst auf Hauptnenner erweitern
> - Ergebnis immer kürzen, falls möglich

> [!question] **Typische Prüfungsfragen**
> - Berechne: $\frac{3}{4} + \frac{5}{6}$
> - Berechne: $2\frac{1}{3} + 1\frac{5}{6}$

## Quellen

- Padberg, Friedhelm: *Didaktik der Bruchrechnung*. Springer, 2009.
