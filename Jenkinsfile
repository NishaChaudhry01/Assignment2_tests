pipeline {
    agent any

    stages {
        stage('Run tests') {
            steps {
                dir('C:/Users/nisha/.jenkins/workspace/Tests'){ 
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
