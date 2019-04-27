from os import environ
from os.path import basename
from os import remove
import glob
from time import sleep
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formatdate


def message(to: str) -> MIMEMultipart:
    """Generate email message object"""
   
    subject = 'VPN Profile Changed'
    body = """Server's global ip has changed.
The attached file is new VPN profile."""

    mail = MIMEMultipart()
    mail['Subject'] = subject
    mail['From'] = environ['EMAIL_HOST_USER']
    mail['To'] = to
    mail.attach(MIMEText(body))

    # attach file
    path = f"/code/profiles/{to}.ovpn"
    with open(path, 'rb') as f:
        profile = MIMEApplication(f.read(), Name=basename(path))
    profile['Content-Disposition'] = f'attachment; filename={to}.ovpn'
    mail.attach(profile)

    return mail
   

def sendmail(mail: MIMEMultipart):
    """Send email"""
   
    server = smtplib.SMTP(host=environ['EMAIL_HOST'], port=environ['EMAIL_PORT'])
    server.starttls()
    server.login(user=environ['EMAIL_HOST_USER'], password=environ['EMAIL_HOST_PASSWORD'])
    server.send_message(mail)
    server.quit()


def userlist() -> list:
    """Return user email list"""
    _userlist = []

    filelist = glob.glob('/code/profiles/*')
    for file in filelist:
        filename = file.split('/')[-1]
        if filename.split('.')[-1] == 'ovpn':
            _userlist.append('.'.join(filename.split('.')[:-1]))
    
    return _userlist

if __name__ == "__main__":
    while True:
        sleep(10)
        BEFORE_IP = environ['GLOBAL_IP']
        NOW_IP = subprocess.check_output(['curl', '-s', 'globalip.me']).decode('utf-8')[:-1]

        if BEFORE_IP != NOW_IP:
            print(f'IP has been changed! {BEFORE_IP} to {NOW_IP}')
            environ['GLOBAL_IP'] = NOW_IP
            
            users = userlist()
            for user in users:
                # Rewrite profiles
                profile_name = f'/code/profiles/{user}.ovpn'
                old_content = ''
                with open(profile_name, 'r') as f:
                    old_content = f.read()

                remove(profile_name)          
                new_content = old_content.replace(BEFORE_IP, NOW_IP)
                with open(profile_name, 'w+') as f:
                    f.write(new_content)
            
                # Send profiles to users
                mail = message(to=user)
                sendmail(mail=mail)


        


