pipeline {
    agent any
    stages {
        stage('Check out repo'){
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '45314cd0-021a-4eb2-bf90-b4221bedc0f7', url: 'https://github.com/NishaChaudhry01/Assignment2_tests.git']])
                }
            }
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
