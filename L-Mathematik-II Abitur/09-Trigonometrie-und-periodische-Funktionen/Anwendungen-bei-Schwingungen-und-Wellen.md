---
author: Andreas Hümmer
title: Anwendungen bei Schwingungen und Wellen
tags:
  - content
  - mathe
  - trigonometrie
  - schwingungen
  - wellen
  - physik
  - anwendungen
created: 2025-06-20
modified: 2025-06-20
---

# Anwendungen bei Schwingungen und Wellen

> [!info] **Lernziele**
> Nach diesem Kapitel solltest du:
> - Die mathematische Beschreibung harmonischer Schwingungen verstehen
> - Wellenphänomene mit trigonometrischen Funktionen modellieren können
> - Überlagerung von Schwingungen (Interferenz) analysieren können
> - Die Verbindung zwischen Mathematik und physikalischen Phänomenen erkennen

---

## Überblick

Die Trigonometrie findet ihre wichtigsten praktischen Anwendungen in der Beschreibung von **Schwingungen** und **Wellen**. Von mechanischen Pendeln über Schallwellen bis zu elektromagnetischer Strahlung – periodische Vorgänge werden mathematisch durch Sinus- und Kosinusfunktionen beschrieben. Dieses Kapitel verbindet die mathematischen Grundlagen mit konkreten physikalischen Anwendungen.

## Harmonische Schwingung

### Definition

Eine **harmonische Schwingung** ist eine periodische Bewegung, die durch eine Sinus- oder Kosinusfunktion beschrieben wird:

$$x(t) = A \cdot \cos(\omega t + \varphi_0)$$

oder äquivalent:

$$x(t) = A \cdot \sin(\omega t + \psi_0)$$

### Die Parameter im physikalischen Kontext

| Parameter | Symbol | Physikalische Bedeutung | Einheit |
|-----------|--------|------------------------|---------|
| Auslenkung | $x(t)$ | Position/Zustand zur Zeit $t$ | m, V, ... |
| Amplitude | $A$ | Maximale Auslenkung | m, V, ... |
| Kreisfrequenz | $\omega$ | Winkelgeschwindigkeit | rad/s |
| Anfangsphase | $\varphi_0$ | Zustand bei $t = 0$ | rad |
| Periode | $T = \frac{2\pi}{\omega}$ | Dauer einer Schwingung | s |
| Frequenz | $f = \frac{1}{T}$ | Schwingungen pro Sekunde | Hz |

### Geschwindigkeit und Beschleunigung

Durch Ableitung erhält man:

**Geschwindigkeit:**
$$v(t) = \frac{dx}{dt} = -A\omega \cdot \sin(\omega t + \varphi_0)$$

**Beschleunigung:**
$$a(t) = \frac{d^2x}{dt^2} = -A\omega^2 \cdot \cos(\omega t + \varphi_0) = -\omega^2 \cdot x(t)$$

Die Beschleunigung ist proportional zur Auslenkung und ihr entgegengerichtet – das ist charakteristisch für harmonische Schwingungen!

## Beispiel: Federpendel

### Bewegungsgleichung

Ein Körper der Masse $m$ an einer Feder mit Federkonstante $k$ schwingt mit:

$$x(t) = A \cdot \cos(\omega_0 t + \varphi_0)$$

wobei die **Eigenkreisfrequenz** ist:

$$\omega_0 = \sqrt{\frac{k}{m}}$$

### Periode des Federpendels

$$T = 2\pi\sqrt{\frac{m}{k}}$$

**Beispiel:** Eine Feder ($k = 100$ N/m) mit Masse $m = 0{,}4$ kg:

$$T = 2\pi\sqrt{\frac{0{,}4}{100}} = 2\pi \cdot 0{,}063 \approx 0{,}4 \text{ s}$$

## Beispiel: Mathematisches Pendel

### Schwingungsgleichung

Für kleine Auslenkungen ($\varphi < 10°$) gilt:

$$\varphi(t) = \varphi_0 \cdot \cos(\omega_0 t)$$

mit der Eigenkreisfrequenz:

$$\omega_0 = \sqrt{\frac{g}{L}}$$

wobei $L$ die Pendellänge und $g \approx 9{,}81$ m/s² ist.

### Periode des mathematischen Pendels

$$T = 2\pi\sqrt{\frac{L}{g}}$$

**Beispiel:** Ein 1 m langes Pendel:

$$T = 2\pi\sqrt{\frac{1}{9{,}81}} \approx 2{,}01 \text{ s}$$

## Wellen

### Wellenfunktion

Eine **Welle** ist eine räumlich und zeitlich periodische Störung. Die allgemeine Form einer harmonischen Welle:

$$y(x, t) = A \cdot \sin(kx - \omega t + \varphi_0)$$

### Wellenparameter

| Parameter | Symbol | Bedeutung | Beziehung |
|-----------|--------|-----------|-----------|
| Wellenzahl | $k$ | Räumliche Frequenz | $k = \frac{2\pi}{\lambda}$ |
| Wellenlänge | $\lambda$ | Abstand zwischen Wellenbergen | $\lambda = \frac{2\pi}{k}$ |
| Kreisfrequenz | $\omega$ | Zeitliche Frequenz | $\omega = 2\pi f$ |
| Ausbreitungs­geschwindigkeit | $c$ | Geschwindigkeit der Welle | $c = \lambda \cdot f = \frac{\omega}{k}$ |

### Fundamentale Wellenbeziehung

$$\boxed{c = \lambda \cdot f}$$

**Beispiel:** Schallwellen mit $f = 440$ Hz (Kammerton A) in Luft ($c = 343$ m/s):

