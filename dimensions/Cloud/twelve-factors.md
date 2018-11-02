# The Twelve-Factors

## An outline of the twelve-factors

- Codebase:  Once codebase that is tracked in revision control, with many deployments
- Dependencies:  Explicitly declare and isolate dependencies
- Configuration:  Store configuration in the environment
- Backing services:  Treat backing services as attached resources
- Build, release, run:  Strictly seperate build and run stages
- Processes:  Execute the app as one or more stateless processes
- Port binding:  Export services with port binding
- Concurrency:  Scale out using the process model
- Disposability:  Maximize robustness with fast startup and efficient shutdown
- Development and production parity:  Keep develoment, staging, and production as similar as possible
- Logs:  Treat logs as event streams
- Admin processes:  Run administrative and management tasks as one-off processes

## Codebase

Each microservice should have its own project with its own main branch and membership.

## Dependencies

- Nodejs:  NPM
- Liberty:  Feature Manager
- Ruby:  Bundler
- Java EE: Application Resources

Never rely on system-wide dependencies

## Configuration

- ANYTHING that is likely to vary between deploys, dev, test, stage, prod
- DO NOT to store in the code, properties files, build, AppServer

## Processes

- Runtime should be stateless, but the services can have state.
- Service state:  data passed into the stateless service
- Session state:  data for history of a user session
- Domain state:  data availabel to multiple or all services

## Concurrency

- Vertical scaling:  One runtime runs more instances, all of the resources(CPU, memory, network) have to belong to a single server.
- Horizontal scaling:  Run more runtimes, resources can be distributed across multiple servers.

## Disposability

- Containers built on this principle

## Logs

- Each process writes to stdout
- Environment decides how to gather, aggregate, and persist stdout output
- ELK stack


