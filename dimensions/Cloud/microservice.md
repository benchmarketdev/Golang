# Introduction to Microservices

## Cloud native

Cloud native is an application architecture that uses the strengths and accommodates the challenges of a standardized cloud environment.

- Elastic scaling
- Immutable deployment
- Disposable instances
- Less predictable infrastructure

## Making developers more efficient

- Small teams
- Less time in communication
- Minimize coordination

## Using technology more efficiently

- Single responsibility principle
- Well defined interface and dependencies

## Architecture

- SOA:  
  - Focused on resue, techinical integration issues, technical APIs
  - Aligh with a centrally funded modle
  - A change to a SOA service might impact multiple consumers
- Microservices:
  - Focused on functional decomposition, business capabilities, business APIs
  - Breaking down monolithic application into smaller
  - Need good DevOps

## Key tenets

- Large monoliths are broken down into many small services
- Services are optimized for a single function
- Communication via REST API and message brokers
- Per-service CI/CD, services evolve at different rates
- Per-service HA and clustering decisions

## Comparing monolithic and microservices architectures

| Category | Monolithic Arch | Microservices Arch |
| -------- | --------------- | ------------------ |
| Architecture | Built as a single logical executable | Built as a suite of small services |
| Modularity | Based on language features | Based on business capabilities |
| Agility | Build and deploying a new version of entrie app | Apply to each service independently |
| Scaling | Entire app scaled when only one part is the bottleneck | Each service scaled independently when needed |
| Implementation | Typically in one language | Different programming language |
| Maintainablity | Large code base | Smaller code bases|
| Deployment | Complex, with maintenance downtimes | Minimal downtime |


## Downsides
- Operational complexity
- The more pieces running independently, the more the distributed system becomes an issue.

## Language decisions

- Dispatchers are often implemented in Node, good at handling large numbers of clients and lots of concurrent I/O
- For iOS, easier to write the dispather in Swift
- Business services afre often written in Java, CPU-intensive tasks, connect to external systems

## Communication between services
- Language-neutral
- JSON/REST
- For asynchronous intergration, Kafka, RabbitMQ, Message Hub(IBM Cloud), etc.