$$\lambda = \frac{c}{f} = \frac{343}{440} \approx 0{,}78 \text{ m}$$

## Überlagerung von Schwingungen (Superposition)

### Prinzip der Superposition

Überlagern sich zwei Wellen, addieren sich ihre Auslenkungen:

$$y_{\text{ges}}(x, t) = y_1(x, t) + y_2(x, t)$$

### Konstruktive Interferenz

Treffen zwei Wellen mit gleicher Phase aufeinander (Phasendifferenz $\Delta\varphi = 0$):

$$A_{\text{ges}} = A_1 + A_2$$

Die Amplituden addieren sich – **Verstärkung**.

### Destruktive Interferenz

Treffen zwei Wellen mit entgegengesetzter Phase aufeinander ($\Delta\varphi = \pi$):

$$A_{\text{ges}} = |A_1 - A_2|$$

Bei gleichen Amplituden: **Auslöschung** ($A_{\text{ges}} = 0$).

### Stehende Wellen

Die Überlagerung zweier gegenläufiger Wellen gleicher Amplitude und Frequenz ergibt eine **stehende Welle**:

$$y(x, t) = 2A \cdot \sin(kx) \cdot \cos(\omega t)$$

Charakteristika:
- **Knoten:** Punkte mit $y = 0$ für alle $t$ (bei $kx = n\pi$)
- **Bäuche:** Punkte maximaler Amplitude (bei $kx = \frac{\pi}{2} + n\pi$)

## Schwebung

### Entstehung

Bei Überlagerung zweier Schwingungen mit leicht verschiedenen Frequenzen $f_1$ und $f_2$:

$$y_1 + y_2 = A\sin(\omega_1 t) + A\sin(\omega_2 t)$$

Mit der Summe-zu-Produkt-Formel:

$$= 2A \cdot \cos\left(\frac{\omega_1 - \omega_2}{2}t\right) \cdot \sin\left(\frac{\omega_1 + \omega_2}{2}t\right)$$

### Interpretation

- Die Schwingung hat die **Trägerfrequenz** $f_T = \frac{f_1 + f_2}{2}$
- Die Amplitude moduliert mit der **Schwebungsfrequenz** $f_S = |f_1 - f_2|$

**Beispiel:** Zwei Stimmgabeln mit $440$ Hz und $442$ Hz erzeugen eine Schwebung mit $f_S = 2$ Hz (2 „Wabern" pro Sekunde).

## Anwendung: Wechselstrom

### Spannung und Stromstärke

Die Netzspannung in Deutschland:

$$u(t) = U_0 \cdot \sin(2\pi \cdot 50 \cdot t)$$

mit $U_0 = 325$ V (Scheitelspannung).

### Effektivwert

Der **Effektivwert** einer Wechselgröße ist:

$$U_{\text{eff}} = \frac{U_0}{\sqrt{2}} \approx 0{,}707 \cdot U_0$$

Für die Netzspannung: $U_{\text{eff}} = 230$ V

### Leistung

Bei Wechselstrom mit rein ohmscher Last:

$$P(t) = u(t) \cdot i(t) = U_0 I_0 \sin^2(\omega t)$$

Die mittlere Leistung:

$$\bar{P} = \frac{U_0 I_0}{2} = U_{\text{eff}} \cdot I_{\text{eff}}$$

## Modellierung realer Phänomene

### Gedämpfte Schwingung

Reale Schwingungen verlieren durch Reibung Energie:

$$x(t) = A_0 \cdot e^{-\delta t} \cdot \cos(\omega_d t + \varphi_0)$$

wobei $\delta$ die Dämpfungskonstante und $\omega_d$ die gedämpfte Kreisfrequenz ist.

### Erzwungene Schwingung

Bei periodischer Anregung mit Frequenz $\omega$:

$$x(t) = A(\omega) \cdot \sin(\omega t + \varphi(\omega))$$

**Resonanz** tritt auf, wenn $\omega \approx \omega_0$ (Eigenfrequenz).

## Zusammenhänge

Querverweise zu verwandten Themen:

- → [[Periodische-Vorgaenge]] – Grundlagen periodischer Phänomene
- → [[Sinus--und-Kosinusfunktionen]] – Mathematische Grundlage
- → [[Phasenverschiebung]] – Phase bei Überlagerung
- → [[Additionstheoreme]] – Mathematik der Superposition

> [!warning] **Prüfungsrelevant**
> - Die Wellenfunktion $y(x,t) = A\sin(kx - \omega t)$ interpretieren können
> - Die Beziehung $c = \lambda \cdot f$ anwenden
> - Konstruktive und destruktive Interferenz unterscheiden
> - Die Entstehung von Schwebungen erklären können

> [!question] **Typische Prüfungsfragen**
> - Eine Welle hat die Frequenz $f = 200$ Hz und die Wellenlänge $\lambda = 1{,}5$ m. Wie groß ist die Ausbreitungsgeschwindigkeit?
> - Erklären Sie das Entstehen einer stehenden Welle.
> - Zwei Töne mit $f_1 = 256$ Hz und $f_2 = 260$ Hz werden gleichzeitig gespielt. Beschreiben Sie, was man hört.

## Quellen

- Tipler, P.A. & Mosca, G.: Physik für Wissenschaftler und Ingenieure. Springer Spektrum, 2019.
- Papula, L.: Mathematik für Ingenieure und Naturwissenschaftler, Band 1. Springer Vieweg, 2018.
- Halliday, D., Resnick, R. & Walker, J.: Physik. Wiley-VCH, 2017.

> [!tip] **Weiterführende Links**
> - [[Phasenverschiebung]] – Phasenbeziehungen bei Überlagerung
> - [[Additionstheoreme]] – Mathematische Werkzeuge
