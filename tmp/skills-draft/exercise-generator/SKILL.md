---
name: exercise-generator
description: Generate practice exercises and exam questions from existing lecture content. Use when creating Übungsaufgaben, sample exams, or practice problems for a lecture topic. Produces exercises with separate solutions following repository conventions.
---

# Exercise Generator — Open Lectures

Create educational exercises and exam questions based on lecture content.

## Output types

1. **Übungsaufgaben** — Practice exercises with solutions
2. **Prüfungsfragen** — Exam-style questions
3. **Selbsttest** — Self-assessment quizzes

## Required output format

### Exercise file structure
```markdown
---
author: [Author]
title: [Exercise Title]
tags:
  - uebung
  - [topic tags]
created: YYYY-MM-DD
modified: YYYY-MM-DD
related: [[Source Lecture Note]]
difficulty: [leicht|mittel|schwer]
---

# [Exercise Title]

> [!info] **Lernziele**
> Diese Übung hilft dir:
> - [Skill 1]
> - [Skill 2]

## Aufgabe 1: [Title]

[Problem statement]

**Hinweise:**
- [Hint if needed]

---

## Aufgabe 2: [Title]

[Problem statement]

---

## Lösungen

> [!warning] **Spoiler-Warnung**
> Versuche die Aufgaben zuerst selbst zu lösen!

### Lösung 1

[Detailed solution with explanation]

### Lösung 2

[Detailed solution with explanation]
```

## Workflow

1. **Identify source material:**
   - Which lecture note(s) to base exercises on
   - Specific topics or concepts to cover
   - Target difficulty level

2. **Analyze learning objectives:**
   - Read the source note's Lernziele
   - Read the Prüfungsrelevant section
   - Identify key concepts that need practice

3. **Design exercises:**
   - Mix of question types:
     - Conceptual understanding
     - Application/calculation
     - Analysis/comparison
     - Problem-solving
   - Progressive difficulty within set
   - Cover different aspects of the topic

4. **Generate content:**
   - Clear, unambiguous problem statements
   - Realistic scenarios where applicable
   - Include necessary data/given values
   - Add hints for harder problems

5. **Write solutions:**
   - Step-by-step explanations
   - Show work, not just answers
   - Explain why, not just how
   - Reference back to lecture concepts

6. **Determine file location:**
   - Place in `0n-Aufgaben/Uebungen/` or equivalent
   - Filename: `U-[Topic]-[Subtopic].md` for exercises
   - Filename: `P-[Topic]-[Subtopic].md` for exam practice

7. **Quality check:**
   - Solutions are correct and complete
   - Difficulty matches stated level
   - Cross-references to source material work
   - No ambiguous questions

8. **Present for review:**
   - Show exercises without solutions first (optional)
   - Then show complete file
   - Confirm placement and naming

## Exercise types by topic area

### Programming/Technical
- Code completion
- Bug finding
- Output prediction
- Implementation tasks
- Complexity analysis

### Theoretical/Conceptual
- Definition questions
- Compare and contrast
- True/false with justification
- Diagram labeling
- Process ordering

### Mathematical
- Calculations with formulas
- Proof sketches
- Algorithm tracing
- Optimization problems

## Difficulty guidelines

| Level | German | Characteristics |
|-------|--------|-----------------|
| Easy | leicht | Direct application of concepts, single-step |
| Medium | mittel | Combination of concepts, multi-step |
| Hard | schwer | Novel situations, requires synthesis |

## Language

Write in **German** unless explicitly requested otherwise.
