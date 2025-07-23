# 🔐 Secure GitOps Microservices with Vault, ArgoCD & Kubernetes 🚀

This project demonstrates a secure, scalable microservices architecture deployed using GitOps (ArgoCD), Kubernetes, and managed secrets with HashiCorp Vault. It showcases full DevOps lifecycle automation including infrastructure provisioning, container orchestration, CI/CD, secrets management, and observability.

---

## 📌 Project Features

| Area                    | Tools Used                          |
|-------------------------|-------------------------------------|
| Microservices           | Python Flask                        |
| Containerization        | Docker                              |
| Orchestration           | Kubernetes (EKS, AKS, GKE-ready)    |
| GitOps                  | ArgoCD                              |
| CI/CD Pipeline          | GitHub Actions                      |
| Infrastructure as Code  | Terraform                           |
| Secrets Management      | HashiCorp Vault                     |
| Monitoring              | Prometheus + Grafana + Loki         |

---

## 🧩 Microservices Included

- **`auth-service`** – Handles user authentication using JWT.
- **`product-service`** – Manages a basic product catalog.
- **`api-gateway`** – Acts as a reverse proxy for routing.

Each service is containerized and includes its own `Dockerfile`.

---

## 🛠️ Setup Overview

### 1. 📦 Build & Push Images

```bash
docker build -t yourrepo/auth-service ./services/auth-service
docker build -t yourrepo/product-service ./services/product-service
docker build -t yourrepo/api-gateway ./services/api-gateway
docker push yourrepo/auth-service
docker push yourrepo/product-service
docker push yourrepo/api-gateway
cd terraform/aws
terraform init
terraform apply
