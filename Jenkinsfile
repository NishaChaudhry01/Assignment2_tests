pipeline {
    agent any
    stages {
        stage('Check out repo'){
            steps {
                checkout scmGit(branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/NishaChaudhry01/Assignment2_tests.git']])
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