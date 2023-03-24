pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                dir('C:/Users/nisha/.jenkins/workspace/Nisha'){ 
                    bat 'python -m unittest'
                }
            }
        }
        stage('Clean Workspace'){
            steps {
                cleanWs()
            }
        }
    }
}