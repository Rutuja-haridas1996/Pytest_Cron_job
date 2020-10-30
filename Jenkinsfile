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
                sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Fab file') {
            input {
                message "Should we continue?"
                ok "Yes, we should."
                submitter "alice,bob"
                parameters {
                    string(name: 'HOSTNAME', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
                    password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')

                }
            }
            steps {
                   echo "Hello, ${HOSTNAME}, nice to meet you."
            }
        }
    }
}
