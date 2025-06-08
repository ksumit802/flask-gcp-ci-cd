# 🚀 CI/CD Pipeline for Dockerized Flask App on GCP

This project demonstrates a fully automated CI/CD pipeline that deploys a Dockerized Flask web application to **Google Cloud Run** using **GitHub Actions**.

---

## 📦 Tech Stack
- **Flask** (Python web framework)
- **Docker** (Containerization)
- **GitHub Actions** (CI/CD automation)
- **Google Cloud Run** (Serverless deployment)
- **Artifact Registry** (Container image storage)

---

## 🌐 Live Demo
Once deployed, access the app via your **Cloud Run URL**:
```
https://flask-app-521747051469.us-central1.run.app/
```

---

## 📁 Project Structure
```
├── app.py                  # Flask app
├── Dockerfile              # Docker instructions
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Actions workflow
```

---

## 🛠️ Local Setup
### 1. Clone the Repo
```bash
git clone https://github.com/ksumit802/flask-gcp-ci-cd
cd flask-gcp-ci-cd
```

### 2. Build and Run Docker Locally
```bash
docker build -t flask-gcp-app .
docker run -p 8080:8080 flask-gcp-app
```
Visit `http://localhost:8080`

---

## 🚀 CI/CD Workflow (deploy.yml)
This GitHub Actions pipeline:
1. Authenticates to GCP using a service account
2. Builds the Docker image
3. Pushes it to Artifact Registry
4. Deploys to Cloud Run automatically

### 📂 Secrets Required in GitHub
- `GCP_PROJECT_ID` → Your Google Cloud project ID
- `GCP_SA_KEY` → Contents of your service account JSON key

---

## ✅ Google Cloud Setup Summary
- Enabled APIs: Cloud Run, Artifact Registry, Cloud Build
- Created `flask-images` Docker repo in Artifact Registry
- Deployed via GitHub Actions to `us-central1`

---

## 📃 License
This project is open-source and for educational/demo purposes.

---

## 🙌 Credits
Built with ❤️ using GCP, Docker, and GitHub Actions by Sumit Kumar.
