from __future__ import with_statement
from fabric.api import local, settings, abort, run, get
from fabric.contrib.console import confirm



def pwd():
    run("pwd")


# /home/rutujaharidas/PycharmProjects/jenkins_3/Pytest_Cron_job

def run_backup_script():
    #result = run("chmod +x /home/rutujaharidas/PycharmProjects/jenkins_3/Pytest_Cron_job/db_backup_script.sh")
    run('crontab -l > /tmp/crondump')
    run(
        'echo "3 * * * * /home/rutujaharidas/PycharmProjects/jenkins_3/Pytest_Cron_job/db_backup_script.sh" >> /tmp/crondump')
    run('crontab /tmp/crondump')
