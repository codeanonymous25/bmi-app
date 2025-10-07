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
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                    '''
                }
            }
        }

        stage('Post Build Info') {
            steps {
                echo "Docker image $DOCKER_IMAGE:$DOCKER_TAG pushed successfully."
            }
        }
    }

    post {
        success {
            echo "✅ Build and push completed successfully."
        }
        failure {
            echo "❌ Build or push failed."
        }
    }
}