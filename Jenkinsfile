pipeline {
    agent any
     environment {
        AUTHOR = 'Rutuja Haridas'
    }
    triggers{ cron('H/5 * * * *') }
    stages {
        stage('Test') {
            steps {
                sh 'pwd'
                echo 'Backup'
                dir ('backup') {
                        }

                //sh 'mkdir backup'
                sh 'ls -l'
            }
        }
        stage('Deploy') {
            steps {
                sh 'chmod +x db_backup_script.sh'
                sh './db_backup_script.sh'
                echo 'Deploying at Dev'
            }
        }
    }
}
