pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git pull || true'
            }
        }
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip setuptools wheel'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest --junitxml=pytest-results.xml'
            }
            post {
                always {
                    junit 'pytest-results.xml'
                }
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }
        stage('OWASP Dependency-Check') {
            steps {
                    dependencyCheck odcInstallation: 'Default-DC', additionalArguments: '--scan . --format XML'
            }
            post {
                always {
                    dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
            }
        }
        // stage('Python Security Scan') {
        //     steps {
        //         sh '. venv/bin/activate && pip install bandit safety pip-audit detect-secrets'
        //         sh '. venv/bin/activate && bandit -r .'
        //         sh '. venv/bin/activate && safety check -r requirements.txt'
        //         sh '. venv/bin/activate && pip-audit'
        //         sh '. venv/bin/activate && detect-secrets scan > detect-secrets-report.json'
        //     }
        // }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t drf-todo-app:latest .'
            }
        }
        stage('Deploy Docker Container') {
            steps {
                sh 'docker rm -f drf-todo-app || true'
                sh 'docker run -d --name drf-todo-app -p 8000:8000 drf-todo-app:latest'
            }
        }
    }
} 