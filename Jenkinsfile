pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "codeanonymous25/bmi-app"
        DOCKER_TAG = "latest"
        DOCKER_CREDENTIALS_ID = "docker-hub-creds" // Set this in Jenkins credentials
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }

        stage('Post Build Info') {
            steps {
                echo "Docker image ${DOCKER_IMAGE}:${DOCKER_TAG} pushed successfully."
            }
        }
    }

    post {
        success {
            echo "Build and push completed successfully."
        }
        failure {
            echo "Build or push failed."
        }
    }
}