---
author: Andreas Hümmer
title: GraphQL
tags:
  - content
  - vs
  - kommunikation
  - graphql
  - api
  - facebook
created: '2026-10-29'
modified: '2026-10-24'
bereich: VS
---

# GraphQL

> [!info] Lernziele
> - GraphQL als Query-Sprache für APIs verstehen
> - Unterschiede zu REST erklären können
> - Schema-Definition und Typsystem kennen
> - Vor- und Nachteile von GraphQL benennen

---

## Einleitung

GraphQL ist eine Query-Sprache für APIs, die 2012 von Facebook entwickelt und 2015 als Open Source veröffentlicht wurde. Der Name steht für "Graph Query Language" und reflektiert die Idee, dass Daten als Graph miteinander verbundener Objekte betrachtet werden.

Anders als REST, wo der Server die Datenstruktur vorgibt, bestimmt bei GraphQL der **Client**, welche Daten er benötigt. Facebook entwickelte GraphQL ursprünglich, um die mobile News-Feed-App zu optimieren – auf langsamen Mobilfunkverbindungen machte jedes überflüssige Byte einen Unterschied.

> [!important] Kernkonzept
> GraphQL löst zwei fundamentale Probleme von REST-APIs: **Overfetching** (zu viele Daten werden übertragen) und **Underfetching** (zu wenige Daten, mehrere Requests nötig). Der Client formuliert eine präzise Abfrage und bekommt exakt diese Daten zurück – nicht mehr, nicht weniger.

> [!example] Analogie
> REST ist wie ein Restaurant mit festen Menüs: Du bestellst "Menü 3" und bekommst Vorspeise, Hauptgang und Dessert – auch wenn du nur den Hauptgang wolltest. GraphQL ist wie ein Buffet mit Bestellkarte: Du schreibst genau auf, was du möchtest, und bekommst exakt das serviert.

### Historischer Kontext

| Jahr | Ereignis |
|------|----------|
| 2012 | Facebook beginnt interne Entwicklung für mobile Apps |
| 2015 | Open-Source-Veröffentlichung auf GitHub |
| 2018 | GraphQL Foundation gegründet (unter Linux Foundation) |
| 2021 | Spezifikation erreicht stabilen Status |
| Heute | Genutzt von GitHub, Shopify, Twitter, Airbnb, PayPal u.v.m. |

GraphQL ist kein Protokoll, sondern eine **Spezifikation**. Es definiert eine Abfragesprache und ein Typsystem, sagt aber nichts über Transport oder Serialisierung. In der Praxis wird es meist über HTTP mit JSON transportiert.

---

## Das Problem mit REST

### Overfetching

```
GET /users/123

Response:
{
  "id": 123,
  "name": "Max Mustermann",
  "email": "max@example.com",
  "address": { ... },      // Nicht benötigt
  "phone": "...",          // Nicht benötigt
  "preferences": { ... },  // Nicht benötigt
  "created_at": "...",     // Nicht benötigt
  "updated_at": "..."      // Nicht benötigt
}
```

Der Client braucht nur `name` und `email`, bekommt aber alles.

### Underfetching

```
GET /users/123           → Benutzer-Daten
GET /users/123/posts     → Posts des Benutzers
GET /posts/456/comments  → Kommentare zum Post
GET /users/789           → Autor eines Kommentars
```

Vier Requests für eine Ansicht – das N+1-Problem.

### GraphQL-Lösung

```graphql
query {
  user(id: 123) {
    name
    email
    posts {
      title
      comments {
        text
        author {
          name
        }
      }
    }
  }
}
```

**Ein Request**, exakt die benötigten Daten.

---

## Schema und Typsystem

GraphQL basiert auf einem streng typisierten Schema. Das Schema ist der **zentrale Vertrag** zwischen Client und Server – es definiert, welche Daten abgefragt werden können und in welcher Struktur sie zurückkommen.

### Warum ein Schema?

Das Schema erfüllt mehrere wichtige Funktionen:

1. **Dokumentation**: Das Schema ist selbstdokumentierend – Tools wie GraphiQL können es auslesen und eine interaktive API-Dokumentation generieren
2. **Validierung**: Queries werden gegen das Schema validiert, bevor sie ausgeführt werden
3. **Code-Generierung**: Aus dem Schema können typsichere Clients generiert werden
4. **Versionierung**: Durch Schema-Evolution (Deprecation statt Breaking Changes) sind API-Versionen unnötig

### Schema Definition Language (SDL)

```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String
  author: User!
  comments: [Comment!]!
  createdAt: DateTime!
}

type Comment {
  id: ID!
  text: String!
  author: User!
}

type Query {
  user(id: ID!): User
  users: [User!]!
  post(id: ID!): Post
}

type Mutation {
  createPost(title: String!, content: String): Post!
  deletePost(id: ID!): Boolean!
}

type Subscription {
  postCreated: Post!
}
```

### Typmodifikatoren

