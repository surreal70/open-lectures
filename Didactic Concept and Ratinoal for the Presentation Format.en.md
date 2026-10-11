# Didactic Concept and Rationale for the Presentation Format
## A Networked, Multimedia, and Extensible Knowledge Environment Based on Obsidian

**Document Type:** Conceptual Rationale (Design Rationale)  
**Project:** Open Lectures  
**Objective:** To explain and justify the didactic, technical, and design decisions behind providing teaching and learning materials as Obsidian Vaults.

---

## 1. Motivation and Objectives

Traditional knowledge transfer in schools, universities, and professional education is often characterized by a multitude of separate information sources and media.

Lecture notes, textbooks, presentation slides, exercises, programming examples, scientific publications, and supplementary online resources are frequently distributed across different formats and platforms.

As a result, learners must regularly switch between different media and sources of information.

Typical examples include:

- Lecture notes provide the theoretical foundations.
- Textbooks offer more detailed explanations.
- Presentations contain diagrams and visualizations.
- Laboratory instructions describe practical experiments.
- Separate repositories provide programming examples.
- Websites and scientific publications supplement the material.
- Personal notes are maintained in another application.

This fragmentation creates additional effort when searching for information and navigating between resources. It can also make relationships between individual topics more difficult to recognize.

The **Open Lectures** project therefore pursues an integrated approach.

> [!abstract] **Guiding Principle**
> Teaching and learning materials should not be provided as isolated documents but as an interconnected, multimedia, and individually extensible knowledge environment.
>
> The Obsidian Vault serves as a central access point for theoretical foundations, visualizations, practical applications, exercises, supplementary literature, and personal knowledge organization.

The long-term objective is to create a comprehensive **One-Stop Learning Resource**.

It should simplify access to relevant information, minimize unnecessary transitions between media, and support independent, in-depth learning.

---

# 2. Fundamental Didactic Principles

The concept is based on several interconnected principles.

| Principle | Objective |
|---|---|
| Visualization | Make complex concepts easier to understand |
| Information Density | Present essential relationships concisely |
| Contextualization | Supplement graphics and models with explanatory text |
| Practical Orientation | Connect theoretical knowledge with concrete applications |
| Experimentation | Enable active learning through exercises, code, and experiments |
| Interconnection | Make relationships between knowledge domains visible |
| Expandable Depth | Provide immediate access to additional information |
| Historical Context | Explain the development and motivation behind concepts |
| Individualization | Enable personal additions and individual learning paths |
| Media Integration | Combine different learning resources in one environment |

These principles are not independent requirements.

Instead, they complement one another and collectively establish a learning environment that supports both structured introductions and individual exploration.

---

# 3. Visualization as a Central Teaching Instrument

## 3.1 Motivation

Many technical and scientific concepts can be communicated more effectively through graphical representations than through textual explanations alone.

This is particularly true for:

- System architectures
- Hierarchical structures
- Process flows
- State transitions
- Data flows
- Spatial relationships
- Cause-and-effect relationships
- Mathematical functions
- Temporal sequences
- Comparative representations

Diagrams should therefore constitute an essential component of the teaching materials.

## 3.2 High Information Density

A well-designed graphic can communicate several related pieces of information simultaneously.

For example, a diagram illustrating operating system memory management can show virtual address spaces, page tables, the Memory Management Unit, and physical memory within a single representation.

```text
         APPLICATION
              |
              v
    +-------------------+
    |  Virtual Address  |
    +-------------------+
              |
              v
    +-------------------+
    |        MMU        |
    +-------------------+
              |
              v
    +-------------------+
    |    Page Table     |
    +-------------------+
              |
              v
    +-------------------+
    |   Physical RAM    |
    +-------------------+
```

*Figure 1: Simplified representation of virtual memory addressing.*

