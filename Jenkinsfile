pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://singhanat:ghp_ABCD1234TOKEN@github.com/singhanat/etl-pipelie/'
            }
        }
    
        stage('Build Docker Image') {
            steps {
                bat '''
                    docker build -t etl-pipeline .
                '''
            }
        }
        
        stage('Run ETL & Test in Docker') {
            steps {
                bat '''
                    docker run --rm -v %CD%:/app/output etl-pipeline
                '''
            }
        }
    }
        
}
