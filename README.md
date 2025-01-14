# Distributed Chat System

## Project Overview

The **Distributed Chat System** is a real-time messaging application designed to ensure **high availability**, **reliability**, and **scalability**. The system is built to distribute messages across multiple servers, ensure that messages are persisted and replicated, and automatically handle server failures without data loss.

### **Key Features**:
- **Message Distribution**: Messages are forwarded to RabbitMQ queues and processed by multiple services across different servers.
- **Data Persistence**: Messages are stored persistently in MongoDB, ensuring that data is never lost.
- **Replication & Synchronization**: MongoDB ensures data is replicated across multiple instances, guaranteeing high availability and fault tolerance.
- **Fault Tolerance**: Kubernetes handles automatic pod recovery and failover in case of server crashes.
- **Scalability**: The system can scale horizontally, automatically adjusting the number of pods in Kubernetes based on resource usage.
- **User Authentication**: JWT authentication ensures secure user access and role-based authorization.

---

## Architecture

This system consists of several core components:
1. **Message Service**: Responsible for publishing messages to RabbitMQ and saving them in MongoDB.
2. **User Service**: Manages user authentication and consumes messages from RabbitMQ.
3. **Database Service**: MongoDB for persistent storage and data replication.
4. **RabbitMQ**: Message queue service for distributing messages between different services.
5. **Prometheus & Grafana**: For monitoring the health and performance of the system in real-time.
6. **Kubernetes**: For orchestrating the services, ensuring high availability, and scaling the system based on demand.
7. **CI/CD Pipeline**: GitHub Actions is used to automate the build, test, and deployment process.

---

## Technologies Used
- **RabbitMQ**: Message broker for handling communication between services.
- **MongoDB**: NoSQL database used for persistent message storage.
- **Docker**: Containerization of services for consistent environments.
- **Kubernetes**: Container orchestration platform for scaling and managing services.
- **Prometheus**: For monitoring the system's performance.
- **Grafana**: For visualizing metrics from Prometheus.
- **GitHub Actions**: For CI/CD automation to ensure smooth integration and deployment.

---

## Prerequisites

Before running the project, make sure you have the following installed:
- **Docker**: To build and run the containers.
- **Kubernetes**: For container orchestration and scaling.
- **Python 3.8+**: Required for the backend services.
- **MongoDB**: Used for data persistence.
- **RabbitMQ**: Used for message queuing.
- **kubectl**: For interacting with the Kubernetes cluster.

---

## Setup Instructions

### 1. **Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/iammudassirali/distributed-chat-system.git
cd distributed-chat-system