**Description:** The diagram illustrates the fundamental translation of a virtual memory address into its corresponding physical address. The MMU performs address translation using page tables managed by the operating system. In real systems, additional mechanisms such as Translation Lookaside Buffers and multilevel page tables may be involved.

The representation provides an overview that can subsequently be used to explain individual components in greater detail.

## 3.3 Design Principles

Graphics should:

1. Serve a clearly identifiable educational purpose.
2. Represent the essential components and their relationships.
3. Contain as few purely decorative elements as possible.
4. Follow an easily understandable reading direction.
5. Use consistent symbols, colors, and terminology.
6. Remain understandable without relying exclusively on color.
7. Be readable in both light and dark Obsidian themes.
8. Include an explanatory caption.
9. Be supplemented by detailed text when necessary.

**High information density does not mean maximum complexity.**

Overloaded diagrams can make concepts more difficult to understand. Complex systems should therefore be explained using multiple progressively detailed illustrations when appropriate.

---

# 4. Text as a Contextual and Explanatory Layer

## 4.1 Combining Graphics and Text

Within this concept, graphics primarily serve to visualize structures and relationships.

Text complements these representations by providing:

- Definitions
- Explanations
- Background information
- Technical details
- Prerequisites
- Limitations
- Examples
- Derivations
- Interpretations

Combining both approaches provides different ways of accessing the same information.

A graphic can offer an immediate overview, while the accompanying text supports a deeper understanding.

## 4.2 Multilevel Presentation of Information

Whenever appropriate, content should be organized into several levels of detail.

```text
+--------------------------------------+
|               TOPIC                  |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
|          VISUAL OVERVIEW             |
|                                      |
|     Diagram / Graphic / Model        |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
|        BASIC EXPLANATION             |
|                                      |
|     Concepts and Relationships       |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
|         DETAILED ANALYSIS            |
|                                      |
|     Mechanisms and Background        |
+--------------------------------------+
                  |
                  v
+--------------------------------------+
|       ADDITIONAL INFORMATION         |
|                                      |
|     Literature / Sources / Examples  |
+--------------------------------------+
```

*Figure 2: Multilevel structure for presenting knowledge.*

**Description:** The diagram illustrates the intended structure of a learning section. Beginning with a visual overview, the essential relationships are explained. This is followed by technical details and opportunities for further exploration.

This structure accommodates different levels of prior knowledge and individual interests.

Beginners can initially focus on the fundamentals, while advanced learners can explore the more detailed information.

---

# 5. Practical Orientation and Real-World Applications

## 5.1 Motivation

Theoretical knowledge becomes particularly relevant when learners understand where and why it is needed in practice.

Teaching materials should therefore establish a direct connection between theoretical concepts and real-world applications.

This is especially important in computer science, mathematics, chemistry, physics, and engineering.

## 5.2 Structure of Practice-Oriented Sections

A suitable didactic pattern consists of five steps:

1. **Problem Statement:** What practical problem needs to be solved?
2. **Theoretical Foundation:** Which concepts are required?
3. **Solution Approach:** How is the theory applied?
4. **Practical Example:** What does a concrete implementation look like?
5. **Evaluation:** What are the results, limitations, and alternatives?

### Example: Race Conditions

In an operating systems lecture, a race condition can initially be explained using a bank account.

Two processes access the same account balance simultaneously.

The example then demonstrates how unsynchronized access can lead to incorrect results and how a mutex can prevent this problem.

The practical connection illustrates that synchronization is not merely a theoretical concept but a fundamental requirement for reliable software.

## 5.3 Benefits

Practical orientation aims to:

- Demonstrate the usefulness of theoretical concepts.
- Increase learner motivation.
- Facilitate the transfer of knowledge to real-world problems.
- Make technical design decisions understandable.
- Encourage independent experimentation.

---

# 6. Programming Examples and Executable Code

## 6.1 Objectives

For technically oriented learners, suitable chapters should be supplemented with executable programming examples.

