pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:/Users/charu/AppData/Local/Programs/Python/Python311/python.exe'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/MSKeerti/ASE-JenkinsDemo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat "${env.PYTHON_PATH} -m venv venv"
                bat ".\\venv\\Scripts\\pip install --upgrade pip"
                bat ".\\venv\\Scripts\\pip install -r requirements.txt || exit 0"
            }
        }

        stage('Run Tests') {
            steps {
                bat ".\\venv\\Scripts\\python -m unittest discover -s tests"
            }
        }

        stage('Deploy') {
            when {
                expression {
                    currentBuild.currentResult == 'SUCCESS'
                }
            }
            steps {
                echo 'Deploying application...'
                // Add your deployment script here, e.g., copying files to a server
            }
        }
    }

    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed. Please check errors.'
        }
    }
}
