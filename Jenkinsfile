pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/Scripts/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/Scripts/activate && pytest --junitxml=pytest-results.xml'
            }
            post {
                always {
                    junit 'pytest-results.xml'
                }
            }
        }
    }
} 