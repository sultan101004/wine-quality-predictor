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
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                        docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                        docker push ${IMAGE_NAME}:${TAG}
                    """
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
