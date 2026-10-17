# Anleitung: Einen eigenen Vault erstellen

Diese Anleitung erklärt, wie du mit Kiro einen völlig neuen Lehr-Vault in diesem Repository aufbaust – von den ersten konzeptionellen Überlegungen bis zum fertigen, konventionskonformen Obsidian-Vault. Sie beschreibt einen empfohlenen Arbeitsablauf, liefert fertige Beispiel-Prompts, verweist auf die vorhandenen Steering-Dateien und Skills und zeigt, wie du eigene ergänzt.

> Dieses Repository wird von Kiro (einem KI-Agenten) betrieben. Am schnellsten baust du einen Vault, indem du in natürlicher Sprache beschreibst, was du möchtest, und den Agenten gerüstet, befüllt und prüfen lässt – geleitet von den Steering-Dateien und Skills des Repositories.

---

## ⚖️ Lizenz — zuerst lesen

**Alles, was du diesem Repository hinzufügst, unterliegt der Lizenz des Repositories: [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](./LICENSE).**

Das bedeutet, dass von dir beigetragene Inhalte von anderen:

- **kostenlos** genutzt, studiert, geteilt und angepasst werden dürfen,
- **mit Namensnennung (Attribution)** und
- **ausschließlich zu nicht-kommerziellen Zwecken**.

**Wenn du dein Material nicht unter diesen Bedingungen bereitstellen möchtest, lege ein eigenes, separates Repository an, statt es hier hinzuzufügen.**

Und umgekehrt: Wenn du ein **abgeleitetes Werk** auf Basis eines bestehenden Vaults erstellst (anpassen, erweitern, remixen), musst du dieselbe Lizenz einhalten — **Namensnennung** für die ursprünglichen Autor(inn)en und **nicht-kommerzielle** Nutzung.

> ‼️ **Fremdmaterial (Quellen, Bilder, Curricula): immer das Urheberrecht beachten.** Füge nur Inhalte hinzu, die du selbst erstellt hast oder die eindeutig für diesen Zweck lizenziert sind (z. B. gemeinfrei oder eine kompatible Lizenz). Im Zweifel verlinke auf die Originalquelle, statt sie zu kopieren, und halte die Quelle fest. Das gilt für Texte, Bilder, Diagramme, Übungen und Prüfungsaufgaben gleichermaßen.

---

## Deinen Vault zurück ins open-lectures-Repo veröffentlichen

Wenn du deinen Vault zurück in das open-lectures-Repository einbringen möchtest, achte darauf, dass deine eigene Kiro-Konfiguration nicht mit der gemeinsamen Konfiguration des Repositories kollidiert.

**Kollisionen mit der globalen Kiro-Konfiguration vermeiden.** Das Repository hat gemeinsame Steering-Dateien, Hooks und Skills unter `.kiro/`. Falls du eigene erstellt hast, mache **eines** der Folgenden, damit sie die globalen nicht überschreiben oder mit ihnen in Konflikt geraten:

- **Eigene Namensgebung (Namespacing).** Gib deinen Dateien ein individuelles Präfix, z. B. `.kiro/steering/meinvault-konventionen.md`, `.kiro/skills/meinvault-exporter/`, `.kiro/hooks/meinvault-check.json`.
- **Von der Synchronisierung ausschließen.** Nutze `.gitignore`, damit deine persönlichen Steuerdateien nicht in das gemeinsame Repo committed/synchronisiert werden.
- **Eigenes Kiro-Steuerverzeichnis verwenden.** Pflege dein eigenes, von diesem Repository unabhängiges Kiro-Steuerverzeichnis und übertrage nur die Vault-Inhalte.

> ‼️ **Schreibe NIEMALS Passwörter oder Zugangsdaten in deinen Vault.** Keine Zugriffstokens, API-Schlüssel, Logins oder Geheimnisse — weder in Notizen noch im Frontmatter, noch in Steering/Hooks/Skills, noch in Beispielcode. Alles, was hier committed wird, ist unter der Repository-Lizenz öffentlich. Falls doch einmal ein Geheimnis in eine Datei gelangt, behandle es als kompromittiert, entferne es und wechsle es (rotieren).

---

## Überblick über den Arbeitsablauf

Einen Vault zu erstellen ist ein mehrstufiger Prozess. Arbeite **von oben nach unten**, und innerhalb jeder Inhaltsstufe **Modul für Modul** statt alles auf einmal. Halte die Dateien bis ganz zum Schluss im Status `draft`.

