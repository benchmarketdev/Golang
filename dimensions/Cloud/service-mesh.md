# Service mesh

A services mesh can help you solve the issues and challenges that arise when implementing a microservices application.

## The challenges with microservices

- How can I find the service I need? What if it moves or fails
- How can I scale my services? Can I control how I spread the load?
- How can I test new version of services? Without impacting existing users?
- How can I test against failures?

## Common functions of a service mesh

- Service registry
  - Simple key value pair data store
  - maintaning a current list of working service instances and their locations
  - Heartbeat mechanism to keep its list current
- Service discovery
  - Client side discovery, client service is responible for making the decision to contact the service instance
  - Server side discovery, service proxy/load balancer, such as lstio
- Failure testing
  - Netflix Chaos Monkey, a testing tool
  - Simian Army, a latency monkey, a janitor monkey...
- Circuit breaker
  - Prevent response delays from a given service dependency
- Bulkhead
  - Using separate connection pools for each dependent service.

# lstio

Istio is an open platform service mesh implementation for connecting, managing, and securing microservices.

- An easy way to create a network of deployed services with load balancing
- service-to-service authentication, monitoring

## lstio capabilities

- Intelligent routing and loading balancing
- Resilience across languages and platforms
- Fleet wide policy enforcement
- In-depth telemetry and reporting