Code provides an opportunity to translate abstract concepts into observable system behavior.

One example is process creation under Linux.

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(void)
{
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        return 1;
    }

    if (pid == 0) {
        printf("Child process: PID=%ld\n",
               (long)getpid());
    } else {
        printf("Parent process: PID=%ld\n",
               (long)getpid());

        if (waitpid(pid, NULL, 0) == -1) {
            perror("waitpid");
            return 1;
        }
    }

    return 0;
}
```

This example demonstrates the creation of a child process using the `fork()` system call.

It can be compiled and executed in a Linux environment.

## 6.2 Requirements for Code Examples

Programming examples should:

1. Have a clearly defined learning objective.
2. Be as complete and executable as possible.
3. Specify the required runtime environment.
4. Explain important sections of the code.
5. Describe the expected results.
6. Handle errors appropriately.
7. Address relevant security considerations.
8. Offer extension exercises when appropriate.

Not every topic requires programming code.

Code should be included whenever it genuinely improves understanding.

---

# 7. Contextual Integration of External Resources

## 7.1 Motivation

A single teaching document cannot and should not attempt to cover every aspect of a subject exhaustively.

External resources should therefore be integrated into the relevant technical context.

These resources may include:

- Textbooks
- Scientific publications
- Official documentation
- Technical standards
- Simulations
- Interactive learning tools
- Recorded lectures
- Open-source projects
- Advanced tutorials

## 7.2 Contextual Linking

External resources should preferably be linked directly where they are relevant to the topic being discussed.

For example, a chapter on CPU scheduling can link directly to an interactive scheduling simulator such as AnimOS.

This allows learners to experiment with the algorithms immediately.

A centralized collection of links at the end of an extensive document would provide less direct contextual support.

## 7.3 Source Quality

The following criteria should be considered when selecting external resources:

1. Technical reliability
2. Currency
3. Clarity
4. Appropriate academic level
5. Accessibility
6. Long-term availability
7. Legal usability
8. Recognizable added value

Official documentation and academically established sources should be preferred for technical details.

External links should also include brief descriptions so learners can understand what additional information is available.

---

# 8. Historical Context, Trivia, and Interesting Background Information

## 8.1 Didactic Motivation

Scientific and technological developments do not occur independently of their historical context.

Many concepts become easier to understand when learners know how they originated and which problems they were initially intended to solve.

Historical information should therefore be an intentional component of the teaching materials.

## 8.2 Possible Content

- Historical development of a method
- Original problem statements
- Influential scientists and developers
- Technological milestones
- Earlier solution approaches
- Interesting technological failures
- Historical security incidents
- Unexpected applications
- Scientific controversies

### Example: Operating Systems

> [!tip] **Historical Background**
> Early computer systems often executed programs without the sophisticated operating system abstractions available today.
>
> The development of batch processing, multiprogramming, and time-sharing enabled increasingly efficient and interactive use of expensive computing systems.
>
> Many modern concepts of process management and scheduling originated from these developments.

## 8.3 Requirements for Trivia

Trivia should not merely provide entertainment but also contribute educational value.

Suitable historical information can:

- Explain the origin of a concept.
- Illustrate a technical problem.
- Establish a broader societal context.
- Stimulate curiosity.
- Support the retention of important concepts.

The information should be factually accurate, verifiable, and clearly distinguished from the primary learning objectives.

---

# 9. Wiki Principles and Nonlinear Knowledge Navigation

## 9.1 Limitations of Linear Documents

Traditional textbooks and lecture notes are predominantly organized in a linear manner.

Although this structure is useful for systematic learning, it only partially reflects the numerous relationships between different areas of knowledge.

For example, process management, memory management, synchronization, and file systems are closely interconnected.

A linear structure can explain these relationships, but it does not always allow immediate navigation between related concepts.

## 9.2 Wiki-Based Knowledge Organization

Obsidian allows individual documents to be linked directly through internal wiki-links.

Example:

```markdown
[[Virtual Memory Management]] enables the
isolation of address spaces belonging to
different [[Processes]].

