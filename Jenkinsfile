pipeline{
    agent any
    environment {
        DOCKER_USER="varsha072"
        IMAGE_NAME="varsha072/webapp"
        IMAGE_TAG="latest"
    }
    stages{
        stage('Checkout Code'){
            steps{
                echo "Checking out the code from the repository"
                checkout scm
            }
        }
        stage('Build Docker Image'){
            steps{
                echo "Building Docker image"
                bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('docker login'){
            steps{
                echo "Logging in to Docker Hub"
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]){
                        bat "docker login -u ${DOCKER_USER} --password-stdin"
                    }
                }
            }
        stage('Push Docker Image'){
            steps{
                echo "Pushing Docker image to Docker Hub"
                bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
                echo "Deploying to Kubernetes"
                bat "kubectl apply -f deployment.yaml validate=False"
                bat "kubectl apply -f service.yaml"
            }
        }
        stage('Verify Deployment'){
            steps{
                echo "Verifying the deployment"
                bat "kubectl get pods"
                bat "kubectl get services"
                bat "kubectl get deployments"
            }
        }
}
POST{
    success{
        echo "Pipeline completed successfully"
    }
    failue{
        echo "Pipeline failed"
    }
}