| # | Phase | Ziel |
|---|-------|------|
| 1 | Umfang & Abgrenzung | Festlegen, was der Vault abdeckt — und was nicht |
| 2 | Tiefe | Niveau und fachliche Tiefe festlegen |
| 3 | Syllabus | Das Curriculum definieren (eigen, aus Lehrplänen oder bestehenden Curricula — Urheberrecht beachten) |
| 4 | Gerüst | Den vault-creator die leere Struktur bauen lassen |
| 5 | Metadaten | Die Frontmatter-Vorgaben bereitstellen und anwenden lassen |
| 6 | Basisinhalt | Basisinhalt erzeugen; optional den Agenten an geeigneten Stellen ASCII-Diagramme einfügen lassen |
| 7 | Strukturkontrolle | Ergebnis der vorherigen Schritte prüfen; präzise und Stück für Stück korrigieren |
| 8 | Umfang & Tiefe anpassen | Inhalt an den gewünschten Umfang und die fachliche Tiefe anpassen (die KI kann helfen) |
| 9 | Redaktionelle Prüfung | Sachliche Richtigkeit, Logik und didaktische Reihenfolge prüfen |
| 10 | Grafiken | ASCII-Diagramme nach Vorgabe in PNGs wandeln; je Grafik fachliche Korrektheit und Angemessenheit prüfen; Bildunterschriften kontrollieren |
| 11 | Bildmaterial | Bildmaterial ergänzen — **Urheberrecht beachten!** |
| 12 | Verzeichnisse | Glossar, Abkürzungsverzeichnis, Abbildungsverzeichnis erstellen (lassen) |
| 13 | Finales Review | Fachliche, inhaltliche und didaktische Prüfung — am besten mit einer Drittperson |
| 14 | Finalisieren | Dateien erst jetzt als `final` markieren; vorher bleiben sie `draft` (bei Bedarf versionieren) |
| 15 | Kontinuierliche Verbesserung | Fehler beheben, Inhalte anpassen/aktualisieren und Feedback berücksichtigen |

---

## Die 15 Schritte im Detail

### 1. Über Umfang und Abgrenzung nachdenken

Bevor irgendetwas erzeugt wird, kläre, **was in den Vault gehört und was nicht**. Ein scharf umrissener Umfang verhindert späteres Ausufern und ungleichmäßiges Material. Notiere ausdrücklich, welche Nachbarthemen *außerhalb* des Umfangs liegen und – wo sinnvoll – welcher andere Vault sie abdeckt.

> **Prompt**
> Ich plane einen Vault zu „[Thema]". Hilf mir, den Umfang festzulegen: Liste auf, was abgedeckt werden soll, was ausdrücklich ausgeschlossen wird und welche angrenzenden Themen in andere Vaults gehören. Stelle Rückfragen, wo die Abgrenzung unklar ist.

### 2. Über die Tiefe nachdenken

Lege **Zielgruppe und Niveau** fest (z. B. Mittlere Reife, Abitur, Bachelor, Zertifizierung). Die Tiefe bestimmt die Fachsprache, welche Beweise/Herleitungen gezeigt werden und wie viel Vorwissen vorausgesetzt wird.

> **Prompt**
> Der Vault richtet sich an [Zielgruppe/Niveau]. Schlage eine passende fachliche Tiefe vor: welcher Grad an Strenge, welche Herleitungen oder Beweise einzuschließen oder wegzulassen sind und welches Vorwissen ich voraussetzen darf. Weise auf Stellen hin, an denen Tiefen-Entscheidungen didaktische Folgen haben.

### 3. Einen Syllabus erstellen

Übersetze Umfang und Tiefe in ein **konkretes Curriculum**: eine geordnete Liste von Modulen (Kapiteln), jedes mit einem kurzen Lernziel. Stütze dich auf deine eigene Gliederung, auf offizielle Lehrpläne oder bestehende Curricula — **aber beachte das Urheberrecht**: Nutze Curricula zur Orientierung, kopiere keine geschützten Texte wörtlich.

> **Prompt**
> Entwirf einen Syllabus für „[Thema]" auf Niveau [Niveau]: Module in Lehrreihenfolge, jedes mit einem einzeiligen Lernziel. Stütze dich auf [meine Unterlagen / die für dieses Fach übliche Struktur]. Kopiere keinen urheberrechtlich geschützten Lehrplan-Text wörtlich — nutze ihn nur zur Orientierung. Warte auf meine Bestätigung.

### 4. Den vault-creator beauftragen

Lass den Skill `vault-creator` die leere Struktur bauen: Verzeichnisse, Index-Dateien, Templates und die grundlegende Obsidian-Konfiguration.

