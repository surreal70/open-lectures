---
author: Andreas Hümmer
created: 2026-10-16
modified: 2026-10-16
status: "draft - review pending"
tags:
  - kryptographie
  - architektur
  - vertiefung
---

# Kryptographie in Microservices

> [!info] **Lernziele**
> - Kryptographische Herausforderungen in Microservices verstehen
> - mTLS und Service Mesh einordnen
> - Secret- und Schlüsselmanagement in verteilten Systemen kennen

---

## Inhalt

### Neue Herausforderungen

In einer **Microservice-Architektur** kommunizieren viele kleine Dienste über das Netzwerk. Das vervielfacht die kryptographischen Anforderungen gegenüber einem Monolithen:

- **Viele Verbindungen** (Service-zu-Service) müssen abgesichert werden.
- **Viele Identitäten** (jeder Dienst braucht eine) und **viele Secrets**.
- **Dynamik**: Dienste werden ständig gestartet/gestoppt/skaliert.

### mTLS und Service Mesh

> [!tip] **Mutual TLS für Service-zu-Service**
> In Microservices authentifizieren sich Dienste gegenseitig per **mutual TLS (mTLS)** (→ [[07-Schluesselvereinbarung-und-Authentifizierung]]): Jeder Dienst hat ein eigenes Zertifikat. Ein **Service Mesh** (z. B. Istio, Linkerd) automatisiert das – es stellt Zertifikate aus, rotiert sie und erzwingt mTLS transparent, ohne dass jeder Dienst das selbst implementieren muss.

### Zero Trust

Microservices passen zum **Zero-Trust-Prinzip**: Kein Dienst vertraut einem anderen allein aufgrund der Netzwerkposition; **jede** Anfrage wird authentifiziert und autorisiert. Kryptographie (mTLS, signierte Tokens wie JWT) ist das Fundament dafür.

### Secret- und Schlüsselmanagement

- **Zentrale Secret-Stores** (Vault, KMS, → [[08-Cloud-Key-Management-Services-KMS]]) statt Secrets in Umgebungsvariablen/Images.
- **Kurzlebige Credentials** und automatische Rotation (→ [[05-Key-Rotation-und-Key-Revocation]]) – passend zur Dynamik.
- **Identität pro Workload** (z. B. SPIFFE/SPIRE) statt geteilter Schlüssel.

### Abwägung

> [!warning] **Komplexität beherrschen**
> Verteilte Systeme erhöhen die Krypto-Komplexität erheblich. Automatisierung (Service Mesh, KMS, Auto-Rotation) ist hier kein Luxus, sondern Voraussetzung, um Fehler (→ [[03-Crypto-Misuse-Patterns]]) zu vermeiden.

---

## Zusammenfassung

> [!abstract] Kernpunkte
> - Microservices vervielfachen Verbindungen, Identitäten und Secrets
> - mTLS (oft via Service Mesh) sichert Service-zu-Service-Kommunikation
> - Zero Trust: jede Anfrage authentifizieren/autorisieren, Kryptographie als Fundament
> - Zentrale Secret-Stores, kurzlebige Credentials, Workload-Identität; Automatisierung ist Pflicht

---

## Übungen

1. Welche zusätzlichen Krypto-Herausforderungen bringen Microservices?
2. Was leistet ein Service Mesh in Bezug auf mTLS?
3. Wie hängen Zero Trust und Kryptographie zusammen?

---

← [[05-Defense-in-Depth-mit-Kryptographie|← Zurück]] | [[00-Architektur-Index|Übersicht]] | [[07-Enterprise-Kryptographie-Architektur|Weiter →]]
