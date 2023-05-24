pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest discover -s tests -p "*_test.py"'
            }
        }
        
        stage('Containerize') {
            steps {
                sh 'docker build -t myapp .'
                sh 'docker run myapp'
            }
        }
    }
