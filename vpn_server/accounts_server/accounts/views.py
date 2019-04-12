from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import subprocess
import os


def index(request):
    return render(request, 'index.html')


def profile_create(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    email = request.POST['email']

    echo_pipe = subprocess.Popen(['echo', os.environ['CA_PASS']], stdout=subprocess.PIPE)
    easyrsa_pipe = subprocess.Popen(['easyrsa', 'build-client-full', email, 'nopass'], stdin=echo_pipe.stdout)
    echo_pipe.stdout.close()
    result = easyrsa_pipe.communicate()[0]
    print(result)
    return redirect('/connect')
