pipeline {
    agent any
     environment {
        AUTHOR = 'Rutuja Haridas'
    }
    triggers{ cron('H/5 * * * *') }
    stages {
        stage('Test') {
            steps {
                echo 'pwd'
                echo 'Backup'
                sh 'ls backup'
            }
        }
        stage('Deploy') {
            steps {
                sh 'chmod +x db_backup_script.sh'
                sh 'mkdir backup'
                sh './db_backup_script.sh'
                echo 'Deploying at Dev'
            }
        }
    }
}