> **Prompt**
> Lade den vault-creator Skill und erstelle das Gerüst für einen Vault namens „[Vault-Name]" für „[Kurstitel]". Module: [Thema 1], [Thema 2], [Thema 3], … . Autor: [Dein Name]. Sprache: Deutsch. Folge den Repository-Konventionen.

### 5. Metadaten bereitstellen und anwenden lassen

Einige dich auf die **Frontmatter-Vorgaben** (Autor, created/modified-Daten, Tags und `status: draft`) und lass sie der Agent einheitlich über alle erzeugten Dateien anwenden.

> **Prompt**
> Lege die Frontmatter-Vorgaben für „[Vault-Name]" fest: Autor „[Dein Name]", Status „draft", created heute, Tags [Liste]. Wende sie auf jede Notiz an und melde jede Datei, der Frontmatter fehlte.

### 6. Basisinhalt erzeugen lassen

Befülle die Module zunächst mit **Basisinhalt** — ziele noch nicht auf die finale Tiefe. Teile dem Agenten mit, wo er aus dem Kontext oder deinem Quellenmaterial ASCII-Diagramme einfügen soll (sie lassen sich leicht verfeinern und später in PNGs wandeln).

> **Prompt**
> Lade den lecture-writer Skill und schreibe Basisinhalt für Modul [N] „[Kapiteltitel]" von „[Vault-Name]": eine Notiz je Unterthema mit Lernzielen, Prüfungsrelevanz und Querverweisen. Halte es auf Basistiefe und im Status draft. Wo ein Konzept von einer Skizze profitiert, füge ein einfaches ASCII-Diagramm in einem Codeblock ein.

> ‼️ Wenn du auf eigene Unterlagen oder gemeinfreie/kompatibel lizenzierte Quellen zurückgreifst, beachte den Urheberrechts-Hinweis von oben und halte Quellen fest.

### 7. Die Struktur kontrollieren

Prüfe das Ergebnis der vorherigen Schritte: Benennung, Indizes, Querverweise, Frontmatter, Ordnerstruktur. Lass Korrekturen **präzise und Stück für Stück** ausführen — frage nach einer Begründung (Reasoning), wo eine Änderung nicht offensichtlich ist, und behebe die Dinge nach und nach statt alles auf einmal.

> **Prompt**
> Prüfe die bisherige Struktur von „[Vault-Name]": Dateibenennung, Index-Dateien, Querverweise und Frontmatter. Liste Probleme mit je einer kurzen Begründung. Behebe sie dann gruppenweise und pausiere nach jeder Gruppe zur Bestätigung — ändere nicht alles auf einmal.

### 8. Umfang und Tiefe anpassen

Bringe den Inhalt nun auf den **gewünschten Umfang und die fachliche Tiefe**. Erweitere dünne Abschnitte, kürze Abschweifungen außerhalb des Umfangs und richte den Schwierigkeitsgrad an den Entscheidungen aus Schritt 1–2 aus. Die KI kann vorschlagen, wo Inhalt zu flach oder zu tief ist.

> **Prompt**
> Vergleiche Modul [N] mit unserem vereinbarten Umfang und der Tiefe ([Kurzfassung]). Weise auf Abschnitte hin, die zu flach, zu tief oder außerhalb des Umfangs sind, und schlage konkrete Anpassungen vor, bevor du sie anwendest.

### 9. Redaktionelle Prüfung

Prüfe **sachliche Richtigkeit, innere Logik und didaktische Reihenfolge**: Baut jedes Konzept auf dem Vorherigen auf? Werden Definitionen eingeführt, bevor sie verwendet werden?

> **Prompt**
> Führe eine redaktionelle Prüfung von Modul [N] durch: sachliche Richtigkeit, logische Konsistenz und didaktische Reihenfolge (nichts wird verwendet, bevor es eingeführt ist). Melde Probleme mit Begründung und behebe sie dann schrittweise.

### 10. ASCII-Diagramme in PNG-Grafiken wandeln

Wandle die ASCII-Diagramme **nach den Grafik-Vorgaben** in PNGs. Prüfe für jedes Diagramm, dass die Darstellung **fachlich korrekt** und für den zu verdeutlichenden Sachverhalt **angemessen** ist und dass die **Bildunterschrift** der Konvention folgt (Kennung + Beschreibung).

> **Prompt**
> Wandle die ASCII-Diagramme in [Datei] in PNGs gemäß dem create-png Skill und dem math-graphics Steering. Bestätige für jedes, dass die Darstellung fachlich/mathematisch korrekt und für die gemeinte Aussage geeignet ist. Zeige mir Vorschauen auf hellem und dunklem Hintergrund vor dem Anwenden und verwende das korrekte Bildunterschriften-Format.

