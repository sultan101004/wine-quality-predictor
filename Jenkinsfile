pipeline {
    agent any
    environment {
        IMAGE_NAME = "sultan101004/wine-quality-predictor"
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
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline Succeeded! Image pushed to Docker Hub.'
        }
        failure {
            echo 'Pipeline Failed!'
        }
    }
}
