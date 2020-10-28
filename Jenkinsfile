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
                sh '''
                   def folder = new File( '/var/lib/jenkins/workspace/Cron_Job/backup' )

                    if( !folder.exists() ) {
                      backup.mkdir()
                    }

                '''
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