When memory is shared, [[Race Conditions]]
may occur.

To prevent such problems,
[[Synchronization Mechanisms]] are used.
```

This allows learners to navigate immediately to related topics.

## 9.3 Two Navigation Approaches

The learning environment should support two equally important navigation methods.

**Linear Navigation:** A predefined learning path systematically guides learners through the material.

**Nonlinear Navigation:** Wiki-links allow targeted reference and individual exploration.

```text
                LECTURE
                   |
                   v
           +---------------+
           |   Chapter 1   |
           +---------------+
                   |
                   v
           +---------------+
           |   Chapter 2   |----------+
           +---------------+          |
                   |                  |
                   v                  v
           +---------------+   +-------------+
           |   Chapter 3   |<->|   Concept   |
           +---------------+   +-------------+
                   |                  |
                   v                  v
           +---------------+   +-------------+
           |   Chapter 4   |<->|  Deep Dive  |
           +---------------+   +-------------+
```

*Figure 3: Linear and nonlinear navigation within a lecture.*

**Description:** The left side represents a traditional sequential learning path. Cross-links allow learners to access definitions, related topics, or additional information at any time.

The linear learning path remains intact while being supplemented by opportunities for individual navigation.

---

# 10. Knowledge Graphs and Visualization of Conceptual Relationships

## 10.1 The Obsidian Graph View

A particular advantage of Obsidian is its ability to visualize internal links between documents as a graph.

In this representation:

- Documents are displayed as nodes.
- Links are displayed as connections.

## 10.2 Thematic Knowledge Clusters

Systematic linking can create thematic clusters.

```text
                    OPERATING SYSTEMS
                            |
            +---------------+---------------+
            |               |               |
            v               v               v
        PROCESSES         MEMORY            I/O
            |               |               |
        +---+---+       +---+---+       +---+---+
        |       |       |       |       |       |
        v       v       v       v       v       v
     Threads Scheduling Paging  MMU    DMA   Interrupts
        |
        v
   Synchronization
        |
     +--+--+
     |     |
     v     v
    Mutex Deadlock
