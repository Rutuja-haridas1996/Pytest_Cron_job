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
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                //sh 'pip3 install -r requirements.txt'

            }
        }

        stage('Run Fab file') {
//             input {
//                 message "Should we continue?"
//                 ok "Yes, we should."
//                 submitter "alice,bob"
//                 parameters {
//                     string(name: 'HOSTNAME', defaultValue: 'host', description: 'Enter the hostname')
//                     password(name: 'PASSWORD', defaultValue: 'pass', description: 'Enter a password')
//
//                 }
//             }
            steps {
                   //sh 'pip install fabric'
                   sh "fab connect"
                   //sh "fab pwd"
            }
        }
    }
}