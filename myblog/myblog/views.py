from django.shortcuts import render_to_response


def home(requests):
    return render_to_response('home.html', {})