| Syntax | Bedeutung |
|--------|-----------|
| `String` | Nullable String |
| `String!` | Non-null String (required) |
| `[String]` | Nullable Liste von nullable Strings |
| `[String!]!` | Non-null Liste von non-null Strings |

---

## Operationstypen

GraphQL definiert drei Operationstypen, die unterschiedliche Arten der Interaktion mit dem Server ermöglichen:

### 1. Query (Lesen)

Queries sind **idempotent** und haben keine Seiteneffekte – sie lesen nur Daten. Der Server kann Queries parallel ausführen.

```graphql
query GetUser {
  user(id: "123") {
    name
    email
  }
}
```

Queries können auch **Argumente**, **Aliase** und **Fragmente** verwenden:

```graphql
query GetTwoUsers {
  admin: user(id: "1") {
    ...UserFields
  }
  guest: user(id: "2") {
    ...UserFields
  }
}

fragment UserFields on User {
  name
  email
  role
}
```

### 2. Mutation (Schreiben)

Mutations verändern Daten auf dem Server. Sie werden **sequentiell** ausgeführt, um Race Conditions zu vermeiden.

```graphql
mutation CreatePost {
  createPost(title: "Hallo Welt", content: "Mein erster Post") {
    id
    title
    createdAt
  }
}
```

> [!note] Konvention
> Mutations geben typischerweise das veränderte Objekt zurück, damit der Client seinen lokalen Cache aktualisieren kann, ohne einen weiteren Request zu machen.

### 3. Subscription (Echtzeit)

Subscriptions ermöglichen Echtzeit-Updates vom Server zum Client. Nach dem initialen Request hält der Server die Verbindung offen und sendet Updates, wenn sich relevante Daten ändern.

```graphql
subscription OnPostCreated {
  postCreated {
    id
    title
    author {
      name
    }
  }
}
```

Subscriptions nutzen WebSockets für die persistente Verbindung und sind ideal für:
- Chat-Anwendungen
- Live-Dashboards
- Collaborative Editing
- Benachrichtigungen

---

## GraphQL vs. REST

| Aspekt | GraphQL | REST |
|--------|---------|------|
| **Endpunkte** | Einer (`/graphql`) | Viele (`/users`, `/posts`, ...) |
| **Datenstruktur** | Client bestimmt | Server bestimmt |
| **Overfetching** | Gelöst | Problem |
| **Underfetching** | Gelöst | Problem |
| **Versionierung** | Nicht nötig (Schema-Evolution) | URL-/Header-Versionierung |
| **Caching** | Komplexer (POST-Requests) | Einfach (HTTP-Caching) |
| **Lernkurve** | Steiler | Flacher |
| **Tooling** | GraphiQL, Apollo DevTools | Swagger, Postman |

### Wann REST, wann GraphQL?

**REST bevorzugen bei:**
- Einfachen CRUD-APIs mit stabilen Datenstrukturen
- Starkem Bedarf an HTTP-Caching (CDN, Browser-Cache)
- Teams ohne GraphQL-Erfahrung
- Öffentlichen APIs mit vielen verschiedenen Konsumenten

**GraphQL bevorzugen bei:**
- Komplexen, verschachtelten Datenstrukturen
- Mobilen Apps mit Bandbreitenbeschränkungen
- Rapidly evolving Frontends mit wechselnden Datenanforderungen
- Microservices, die über eine einheitliche API-Schicht aggregiert werden

---

## Resolver

Resolver sind die Funktionen, die die Daten für ein GraphQL-Feld beschaffen. Jedes Feld im Schema kann einen eigenen Resolver haben.

### Resolver-Kette

Wenn ein Client diese Query sendet:

```graphql
query {
  user(id: "123") {
    name
    posts {
      title
    }
  }
}
```

Werden die Resolver in dieser Reihenfolge aufgerufen:

1. `Query.user(id: "123")` → Lädt User aus DB
2. `User.name` → Gibt `user.name` zurück (Default-Resolver)
3. `User.posts` → Lädt Posts des Users
4. `Post.title` → Gibt `post.title` zurück (Default-Resolver)

### Beispiel-Implementierung (JavaScript)

```javascript
const resolvers = {
  Query: {
    user: (parent, { id }, context) => {
      return context.db.users.findById(id);
    }
  },
  User: {
    posts: (user, args, context) => {
      return context.db.posts.findByAuthor(user.id);
    }
  }
};
```

Die drei Resolver-Argumente:
- **parent**: Das Ergebnis des übergeordneten Resolvers
- **args**: Die übergebenen Argumente (z.B. `id`)
- **context**: Geteilter Kontext (DB-Verbindung, Auth-Info)

---

## Vor- und Nachteile

### Vorteile

- **Flexibilität**: Client bestimmt die Datenstruktur
- **Effizienz**: Keine Over-/Underfetching-Probleme
- **Typsicherheit**: Schema als Vertrag zwischen Client und Server
- **Introspection**: API ist selbstdokumentierend
- **Versionierung**: Schema-Evolution statt API-Versionen
- **Developer Experience**: GraphiQL, Code-Generierung

