---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# Zephyr

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Echtzeit-Betriebssystem |
| **Entwickler** | Linux Foundation |
| **Erstveröffentlichung** | 2016 |
| **Lizenz** | Apache 2.0 |
| **Architektur** | ARM, x86, RISC-V, Xtensa, Arc |

## Zusammenfassung

Zephyr ist ein modernes, sicherheitsorientiertes RTOS für ressourcenbeschränkte IoT-Geräte. Es wird von der Linux Foundation gehostet und kombiniert Linux-ähnliche Entwicklungspraktiken mit einem minimalen Footprint.

### Design-Ziele

| Ziel | Umsetzung |
|------|-----------|
| **Sicherheit** | Memory Protection, Secure Boot |
| **Konnektivität** | Bluetooth, Thread, LoRa, WiFi |
| **Modularität** | Kconfig-basierte Konfiguration |
| **Portabilität** | 400+ unterstützte Boards |

### Architektur

```
Zephyr OS Architektur
┌─────────────────────────────────────────┐
│          User Applications              │
├─────────────────────────────────────────┤
│        Zephyr Subsystems                │
│  ┌─────────────────────────────────┐   │
│  │ Net │ BT │ USB │ File │ Shell  │   │
│  └─────────────────────────────────┘   │
├─────────────────────────────────────────┤
│          Kernel Services                │
│  ┌─────────────────────────────────┐   │
│  │ Threads │ Memory │ Timers │ IPC │   │
│  └─────────────────────────────────┘   │
├─────────────────────────────────────────┤
│          Hardware Abstraction           │
│       (Device Tree, Kconfig)            │
├─────────────────────────────────────────┤
│           Hardware / SoC                │
└─────────────────────────────────────────┘
```

### Unterstützte Technologien

| Kategorie | Protokolle |
|-----------|------------|
| **Wireless** | Bluetooth LE/Mesh, Thread, Zigbee |
| **IoT** | MQTT, CoAP, LwM2M |
| **Netzwerk** | IPv4/IPv6, TCP/UDP, TLS |
| **Speicher** | LittleFS, FAT, NVS |
| **USB** | Device & Host Stack |

### Sicherheitsfeatures

- Memory Protection Unit (MPU) Support
- Stack Canaries
- Thread Isolation
- Secure Boot (MCUboot)
- TLS/DTLS (mbedTLS, wolfSSL)
- PSA Certified

### Vergleich mit FreeRTOS

| Aspekt | Zephyr | FreeRTOS |
|--------|--------|----------|
| Lizenz | Apache 2.0 | MIT |
| Fokus | Security, Connectivity | Minimalism |
| Networking | Native | Separate Libs |
| Devicetree | Ja | Nein |
| Build | CMake/west | IDE/Make |

### Unterstützer

Intel, Nordic Semiconductor, NXP, Texas Instruments, Google, Meta und viele andere tragen zum Projekt bei.

## Siehe auch

- [[FreeRTOS]]
- [[RTEMS]]
- [[Linux]]

## Quellen

- [Zephyr Project](https://www.zephyrproject.org/)
- [Zephyr Documentation](https://docs.zephyrproject.org/)
- [Wikipedia: Zephyr](https://en.wikipedia.org/wiki/Zephyr_(operating_system))
