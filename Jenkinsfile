pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/your-org/etl-pipeline-demo.git'
        REPO_DIR = 'repo'
        IMAGE_NAME = 'etl-pipeline'
        OUTPUT_DIR = 'output'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                bat '''
                    if exist %REPO_DIR% rmdir /s /q %REPO_DIR%
                    if exist %OUTPUT_DIR% rmdir /s /q %OUTPUT_DIR%
                    mkdir %REPO_DIR%
                    mkdir %OUTPUT_DIR%
                '''
            }
        }

        stage('Clone Source Code') {
            steps {
                bat 'git clone %REPO_URL% %REPO_DIR%'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    cd %REPO_DIR%
                    docker build -t %IMAGE_NAME% .
                '''
            }
        }

        stage('Run ETL & Test in Docker') {
            steps {
                bat '''
                    for /f %%i in ('cd') do set ABS_PATH=%%i
                    docker run --rm -v %CD%\%OUTPUT_DIR%:/app/output %IMAGE_NAME%
                '''
            }
        }

        stage('Show Results') {
            steps {
                bat '''
                    type %OUTPUT_DIR%\cleaned_products.csv || echo No CSV found
                    type %OUTPUT_DIR%\test_result.txt || echo No Test Result Found
                '''
            }
        }
    }
}