```

*Figure 4: Simplified conceptual knowledge graph for an operating systems lecture.*

**Description:** The diagram illustrates relationships between the central topics of operating systems. Processes are associated with threads, scheduling, and synchronization, while memory management is connected to paging and the MMU.

In an actual Obsidian Graph View, additional cross-connections may become visible through wiki-links.

## 10.3 Educational Benefits

The Graph View can help learners:

1. Discover relationships between topics.
2. Identify central concepts.
3. Recognize thematic clusters.
4. Locate isolated documents.
5. Connect different knowledge domains.
6. Reflect on their learning progress.

However, the Graph View initially represents only the existing link structure.

A highly connected node is not necessarily more important from an academic perspective. Similarly, a missing connection does not necessarily imply that two subjects are unrelated.

**The usefulness of the graph therefore depends significantly on the quality of the internal linking structure.**

---

# 11. Individual Extensibility and Personal Knowledge Organization

## 11.1 From Passive Consumers to Active Knowledge Contributors

A central objective of the concept is to avoid limiting learners to the passive role of readers.

Instead, they should be able to expand the provided materials and adapt them to their individual learning needs.

Possible additions include:

- Personal notes
- Additional explanations
- Personal summaries
- Original examples
- Custom diagrams
- Programming experiments
- Additional sources
- Exercises
- Links to related topics

## 11.2 Separating Original Content from Personal Additions

To support long-term maintainability, a clear separation is recommended.

For example:

```text
operating-systems/
|
+-- 01-Fundamentals/
|
+-- 02-Processes/
|
+-- 03-Memory-Management/
|
+-- 04-IO/
|
+-- 05-Synchronization/
|
+-- 06-File-Systems/
|
+-- 07-System-Calls/
|
+-- My-Notes/
|   |
|   +-- Questions.md
|   +-- Summaries.md
|   +-- Personal-Examples.md
|
+-- Glossary.md
```

*Figure 5: Example of an individually extensible Vault structure.*

**Description:** The original lecture materials remain organized within a defined directory structure. Learners can create additional directories and documents and connect them to the provided content through wiki-links.

This represents a possible extension of the existing Vault conventions and should be defined as an optional area.

## 11.3 Advantages of Open Markdown Files

Using Markdown provides several benefits:

- Content remains human-readable.
- Files can be opened with different editors.
- Personal additions do not require proprietary document formats.
- Version control with Git is possible.
- Content can be processed automatically.
- Export to other formats is possible.
- Long-term dependence on a single application is reduced.

Within this concept, Obsidian serves as a convenient working environment.

The actual learning content remains largely independent of the application because it is stored in Markdown files.

However, specialized Obsidian features such as wiki-links, callouts, and certain plugins may not be supported consistently by other Markdown applications.

---

# 12. Minimizing Media Discontinuities

## 12.1 Problem Statement

When using traditional learning materials, learners often have to determine independently which information source is appropriate for a specific question.

Switching between lecture notes, textbooks, browsers, laboratory instructions, and programming environments interrupts the learning workflow.

Such transitions cannot be eliminated entirely, but they can be significantly reduced through appropriate organization.

## 12.2 Integrated Information Model

The proposed presentation format combines several types of information.

```text
                  +-------------------+
                  |                   |
                  |   OBSIDIAN VAULT  |
                  |                   |
                  +-------------------+
                            |
          +-----------------+-----------------+
          |                 |                 |
          v                 v                 v
  +---------------+ +---------------+ +---------------+
  |    THEORY     | | VISUALIZATION | |   PRACTICE    |
  |               | |               | |               |
  | Definitions   | | Diagrams      | | Examples      |
  | Explanations  | | Graphics      | | Exercises     |
  | Derivations   | | Models        | | Code          |
  +---------------+ +---------------+ +---------------+
          |                 |                 |
          +-----------------+-----------------+
                            |
                            v
                  +-------------------+
                  |   CONNECTIONS     |
                  |                   |
                  | Wiki-Links        |
                  | External Sources  |
                  | Knowledge Graph   |
                  +-------------------+
                            |
                            v
                  +-------------------+
                  |  INDIVIDUAL       |
                  |  LEARNING         |
                  |                   |
                  | Personal Notes    |
                  | Additions         |
                  | Experiments       |
                  +-------------------+
