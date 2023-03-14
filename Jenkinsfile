pipeline {
    agent any

    stages {
        stage('Run tests') {
            steps {
                dir('C:/ProgramData/Jenkins/.jenkins/workspace/Nisha'){ 
                    bat 'python -m unittest'
                }
            }
        }
        stage('Workspace cleaning'){
            steps {
                cleanWs()
            }
        }
    }
}
