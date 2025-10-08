node {
    stage("Cloning") {
checkout scm    
}

    stage("Building") {
        sh '''
        docker build -t bmi-app:01 .
        '''
    }

    stage("Deployment") {
        sh '''
	helm uninstall bmi-app-release || echo "Release not found, skipping uninstall"
        helm install bmi-app-release bmi-app
        '''
    }

    stage("Pods") {
        sh '''
        kubectl get pods
        sleep 10
        '''
    }

    stage("Testing") {
        script {
            def podStatus = sh(script: "kubectl get pods | grep bmi-app | grep Running", returnStatus: true)
            if (podStatus == 0) {
                currentBuild.result = "SUCCESS"
            } else {
                currentBuild.result = "FAILURE"
            }
        }
    }

    stage("Approval") {
        script {
            if (env.CHANGE_ID && (currentBuild.result == "SUCCESS" || currentBuild.result == null)) {
                input message: "Everything correct, do you want to merge?", ok: "Merge"
            }
        }
    }

    stage("Done") {
        script {
            if (currentBuild.result == "SUCCESS" || currentBuild.result == null) {
		

               
                sh '''
                echo "Everything is working correct!"
                '''
            } else {
                echo "Build failed — skipping downstream job."
            }
        }
    }
}
