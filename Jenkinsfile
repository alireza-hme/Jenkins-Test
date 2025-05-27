pipeline {
    agent {
        node {
            label 'docker-agent-alpine'
        }
    }
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
        stage('OWASP Dependency-Check') {
            steps {
                    dependencyCheck odcInstallation: 'OWASP Dependency-Check Vulnerabilities', additionalArguments: '--scan . --format XML --prettyPrint --log dependency-check-run.log'
            }
            post {
                always {
                    dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
            }
        }
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