# Load-Balanced URL Shortener using Docker & Kubernetes

- This project is a scalable, containerized URL Shortener built with Flask, Redis, Docker, and deployed on Kubernetes.
- It accepts long URLs, generates short links, and redirects users appropriately.
- The application supports load balancing, horizontal pod autoscaling, and basic stress testing.
- This was done as a Mini project for the course *Cloud Computing (UE22CS351B)*

## Features

- **Shorten URLs**  
  Users can submit long URLs via a simple web interface and receive a shortened link.

- **In-Memory Storage with Redis**  
  All URL mappings are stored in a Redis key-value store for fast access.

- **Dockerized**  
  The app is containerized using Docker for portability and consistency across environments.

- **Kubernetes Deployment**  
  - Deployed using Kubernetes Deployment and Service manifests.  
  - Uses a ClusterIP service for internal Redis communication.  
  - Exposed externally using a NodePort service.

- **Load Balancing**  
  Multiple replicas of the URL shortener app are deployed and traffic is balanced via Kubernetes services.

- **Horizontal Pod Autoscaling (HPA)**  
  Automatically scales app pods based on CPU usage.

- **Logging**  
  Application logs are accessible using `kubectl logs` for real-time debugging and monitoring.

- **Stress Tested**  
  Apache Benchmark (`ab`) was used to simulate concurrent requests and test app scalability.

## Tech Stack

- **Backend**: Python (Flask)
- **Storage**: Redis
- **Containerization**: Docker
- **Orchestration**: Kubernetes (kubectl)
- **Monitoring**: kubectl logs + manual stress testing