> Für strukturelle Diagramme (Lernpfade, Abläufe, Hierarchien) bevorzuge **Mermaid**-Blöcke, damit sie editierbar und seitenbreitensicher bleiben.

### 11. Bildmaterial hinzufügen

Ergänze Fotos oder anderes Bildmaterial, wo es hilft — **und beachte das Urheberrecht strikt**. Nutze nur selbst erstellte Bilder oder eindeutig kompatible Lizenzen; lege Assets gemäß den Konventionen neben die Notiz und versieh sie mit einer Bildunterschrift.

> **Prompt**
> Schlage vor, wo ein Bild Modul [N] stärken würde, und liste auf, was jedes Bild zeigen soll. Ich stelle Bilder bereit, die ich verwenden darf. Lade oder binde keine fremden Bilder ohne bestätigte kompatible Lizenz ein.

### 12. Die Verzeichnisse erstellen

Lass den Agenten aus dem fertigen Inhalt **Glossar, Abkürzungsverzeichnis und Abbildungsverzeichnis** erstellen.

> **Prompt**
> Erstelle ein Glossar, ein Abkürzungsverzeichnis und ein Abbildungsverzeichnis für „[Vault-Name]" aus den vorhandenen Notizen. Verlinke Glossarbegriffe an ihrer ersten Nennung.

### 13. Finales Review

Führe ein **finales Review** durch — fachlich, inhaltlich und didaktisch — am besten **mit oder durch eine Drittperson**. Ein zweites Augenpaar findet Lücken, die Autor und KI beide übersehen.

> **Prompt**
> Erstelle eine Review-Checkliste für „[Vault-Name]" zu fachlicher Korrektheit, Vollständigkeit und didaktischem Fluss, damit eine prüfende Person sie Modul für Modul durcharbeiten kann.

### 14. Finalisieren

**Erst nach dem Review** markierst du die Dateien als `final`. Bis dahin bleiben sie `draft`; versioniere sie, falls du Revisionen nachhältst. Dann committen.

> **Prompt**
> Markiere alle Hauptkapitel-Dateien von Modul [N] in „[Vault-Name]" als final (status: final) und führe einen Commit durch. Lass alles, was noch in Prüfung ist, als draft.

### 15. Kontinuierliche Verbesserung

Ein Vault ist nie wirklich „fertig". Betrachte `final` als „einsatzbereit", nicht als „eingefroren". Mit der Zeit wirst du **Fehler beheben**, **Inhalte anpassen oder aktualisieren** (neue Entwicklungen, klarere Erklärungen, bessere Beispiele) und **Feedback berücksichtigen** — von Lernenden, Prüfenden oder Mitautor(inn)en. Halte Änderungen klein, begründet und in beschrifteten Schritten committed, damit die Historie nachvollziehbar bleibt; wiederhole die redaktionelle und die Grafik-Prüfung für alles, was du anfasst, und beachte das Urheberrecht für neu hinzugefügtes Material.

> **Prompt**
> Hier ist Feedback zu „[Vault-Name]": [Feedback einfügen / Fehler beschreiben]. Schlage konkrete Korrekturen mit je einer kurzen Begründung vor und wende sie dann schrittweise an. Halte Bildunterschriften und Konventionen ein und markiere alles, was eine fachliche oder didaktische Nachprüfung braucht.

---

## Vorhandenes Steering

Steering-Dateien in `.kiro/steering/` kodieren die Repository-Konventionen, damit der Agent konsistent bleibt. Die meisten werden automatisch angewandt; du kannst eine in einem Prompt namentlich nennen, um sicherzugehen, dass sie beachtet wird.

| Steering-Datei | Zweck |
|----------------|-------|
| `product.md` | Was open-lectures ist und für wen |
| `structure.md` | Ordner-/Dateiorganisation des Repositories |
| `tech.md` | Werkzeuge und Tech-Stack |
| `obsidian-markdown.md` | Markdown-Konventionen (Wiki-Links, Callouts, Bildunterschriften, Assets, Frontmatter) |
| `obsidian-lecture-notes.md` | Didaktischer Aufbau einer Vorlesungsnotiz |
| `math-graphics.md` | Farbschema und Regeln für Mathe-PNG-Grafiken |

---

## Vorhandene Skills

Skills in `.kiro/skills/` bündeln wiederkehrende Arbeitsabläufe. Bitte Kiro, „den Skill [Name] zu laden", oder beschreibe eine passende Aufgabe.

