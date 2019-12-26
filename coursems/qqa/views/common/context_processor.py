from django.shortcuts import render

def navigation_bar(request):
    ret = {}
    try:
        if request.session['name']:
            ret['name'] = request.session['name']
    except KeyError:
        ret['name'] = 'None'
    return ret