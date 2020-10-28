pipeline {
    agent any
     environment {
        AUTHOR = 'Rutuja Haridas'
        def folder = new File( 'backup/' )
    }
    triggers{ cron('H/5 * * * *') }
    stages {
        stage('Test') {
            when {
            expression { folder=='true' }
                }

            steps {
                echo 'Backup folder exists'
                //sh 'mkdir backup'
                sh 'ls backup'
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