| Skill | Damit … |
|-------|---------|
| `vault-creator` | Gerüst für einen kompletten neuen Vault (Ordner, Indizes, Templates, Konfig) |
| `lecture-writer` | Strukturierte akademische Vorlesungsnotizen schreiben |
| `lecture-processor` | Rohe/importierte Notizen in das Hausformat bringen |
| `exercise-generator` | Übungsaufgaben und Musterprüfungen mit Lösungen erzeugen |
| `create-png` | Theme-sichere PNG-Illustrationen erzeugen (Farb- + Graustufen-Paar) |
| `markdown-validator` | Notizen gegen die Steering-Konventionen prüfen |
| `source-extractor` | Quellenmaterial extrahieren und organisieren |

## Hooks

Automatisierungen in `.kiro/hooks/` laufen bei Ereignissen — ohne manuelles Zutun:

| Hook | Auslöser | Wirkung |
|------|----------|---------|
| `update-modified-date.json` | Beim Speichern | Setzt das Frontmatter-Feld `modified` auf heute |
| `sync-english-docs.json` | Bei Doku-Änderung | Hält englische/deutsche Dokumente synchron |
| `date-awareness.json` | Sitzungsbeginn | Fügt das aktuelle Datum in den Kontext ein |

---

## Eigenes Steering hinzufügen

Nutze Steering, um Regeln zu ergänzen, die über Interaktionen hinweg gelten sollen — einen Hausstil, eine Benennungsregel, eine fachliche Konvention.

1. Lege eine Markdown-Datei in `.kiro/steering/` an, z. B. `meine-konventionen.md`.
2. Wähle einen Inklusionsmodus über das Frontmatter:
   - **Immer** (Standard): kein Frontmatter nötig; wird auf jede Anfrage angewandt.
   - **Dateibezogen**: `inclusion: fileMatch` + `fileMatchPattern: 'README*'`.
   - **Manuell**: `inclusion: manual` — du ziehst es per `#` im Chat hinzu.
   - **Auto (bei Bedarf)**: `inclusion: auto` + `name` + `description` — wird aktiviert, wenn die Anfrage zur Beschreibung passt.
3. Schreibe die Regeln als klare, imperative Stichpunkte.
4. Optional kannst du andere Dateien mit `#[[file:relativer/pfad]]` einbetten, um dem Agenten zusätzlichen Kontext zu geben (z. B. eine Spezifikation).

```yaml
---
inclusion: auto
name: meine-konventionen
description: Hausregeln für Benennung und Tonalität in meinen Vaults
---
```

---

## Einen eigenen Skill hinzufügen

Nutze einen Skill, um einen wiederkehrenden Arbeitsablauf mit eigenen Anweisungen zu bündeln.

1. Lege ein Verzeichnis in `.kiro/skills/` an, z. B. `.kiro/skills/mein-skill/`.
2. Füge eine `SKILL.md` mit Frontmatter hinzu, das Name und Zweck beschreibt:

```yaml
---
name: mein-skill
description: Ein Satz dazu, was er tut und wann er zu verwenden ist. Der Agent liest dies, um zu entscheiden, wann der Skill angewandt wird.
---
```

3. Beschreibe im Textkörper die erforderlichen Eingaben, den Output-Vertrag und einen Schritt-für-Schritt-Ablauf. Halte die Anweisungen explizit — der Agent folgt ihnen wörtlich.
4. Optional füge Hilfsskripte oder Referenzdateien im Skill-Verzeichnis hinzu und verweise aus der `SKILL.md` darauf.
5. Rufe ihn auf, indem du Kiro bittest, „den Skill mein-skill zu laden", oder eine passende Aufgabe beschreibst.

> Tipp: Orientiere deinen Skill an einem bestehenden (z. B. `create-png/SKILL.md`), um Struktur und Ton zu treffen.

---

## Bewährte Praktiken

- **Nachdenken vor dem Generieren.** Umfang, Tiefe und Syllabus (Schritte 1–3) entscheiden über die Qualität von allem Weiteren.
- **Modul für Modul arbeiten.** Schreiben → Prüfen → Anpassen → Review → Finalisieren, jeweils ein Modul.
- **Inkrementell korrigieren.** Begründung erbitten und Korrekturen in kleinen Gruppen anwenden, nicht alles auf einmal.
- **Grafiken theme-sicher und korrekt halten.** Farb- + Graustufen-Variante, kein reines Schwarz/Weiß, und die Darstellung auf fachliche Richtigkeit prüfen.
- **Urheberrecht in jedem Schritt beachten** — Texte, Curricula, Bilder, Übungen.
- **Bis zum finalen Review im Status draft bleiben.** Erst danach auf `final` umstellen.
- **In kleinen, beschrifteten Schritten committen**, damit die Arbeit nachvollziehbar und umkehrbar bleibt.
