pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')
        IMAGE_NAME = "sultan101004"
        TAG = "latest"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'docker-hub-credentials') {
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline Succeeded! Image pushed to Docker Hub.'
            // mail to: 'admin@example.com', subject: 'Build Success', body: 'Jenkins build succeeded!'
        }
        failure {
            echo 'Pipeline Failed!'
            // mail to: 'admin@example.com', subject: 'Build Failed', body: 'Jenkins build failed!'
        }
    }
}