---
title: "MQTT – Message Queuing Telemetry Transport"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf11d
  - iot
  - mqtt
  - protokoll
  - publish-subscribe
  - mosquitto
source: proTirone (CC-BY-4.0)
---

# MQTT – Message Queuing Telemetry Transport

> [!info] Lernziele
> - MQTT-Architektur und Publish/Subscribe-Prinzip verstehen
> - Topics und Wildcards anwenden
> - Mosquitto installieren und nutzen

## Was ist MQTT?

**MQTT** (ursprünglich *Message Queuing Telemetry Transport*) ist ein leichtgewichtiges Messaging-Protokoll für IoT-Anwendungen.

### Eigenschaften

- **Publish/Subscribe**-Modell (nicht Request/Response)
- **Leichtgewichtig**: Minimaler Overhead
- **Zuverlässig**: Verschiedene QoS-Level
- **Asynchron**: Entkopplung von Sender und Empfänger

## Architektur

```
┌─────────────┐                           ┌─────────────┐
│  Publisher  │                           │  Subscriber │
│  (Sensor)   │                           │   (App)     │
└──────┬──────┘                           └──────┬──────┘
       │                                         │
       │ publish                       subscribe │
       │ "home/temp"                   "home/#"  │
       ↓                                         ↓
┌─────────────────────────────────────────────────────────┐
│                      MQTT Broker                        │
│                     (Mosquitto)                         │
│                                                         │
│   Topics:                                               │
│   ├── home/sensor/temperature                           │
│   ├── home/sensor/humidity                              │
│   └── home/light/status                                 │
└─────────────────────────────────────────────────────────┘
```

### Komponenten

| Komponente | Funktion |
|------------|----------|
| **Publisher** | Sendet Nachrichten zu einem Topic |
| **Subscriber** | Empfängt Nachrichten von abonnierten Topics |
| **Broker** | Vermittelt zwischen Publishern und Subscribern |
| **Topic** | Hierarchischer Namensraum für Nachrichten |

## Topics

Topics sind hierarchisch aufgebaut und durch `/` getrennt:

```
home/sensor/temperature
home/sensor/humidity
home/light/living_room/status
office/sensor/motion
```

### Wildcards

| Wildcard | Bedeutung | Beispiel |
|----------|-----------|----------|
| `+` | Ein Level | `home/+/temperature` → `home/kitchen/temperature`, `home/bedroom/temperature` |
| `#` | Alle Level (ab hier) | `home/#` → alle Topics unter `home/` |

### Topic-Design Beispiel

```
Raum 1: Sensor 1 (Temp/Druck), Sensor 2 (Lautstärke)
Raum 2: Sensor 1 (Temp/Druck), Sensor 2 (Feuchtigkeit)

Topics:
├── R1/S1/Temp_Press
├── R1/S2/Volume
├── R2/S1/Temp_Press
└── R2/S2/Humidity

Subscriptions:
├── R2/#           → Alle Werte aus Raum 2
├── +/+/Temp_Press → Alle Temperaturwerte
└── +/S1/#         → Alle Hauptsensoren
```

## Quality of Service (QoS)

| Level | Name | Beschreibung |
|-------|------|--------------|
| **0** | At most once | Keine Bestätigung, Nachricht kann verloren gehen |
| **1** | At least once | Bestätigung erforderlich, Duplikate möglich |
| **2** | Exactly once | Vier-Wege-Handshake, keine Duplikate |

## Mosquitto: MQTT-Broker

### Installation (Ubuntu)

```bash
# System aktualisieren
sudo apt-get update
sudo apt-get upgrade

# Mosquitto-Broker installieren
sudo apt-get install -y mosquitto

# Mosquitto-Clients installieren
sudo apt-get install -y mosquitto-clients

# Status prüfen
sudo systemctl status mosquitto
```

### Konfiguration

- **Hauptkonfiguration**: `/etc/mosquitto/mosquitto.conf`
- **Teilkonfigurationen**: `/etc/mosquitto/conf.d/`
- **Standard-Port**: 1883 (unverschlüsselt), 8883 (TLS)

### Befehle

#### Subscriber starten

```bash
# Einzelnes Topic abonnieren
mosquitto_sub -t "home/sensor/temperature"

# Mit Wildcard
mosquitto_sub -t "home/#"

# Alle Topics
mosquitto_sub -t "#"
```

#### Nachrichten publizieren

```bash
# Einfacher Wert
mosquitto_pub -t "home/sensor/temperature" -m "22.5"

# Mit QoS und Retain
mosquitto_pub -t "home/sensor/temperature" -m "22.5" -q 1 -r

# JSON-Nachricht
mosquitto_pub -t "home/sensor/temperature" \
  -m '{"time":"2026-10-13", "temp":22.5, "unit":"C"}'
```

#### Parameter

| Parameter | Bedeutung |
|-----------|-----------|
| `-t` | Topic |
| `-m` | Message (Nachricht) |
| `-q` | QoS-Level (0, 1, 2) |
| `-r` | Retain (letzte Nachricht speichern) |
| `-h` | Hostname des Brokers |
| `-p` | Port |

## Praxisbeispiel: Sensor-Monitoring

### Publisher-Skript

```bash
#!/bin/bash
# sensor-publish.sh

while true; do
  TEMP=$(cat /sys/class/thermal/thermal_zone0/temp)
  TEMP_C=$((TEMP / 1000))
  
  mosquitto_pub -t "server/cpu/temperature" \
    -m "{\"temp\": $TEMP_C, \"unit\": \"C\"}" \
    -q 1 -r
  
  sleep 60
done
```

### Subscriber

```bash
# Alle Serverdaten empfangen
mosquitto_sub -t "server/#" -v
```

## Prüfungsrelevanz

> [!question] Typische Prüfungsfragen
> - Erklären Sie das Publish/Subscribe-Prinzip
> - Was ist ein MQTT-Broker?
> - Welche Wildcards gibt es und was bedeuten sie?
> - Nennen Sie die drei QoS-Level und ihre Eigenschaften

## Querverweise

- → [[02-LoRaWAN|LoRaWAN]] – Weiteres IoT-Protokoll
- → [[../01-Serverinstallation/01-Konzeption|Serverkonzeption]] – Broker-Installation
- → [[../../../09-LF09-Netzwerke-Erweitert/02-Ports/01-Ports-Services|Ports]] – MQTT-Ports

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (CC-BY-4.0).
