pipeline {
    agent any
    stages {
        stage('Check Path') {
            steps {
                echo 'Check Path..'
                sh 'pwd'
            }
        }

        stage('Create virtual environment') {
            steps {
                echo 'Create virtual environment..'
                sh 'python3 -m venv venv'
            }
        }
        stage('Activate virtual environment') {
            steps {
                echo 'Activate virtual environment..'
                sh '. venv/bin/activate'
            }
        }
        stage('Install Flask') {
            steps {
                echo 'Install Flask..'
                sh 'pip install Flask'
            }
        }
        

    }

}
