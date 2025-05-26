# Minimal Django DRF ToDo API with Jenkins CI/CD

## Features

- Django REST Framework ToDo API (CRUD)
- Unit tests with Django test client
- Jenkins CI/CD (local, via Docker)
- GitHub integration

---

## 1. GitHub Integration

### 1.1. Create a New GitHub Repo

1. Go to [GitHub](https://github.com/) and create a new repository (e.g., `drf-todo-jenkins`).
2. **Do not** initialize with a README or .gitignore (already present locally).

### 1.2. Push Local Code to GitHub

```sh
git remote add origin https://github.com/<your-username>/<your-repo>.git
git branch -M main
git push -u origin main
```

---

## 2. Jenkins Local Setup

### 2.1. Start Jenkins with Docker

```sh
docker-compose up --build
```

- Jenkins dashboard: [http://localhost:8080](http://localhost:8080)
- First startup may take a few minutes.

### 2.2. Jenkins Plugins

- Pre-installed: **GitHub** and **JUnit** plugins

---

## 3. Jenkins CI/CD Pipeline

### 3.1. Create a New Pipeline Job

1. In Jenkins, click **New Item** > **Pipeline**.
2. Set the GitHub repo URL as the source.
3. Jenkins will use the provided `Jenkinsfile` for CI/CD.

### 3.2. What the Pipeline Does

- Checks out code
- Sets up Python venv
- Installs dependencies
- Runs tests
- Publishes test results (JUnit)

---

## 4. GitHub Webhook (Trigger Jenkins on Push)

1. In your GitHub repo, go to **Settings > Webhooks > Add webhook**
2. Payload URL: `http://localhost:8080/github-webhook/`
3. Content type: `application/json`
4. Select: **Just the push event**
5. Save

---

## 5. Local Django Usage

### 5.1. Run Locally

```sh
python -m venv venv
source venv/Scripts/activate  # On Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- API: [http://localhost:8000/api/todos/](http://localhost:8000/api/todos/)
- Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### 5.2. Run Tests

```sh
python manage.py test
```