### Nachteile

- **Komplexität**: Mehr Setup als REST
- **Caching**: HTTP-Caching funktioniert nicht direkt
- **Performance**: Komplexe Queries können teuer sein (N+1 auf Server-Seite)
- **File Upload**: Nicht nativ unterstützt
- **Rate Limiting**: Schwieriger (ein Endpunkt, variable Komplexität)

---

## Sicherheit und Performance

### Introspection

GraphQL bietet eine eingebaute **Introspection**-Funktion: Clients können das Schema selbst abfragen. Das ermöglicht Tools wie GraphiQL, die API automatisch zu dokumentieren.

```graphql
query IntrospectionQuery {
  __schema {
    types {
      name
      fields {
        name
        type { name }
      }
    }
  }
}
```

> [!warning] Sicherheitshinweis
> In Produktionsumgebungen sollte Introspection deaktiviert werden, da Angreifer damit die gesamte API-Struktur auslesen können.

### Query Complexity Analysis

Schutz vor teuren Queries:

```graphql
# Diese Query könnte exponentiell viele Daten laden
query DangerousQuery {
  users {           # 100 User
    posts {         # je 50 Posts = 5.000
      comments {    # je 20 Comments = 100.000
        author {
          posts {   # wieder 50 Posts = 5.000.000
            ...
          }
        }
      }
    }
  }
}
```

**Gegenmaßnahmen:**
- Query Depth Limiting
- Query Complexity Scoring
- Rate Limiting per Query-Komplexität
- Persisted Queries (nur vordefinierte Queries erlauben)

### DataLoader Pattern

Lösung für das N+1-Problem auf Server-Seite:

```javascript
// Ohne DataLoader: 100 einzelne DB-Queries
// Mit DataLoader: 1 Batch-Query für alle 100 User
const userLoader = new DataLoader(ids => 
  User.findByIds(ids)
);
```

### Caching-Strategien

Da GraphQL typischerweise POST-Requests verwendet, funktioniert HTTP-Caching nicht direkt. Alternativen:

| Strategie | Beschreibung | Anwendung |
|-----------|--------------|-----------|
| **Persisted Queries** | Queries werden vorab registriert und per Hash aufgerufen (GET möglich) | Produktion mit bekannten Clients |
| **Automatic Persisted Queries (APQ)** | Client sendet Hash, Server fragt Query nur bei Cache-Miss an | Apollo-Ökosystem |
| **Response Caching** | Ganze Responses werden gecacht (z.B. Redis) | Häufig gleiche Queries |
| **Field-Level Caching** | Einzelne Felder mit TTL cachen | Teure Berechnungen |
| **Normalized Client Cache** | Client cached Objekte nach ID (Apollo Client) | SPA mit häufigen Updates |

---

## Praktische Implementierungen

| Stack | Server | Client |
|-------|--------|--------|
| **JavaScript** | Apollo Server, Express-GraphQL | Apollo Client, Relay |
| **Python** | Graphene, Strawberry | gql |
| **Java** | GraphQL Java, DGS | Apollo Android |
| **Go** | gqlgen, graphql-go | - |
| **.NET** | Hot Chocolate, GraphQL.NET | - |

### Tools

- **GraphiQL**: Interaktive IDE im Browser
- **Apollo Studio**: Monitoring und Schema-Management
- **Postman**: GraphQL-Unterstützung seit 2019
- **Insomnia**: REST + GraphQL Client

---

## Zusammenhänge

- [[03-REST]] → GraphQL als Alternative für flexible Abfragen
- [[06-gRPC]] → gRPC für Performance, GraphQL für Flexibilität
- [[08-WebSockets]] → Subscriptions nutzen WebSockets
- [[05-SOA]] → GraphQL als moderne API-Schicht für Services

---

## Prüfungstipps

> [!warning] **Prüfungsrelevant**
NA

> [!question] **Typische Prüfungsfragen**
> 1. Vergleichen Sie GraphQL und REST.
> 2. Was ist das Schema in GraphQL und warum ist es wichtig?
> 3. Welche Sicherheitsrisiken gibt es bei GraphQL?

> [!tip] Merkhilfe
> **GraphQL = Fragen, was du brauchst**
> - **Q**uery: Lesen
> - **M**utation: Schreiben
> - **S**ubscription: Echtzeit
> - Ein Endpunkt, flexible Abfragen

---

## Quellen

- GraphQL Foundation. GraphQL Specification: https://spec.graphql.org/
- Facebook (2015). GraphQL: A data query language. Engineering Blog.
- Buna, S. (2021). *GraphQL in Action*. Manning Publications.
- Apollo GraphQL Documentation: https://www.apollographql.com/docs/
- How Facebook Invented GraphQL: https://engineering.fb.com/
