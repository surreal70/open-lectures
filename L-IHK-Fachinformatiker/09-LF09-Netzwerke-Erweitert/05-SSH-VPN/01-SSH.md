---
title: "SSH – Secure Shell"
created: 2026-10-13
modified: 2026-10-13
type: lecture
tags:
  - lf09
  - ssh
  - sicherheit
  - fernzugriff
source: proTirone (CC-BY-4.0)
---

# SSH – Secure Shell

> [!info] Lernziele
> - SSH-Funktionsweise verstehen
> - Public-Key-Authentifizierung einrichten
> - SSH-Tunnel erstellen
> - Sicherheitsaspekte berücksichtigen

## Grundlagen

### Was ist SSH?

**SSH** (Secure Shell) ist ein Client-Server-System mit asymmetrischer Verschlüsselung zur sicheren Übertragung von Daten auf Layer VII.

### Schlüsselpaare

Jeder SSH-Client und SSH-Server hat ein **rechnerspezifisches Schlüsselpaar**:

```bash
# Server-Schlüssel anzeigen (Linux)
ls /etc/ssh/ssh_host_*_key.pub

# Typische Dateien:
# /etc/ssh/ssh_host_rsa_key      (privat)
# /etc/ssh/ssh_host_rsa_key.pub  (öffentlich)
# /etc/ssh/ssh_host_ed25519_key
# /etc/ssh/ssh_host_ed25519_key.pub
```

## Ablauf einer SSH-Verbindung

```
┌──────────────────────────────────────────────────────────────────┐
│ 1. Client sendet Verbindungswunsch                               │
│ 2. Server sendet Hash seines öffentlichen Schlüssels             │
│ 3. Client prüft known_hosts (Vertrauen?)                         │
│ 4. Schlüsselaustausch (Diffie-Hellman)                           │
│ 5. Benutzerauthentifizierung (Passwort oder Key)                 │
│ 6. Verschlüsselte Kommunikation                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Detaillierter Ablauf

**SSH-Client:**
1. Agiert als Shell auf dem Client-Rechner
2. Stellt SSH-Verbindung zum Server her
3. Nimmt Kommandozeilenbefehl entgegen
4. Verschlüsselt mit Server-Public-Key
5. Überträgt zum SSH-Server

**SSH-Server:**
1. Hilft bei Verbindungsherstellung
2. Empfängt verschlüsselten Befehl
3. Entschlüsselt mit Private-Key
4. Führt Befehl in Shell aus
5. Verschlüsselt Output mit Client-Public-Key
6. Sendet Antwort zurück

## Praktische Einrichtung

### 1. SSH-Client vorbereiten

```bash
# Linux/macOS: Prüfen ob installiert
which ssh

# .ssh-Verzeichnis anlegen
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

### 2. Schlüsselpaar erzeugen

```bash
# RSA-Schlüssel (klassisch)
ssh-keygen -t rsa -b 4096

# Ed25519 (modern, empfohlen)
ssh-keygen -t ed25519

# Dateien werden erstellt:
# ~/.ssh/id_ed25519      (privater Schlüssel)
# ~/.ssh/id_ed25519.pub  (öffentlicher Schlüssel)
```

> [!tip] Passphrase
> Eine Passphrase schützt den privaten Schlüssel zusätzlich. Wird der Key gestohlen, braucht der Angreifer noch die Passphrase.

### 3. Public Key auf Server übertragen

**Variante 1: ssh-copy-id (empfohlen)**
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server
```

**Variante 2: Manuell**
```bash
# Key auf Server kopieren
scp ~/.ssh/id_ed25519.pub user@server:~/

# Auf Server einloggen und Key hinzufügen
ssh user@server
cat ~/id_ed25519.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
rm ~/id_ed25519.pub
```

### 4. Verbindung testen

```bash
# Verbindung mit Key
ssh user@server

# Bei erstem Connect: Fingerprint bestätigen
# The authenticity of host 'server' can't be established.
# ED25519 key fingerprint is SHA256:xxx
# Are you sure you want to continue connecting (yes/no)?
```

## SSH-Varianten

### SCP – Secure Copy

```bash
# Datei zum Server kopieren
scp datei.txt user@server:/pfad/

