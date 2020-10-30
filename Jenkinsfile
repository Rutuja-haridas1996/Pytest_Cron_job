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
                   echo "Hello, ${HOSTNAME}, nice to meet you. ${PASSWORD}"
                   echo "fab pwd -H ${HOSTNAME} --password=${PASSWORD}"
                   sh "fab pwd -H ${HOSTNAME} --password=${PASSWORD}"
            }
        }
    }
}




// pipeline {
//     agent any
//     stages {
//         stage('Check Path') {
//             steps {
//                 echo 'Check Path..'
//                 sh 'pwd'
//             }
//         }
//         stage('Create virtual environment') {
//             steps {
//                 echo 'Create virtual environment..'
//                 sh 'python3 -m venv venv'
//             }
//         }
//         stage('Activate virtual environment') {
//             steps {
//                 echo 'Activate virtual environment..'
//                 sh '. venv/bin/activate'
//             }
//         }
//         stage('Install Flask') {
//             steps {
//                 echo 'Install Flask..'
//                 sh 'pip install Flask'
//             }
//         }
//         stage('Run Test file 1') {
//             steps {
//                 echo 'Run Test App file..'
//                 sh 'python test.py'
//             }
//         }
//         stage('Run Pytest file ') {
//             steps {
//                 echo 'Run Pytest file..'
//                 //sh 'pytest -v --tb=no'
//                 sh 'pytest -v --tb=no || [[ $? -eq 1 ]]'
//             }
//         }
//
//     }
// }

















// pipeline {
//     agent any
//      environment {
//         AUTHOR = 'Rutuja Haridas'
//     }
//     //triggers{ cron('H/5 * * * *') }
//     stages {
//
//         stage('Check Path and make backup folder') {
//             steps {
//                 sh 'pwd'
//                 echo 'Backup'
//                 dir ('backup') {
//                 }
//                 sh 'ls -l'
//             }
//         }
//
//         stage('Make virtual environment and install requirements') {
//             steps {
//                 sh 'virtualenv venv && . venv/bin/activate && pip3 install -r requirements.txt'
//
//             }
//         }
//
//         stage('Run Fab file') {
//             input {
//                 message "Should we continue?"
//                 ok "Yes, we should."
//                 submitter "alice,bob"
//                 parameters {
//                     string(name: 'HOSTNAME', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
//                     password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
//
//                 }
//             }
//             steps {
//                    echo "Hello, ${HOSTNAME}, nice to meet you. ${PASSWORD}"
//                    echo "fab pwd -H ${HOSTNAME} --password=${PASSWORD}"
//                    sh "fab pwd -H ${HOSTNAME} --password=${PASSWORD}"
//             }
//         }
//     }
// }

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

//         stage('Make virtual environment and install requirements') {
//             steps {
//                 //sh 'python3 -m venv venv'
//                 //sh '. venv/bin/activate'
//                 //sh 'pip install -r requirements.txt'
// //
// //                 sh 'pip install fabric3'
//
//                 //sh 'pip3 install paramiko'
//
//             }
//         }

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
                   echo "Hello, ${HOSTNAME}, nice to meet you. ${PASSWORD}"
                   echo "fab pwd -H ${HOSTNAME} --password=${PASSWORD}"
                   sh "fab pwd -H ${HOSTNAME} --password=${PASSWORD}"
            }
        }
    }
}




// pipeline {
//     agent any
//     stages {
//         stage('Check Path') {
//             steps {
//                 echo 'Check Path..'
//                 sh 'pwd'
//             }
//         }
//         stage('Create virtual environment') {
//             steps {
//                 echo 'Create virtual environment..'
//                 sh 'python3 -m venv venv'
//             }
//         }
//         stage('Activate virtual environment') {
//             steps {
//                 echo 'Activate virtual environment..'
//                 sh '. venv/bin/activate'
//             }
//         }
//         stage('Install Flask') {
//             steps {
//                 echo 'Install Flask..'
//                 sh 'pip install Flask'
//             }
//         }
//         stage('Run Test file 1') {
//             steps {
//                 echo 'Run Test App file..'
//                 sh 'python test.py'
//             }
//         }
//         stage('Run Pytest file ') {
//             steps {
//                 echo 'Run Pytest file..'
//                 //sh 'pytest -v --tb=no'
//                 sh 'pytest -v --tb=no || [[ $? -eq 1 ]]'
//             }
//         }
//
//     }
// }
