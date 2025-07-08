# 🚀 Real-Time Incident Collaboration Platform

A **full-stack, real-time incident collaboration tool** built with **FastAPI, React, PostgreSQL, Redis, Clerk Authentication, and WebSockets**, enabling teams to **log, update, and track incidents collaboratively with live updates**.

## 🌟 Features

✅ User authentication via [Clerk](https://clerk.com)
✅ Real-time updates with **Redis Pub/Sub + WebSockets**
✅ Incident creation, editing, deletion with audit trail
✅ PostgreSQL database with Alembic migrations
✅ Responsive React frontend with clean UI
✅ Dockerized deployment for seamless testing
✅ Pre-built Docker images on GitHub Container Registry (GHCR)
✅ Perfect for **portfolio, hackathons, and teamwork practice**


## 🛠️ Tech Stack

* **Frontend:** React + Clerk + Axios + WebSockets
* **Backend:** FastAPI + SQLAlchemy + Alembic
* **Database:** PostgreSQL
* **Real-Time:** Redis Pub/Sub + WebSockets
* **Containerization:** Docker + Docker Compose
* **Authentication:** Clerk.dev


## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shreyaparab28/incident_collab_platform.git
cd incident_collab_platform
```

---

### 2️⃣ Run with Docker (Recommended)

Ensure you have Docker installed ([Install Guide](https://docs.docker.com/get-docker/)).

Run:

```bash
docker compose up --build
```

* Frontend: [http://localhost:3001](http://localhost:3001)
* Backend: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)

---

### 3️⃣ Using Prebuilt Docker Images

Skip build time by pulling prebuilt images:

#### Pull Backend Image:

```bash
docker pull ghcr.io/shreyaparab28/incident_collab_platform_backend:latest
```

#### Pull Frontend Image:

```bash
docker pull ghcr.io/shreyaparab28/incident_collab_platform_frontend:latest
```

Adjust your `docker-compose.yml` to reference these images and run:

```bash
docker compose up
```

---

## ✨ Using the Application

1️⃣ Sign up or sign in using Clerk on the frontend.
2️⃣ Create, update, or delete incidents.
3️⃣ **All connected users see updates in real time.**
4️⃣ "Created By" displays **username** of the creator.

---

## 🗂️ Project Structure

```
incident_collab_platform/
├── backend/
│   ├── app/
│   ├── alembic/
│   ├── Dockerfile
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
└── docker-compose.yml
```

---

## ⚙️ Development Mode

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🛡️ Security Notes

✅ Clerk securely manages authentication and tokens.
✅ Backend enforces JWT validation and CORS policies.
✅ Environment variables should be secured in `.env` files for production deployments.

---


## 🙏 Acknowledgements

* [FastAPI](https://fastapi.tiangolo.com/)
* [React](https://reactjs.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Redis](https://redis.io/)
* [Clerk.dev](https://clerk.com/)
* [Docker](https://docker.com/)

---


✅ A **GitHub Actions CI/CD workflow** to build and push your images automatically to GHCR on every push to `main`.
✅ A **clean `docker-compose.yml` for end users** to test with your GHCR images easily.

Let me know whenever you are ready for the next polishing steps for your **portfolio deployment**.