# Datei vom Server holen
scp user@server:/pfad/datei.txt ./

# Verzeichnis rekursiv kopieren
scp -r verzeichnis/ user@server:/pfad/
```

### SFTP – SSH File Transfer Protocol

```bash
# SFTP-Session starten
sftp user@server

# SFTP-Befehle
sftp> ls              # Remote-Verzeichnis auflisten
sftp> lcd /lokal      # Lokales Verzeichnis wechseln
sftp> put datei.txt   # Upload
sftp> get datei.txt   # Download
sftp> exit
```

## SSH-Tunnel

### Lokaler Tunnel (Local Port Forwarding)

Leitet einen lokalen Port an einen entfernten Server weiter:

```bash
# Syntax: ssh -L lokalerPort:ziel:zielPort user@sshServer
ssh user@server -L 9000:localhost:80

# Jetzt erreichbar: localhost:9000 → server:80
```

```
┌─────────┐     SSH-Tunnel      ┌─────────┐
│ Client  │═════════════════════│ Server  │
│localhost│        ▲            │localhost│
│  :9000  │────────┘            │   :80   │
└─────────┘                     └─────────┘
```

### Anwendungsbeispiel

```bash
# Webserver über SSH-Tunnel erreichen
ssh user@192.168.1.100 -L 9000:192.168.1.100:80

# Im Browser: http://localhost:9000
# Zeigt den Webserver auf 192.168.1.100
```

### Komplexeres Beispiel

Über einen Jump-Host einen internen Server erreichen:

```bash
# Tunnel durch Jump-Host zu internem Server
ssh user@jumphost -L 9000:interner-server:80
```

## SSH-Agent

### Problem

Bei Passphrase-geschützten Keys muss man die Passphrase bei jeder Verbindung eingeben.

### Lösung: SSH-Agent

```bash
# Agent starten (Linux)
eval $(ssh-agent)

# Key zum Agent hinzufügen
ssh-add ~/.ssh/id_ed25519
# Passphrase wird einmalig abgefragt

# Geladene Keys anzeigen
ssh-add -l
```

**Windows:**
```powershell
# SSH-Agent starten
Start-Service ssh-agent

# Key hinzufügen
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

## Sicherheitshinweise

> [!warning] Best Practices
> 1. **Passwort-Login deaktivieren** wenn Key-Auth funktioniert
> 2. **Root-Login verbieten** (`PermitRootLogin no`)
> 3. **Starke Schlüssel** verwenden (Ed25519 oder RSA 4096)
> 4. **known_hosts** nicht ignorieren – Fingerprint prüfen!
> 5. **Fail2Ban** oder ähnliches gegen Brute-Force

### Server-Konfiguration

```bash
# /etc/ssh/sshd_config

# Nur Key-Authentifizierung
PasswordAuthentication no
PubkeyAuthentication yes

# Root-Login verbieten
PermitRootLogin no

# Nur bestimmte User erlauben
AllowUsers admin deploy
```

---

> [!tip] Übungen
> 1. Erstellen Sie ein Ed25519-Schlüsselpaar
> 2. Richten Sie Key-basierte Authentifizierung zu einem Server ein
> 3. Erstellen Sie einen SSH-Tunnel zu einem Webserver
> 4. Analysieren Sie mit `ssh -v` den Verbindungsaufbau

## Weiterführende Links

- [OpenSSH Manual](https://www.openssh.com/manual.html)
- [SSH.com Academy](https://www.ssh.com/academy/ssh)
- [Thomas Krenn Wiki: SSH unter Ubuntu](https://www.thomas-krenn.com/de/wiki/OpenSSH_Public_Key_Authentifizierung_unter_Ubuntu)

---

> [!quote] Quellenhinweis
> Basiert auf Materialien von proTirone (Karsten Reincke), lizenziert unter CC-BY-4.0.
> Inhalte wurden für das Open-Lectures-Format angepasst.
