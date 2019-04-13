from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.core.mail import BadHeaderError, EmailMessage
import subprocess
import os

PROFILES_DIR = '/code/profiles'


def index(request):
    return render(request, 'index.html')


def profile_create(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    email = request.POST['email']

    if not os.path.exists(f'{PROFILES_DIR}/{email}.ovpn'):
        # Generate Profile
        echo_pipe = subprocess.Popen(['echo', os.environ['CA_PASS']], stdout=subprocess.PIPE)
        easyrsa_pipe = subprocess.Popen(['easyrsa', 'build-client-full', email, 'nopass'], stdin=echo_pipe.stdout)
        echo_pipe.stdout.close()
        result = easyrsa_pipe.communicate()[0]
        print(result)

        # Save profile
        content = subprocess.check_output(['ovpn_getclient', email])

        with open(f'{PROFILES_DIR}/{email}.ovpn', 'w') as profile:
            profile.write(content.decode())

    # Send email
    subject = 'VPN Profile'
    message = 'The attached file is OpenVPN profile you requested.'
    from_email = os.environ['EMAIL_HOST_USER']
    recipient_list = [email, ]
    with open(f'{PROFILES_DIR}/{email}.ovpn', 'r') as profile:
        m = EmailMessage(subject, message, from_email=from_email, to=recipient_list)
        m.attach(f'{email}.ovpn', profile.read(), 'text/plain')
        m.send()

    return redirect('/connect')


def connect(request):
    return render(request, 'connect.html')
