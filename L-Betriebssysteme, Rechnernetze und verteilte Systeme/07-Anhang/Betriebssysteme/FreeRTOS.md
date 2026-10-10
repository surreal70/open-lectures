---
author: Andreas Hümmer
created: '2026-10-07'
modified: '2026-10-09'
tags:
  - anhang
---

# FreeRTOS

## Überblick

| Eigenschaft | Wert |
|-------------|------|
| **Typ** | Echtzeit-Betriebssystem |
| **Entwickler** | Amazon Web Services (seit 2017) |
| **Erstveröffentlichung** | 2003 |
| **Lizenz** | MIT (früher modifizierte GPL) |
| **Architektur** | 40+ Mikrocontroller-Plattformen |

## Zusammenfassung

FreeRTOS ist das weltweit meistgenutzte Echtzeit-Betriebssystem für Mikrocontroller. Mit nur wenigen KB RAM-Footprint ermöglicht es präventives Multitasking auf ressourcenbeschränkten Embedded-Systemen.

### Kern-Features

| Feature | Beschreibung |
|---------|--------------|
| **Tasks** | Präventives Scheduling mit Prioritäten |
| **Queues** | Inter-Task-Kommunikation |
| **Semaphoren** | Synchronisation |
| **Timer** | Software-Timer |
| **Event Groups** | Ereignis-Synchronisation |
| **Tickless Mode** | Energiesparen |

### Minimaler Footprint

```
FreeRTOS Speicherbedarf
┌─────────────────────────────────────────┐
│  Kernel:           ~6-12 KB ROM         │
│  Pro Task-Stack:   Konfigurierbar       │
│  RAM (Kernel):     ~236 Bytes           │
│  Pro Task:         ~64 Bytes TCB        │
└─────────────────────────────────────────┘
```

### Architektur

```
FreeRTOS Task-Modell
┌─────────────────────────────────────────┐
│    Task 1     Task 2     Task 3         │
│   (Prio 3)   (Prio 2)   (Prio 1)        │
├─────────────────────────────────────────┤
│           FreeRTOS Kernel               │
│  ┌──────────────────────────────────┐  │
│  │  Scheduler │ Queues │ Semaphores │  │
│  └──────────────────────────────────┘  │
├─────────────────────────────────────────┤
│       Hardware Abstraction (Port)       │
├─────────────────────────────────────────┤
│          Mikrocontroller               │
│     (ARM Cortex-M, ESP32, etc.)         │
└─────────────────────────────────────────┘
```

### AWS-Integration

Seit der Amazon-Übernahme bietet FreeRTOS:
- **AWS IoT Integration**: MQTT, Shadow
- **OTA Updates**: Over-the-Air-Updates
- **TLS**: Sichere Verbindungen
- **POSIX-Schicht**: Portierbarkeit

### Unterstützte Plattformen

- ARM Cortex-M (STM32, NXP, Nordic)
- ESP32 (Espressif)
- RISC-V
- PIC, AVR
- Xtensa

## Siehe auch

- [[VxWorks]]
- [[Zephyr]]
- [[RTOS-Grundlagen]]

## Quellen

- [FreeRTOS.org](https://www.freertos.org/)
- [FreeRTOS Documentation](https://www.freertos.org/Documentation/)
- [Wikipedia: FreeRTOS](https://en.wikipedia.org/wiki/FreeRTOS)
