pipeline {
    agent any
    environment {
        IMAGE_NAME = "reflex-app"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/raulblend/web-portfolio.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

    }
}