pipeline {
    agent any
     environment {
        AUTHOR = 'Rutuja Haridas'
    }
    //triggers{ cron('H/5 * * * *') }
    stages {

        stage('Check Path and make backup folder') {
            steps {
                sh 'pwd'
                echo 'Backup'
                dir ('backup') {
                }
                sh 'ls -l'
            }
        }

        stage('Make virtual environment and install requirements') {
            steps {
                //sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }
        }

        stage('Run Fab file') {
            input {
                message "Should we continue?"
                ok "Yes, we should."
                submitter "alice,bob"
                parameters {
                    string(name: 'HOSTNAME', defaultValue: 'rutujaharidas-HP-Pavilion-Laptop-15-cc1xx', description: 'Who should I say hello to?')
                    string(name: 'PASSWORD', defaultValue: 'root@123', description: 'Enter a password')

                }
            }
            steps {

                   sh "fab pwd -H ${HOSTNAME} "
            }
        }
    }
}