```

*Figure 6: The Obsidian Vault as an integrated learning environment.*

**Description:** The Obsidian Vault combines theoretical content, graphical representations, and practical applications. Internal and external links allow learners to move directly between related information. Personal additions make the knowledge environment individually extensible.

## 12.3 The One-Stop Resource Principle

The intended objective is not to copy all available information into the Vault.

Instead, the Vault should serve as the **central access point to information relevant to a particular learning topic**.

Learners should rarely need to search outside the provided learning environment for fundamental explanations or supplementary resources.

Additional information should instead be directly accessible.

This is achieved through:

1. Comprehensive fundamental explanations.
2. Contextual visualizations.
3. Practical examples.
4. Linked technical terminology.
5. Internal cross-references.
6. Supplementary literature.
7. External simulations.
8. Relevant programming examples.
9. Personal notes.

The result is a learning environment that supports a continuous and coherent workflow.

---

# 13. Modularity and Reusability

Another advantage of the wiki-based approach is the ability to address individual concepts in self-contained documents.

For example, a document about *entropy* can be referenced from several different courses:

- Cryptography
- Random Number Generation
- Information Theory
- Statistics
- Physics

This allows relationships between subjects to be established without repeating every explanation in full within each lecture.

## 13.1 Conceptual Modularity

Whenever possible, each document should address a clearly defined topic.

This supports:

- Targeted information retrieval
- Straightforward linking
- Maintenance and updates
- Reusability
- Clear graph structures

## 13.2 Independence of Individual Lecture Vaults

Since Open Lectures is designed around independent Obsidian Vaults, a distinction must be made between conceptual reusability and technical independence.

Each Vault should remain fully usable even when other courses are not installed.

Cross-disciplinary relationships can be established through external links or by explicitly incorporating locally stored materials.

This architecture prevents unwanted dependencies between individual lectures.

---

# 14. Quality Requirements for Teaching Materials

To ensure the concept remains sustainable over time, consistent quality requirements are necessary.

## 14.1 Academic Quality

- Correct definitions and statements
- Traceable explanations
- Unambiguous terminology
- Appropriate examples
- Verifiable sources
- Clear identification of simplifications
- Explicit documentation of assumptions

## 14.2 Visual Quality

- Meaningful diagrams
- Consistent design
- Consistent labeling
- Understandable legends
- Descriptive captions
- Appropriate information density

## 14.3 Didactic Quality

- Clear learning objectives
- Logical organization
- Explanations at an appropriate level
- Practical relevance
- Exercises and opportunities for self-assessment
- Different levels of detail
- Motivating supplementary information

## 14.4 Technical Quality

- Consistent Markdown structure
- Correct wiki-links
- Meaningful filenames
- Consistent metadata
- Functional external links
- Traceable directory structure
- Minimal dependence on specialized plugins
- Good readability in Obsidian

---

# 15. Limitations and Challenges

Despite its advantages, the proposed presentation format introduces several challenges.

### 15.1 Excessive Information Density

High information density can make concepts more difficult to understand if graphics or documents contain too many ideas simultaneously.

**Mitigation:** Multilevel explanations, clear structure, and progressively detailed diagrams.

### 15.2 Uncontrolled Interconnection

A large number of internal links can produce confusing graph structures.

**Mitigation:** Meaningful links, consistent terminology, and thematic overview pages.

### 15.3 Dependence on External Resources

External websites may be modified, relocated, or removed.

**Mitigation:** Complete bibliographic information, regular link validation, and legally permissible archiving where appropriate.

### 15.4 Different Learning Prerequisites

Not all learners have the same prior knowledge or prefer identical presentation styles.

**Mitigation:** Combine linear learning paths, visual overviews, detailed explanations, and optional advanced material.

### 15.5 Maintenance and Updates

A comprehensive knowledge collection requires continuous quality assurance.

**Mitigation:** Version control, clearly defined responsibilities, automated checks, and structured maintenance procedures.

### 15.6 Accessibility

Purely visual representations may be difficult to access for some learners.

**Mitigation:** Graphics should be accompanied by textual explanations. Essential information must not be communicated exclusively through color or spatial arrangement.

---

# 16. Success Criteria and Evaluation

The success of the concept should not be measured solely by the number of documents, graphics, or links.

The decisive question is whether the presentation format actually improves the learning process.

Possible evaluation criteria include:

| Criterion | Possible Evaluation |
|---|---|
| Comprehensibility | Learner feedback |
| Navigation | Time required to locate specific information |
| Learning Outcomes | Comprehension and transfer exercises |
| Practical Relevance | Successful completion of practical exercises |
| Interconnection | Use of conceptual cross-references |
| Completeness | Coverage of defined learning objectives |
| Source Quality | Academic review of references |
| Extensibility | Ability to incorporate personal materials |
| Maintainability | Effort required to update content |
| Media Integration | Frequency of necessary transitions to resources outside the integrated environment |

The results can be used to continuously improve the structure, information density, and linking strategy of the teaching materials.

---

# 17. Overall Evaluation and Conceptual Rationale

The decision to use an Obsidian-based wiki format for Open Lectures is founded on the idea that modern knowledge transfer should go beyond the linear presentation of information.

Academic understanding does not arise solely from reading individual texts. It also develops through recognizing relationships, applying concepts, and actively engaging with the subject matter.

The proposed presentation format therefore combines several elements:

**Visualizations** provide concise overviews of complex concepts.

**Explanatory texts** supply context, definitions, and technical details.

**Practical examples** demonstrate the usefulness of theoretical concepts.

**Programming examples and exercises** enable active application of knowledge.

**Historical information and trivia** supplement technical content with background and context.

**Wiki-links** enable flexible navigation between related concepts.

**The Obsidian Graph View** visualizes existing connections and can help identify thematic clusters.

**Personal extensibility** allows learners to transform the provided materials into an individual knowledge base.

Together, these elements support the overarching objective of minimizing traditional transitions between lecture notes, textbooks, presentations, laboratories, and supplementary research wherever reasonably possible.

---

# 18. Open Lectures Mission Statement

> [!abstract] **Open Lectures – Mission Statement**
>
> Open Lectures aims to provide scientific and technical educational content within an open, interconnected, and individually extensible knowledge environment.
>
> Its central focus is the combination of intuitive visualization, academically sound explanations, practical applications, and immediate access to supplementary knowledge.
>
> Content is not treated as a collection of isolated documents but as part of a structured knowledge network supporting both systematic learning and individual exploration.
>
> By using Markdown and Obsidian, the materials remain transparent, editable, accessible over the long term, and open to personal additions.
>
> **The learning environment should not merely present knowledge, but enable its understanding, application, interconnection, and individual development.**

---

# 19. Summary of Design Decisions

| Decision | Rationale | Expected Benefit |
|---|---|---|
| Obsidian as the learning environment | Wiki functionality and Markdown support | Integrated knowledge organization |
| Strong emphasis on visualization | Concise representation of complex relationships | Improved clarity |
| Supporting explanatory text | Context and technical detail | Deeper understanding |
| Practical examples | Connection between theory and application | Knowledge transfer |
| Code examples | Experimentation with technical concepts | Active learning |
| Contextual external links | Immediate access to supplementary resources | Reduced search effort |
| History and trivia | Contextualization and motivation | Interest and contextual understanding |
| Wiki-links | Nonlinear navigation | Networked learning |
| Graph View | Visualization of existing connections | Recognition of knowledge clusters |
| Personal extensibility | Individual notes and additions | Self-directed learning |
| Markdown | Open, text-based format | Portability and maintainability |
| Independent Vaults | Independence of individual courses | Modular distribution |

---

# 20. Final Design Decision

The presentation format of Open Lectures is defined as an **integrated, visually oriented, and interconnected knowledge environment based on independent Obsidian Vaults**.

The following principles apply:

1. **Visual First, Text Supported:** Graphics and diagrams communicate structures and relationships, while explanatory text provides the necessary academic depth.
2. **Theory Meets Practice:** Theoretical content is supplemented with appropriate application examples whenever possible.
3. **Learning by Doing:** Where suitable, executable code examples, simulations, and exercises enable active engagement with the subject matter.
4. **Knowledge in Context:** Supplementary resources are integrated directly into the relevant academic context.
5. **Learning Through Exploration:** Wiki-links and Graph Views support nonlinear exploration of conceptual relationships.
6. **Engagement Through Context:** Historical backgrounds and interesting supplementary information enrich the learning experience.
7. **Personal Knowledge Ownership:** Learners can extend the knowledge collection with their own materials and organize it according to their individual needs.
8. **One-Stop Learning Experience:** The learning environment should consolidate as many resources required for learning as reasonably possible and minimize unnecessary transitions between media.

**Open Lectures is intended to be more than a collection of digital lecture notes: it aims to become an open, structured, visually understandable, and individually extensible learning and knowledge environment.**