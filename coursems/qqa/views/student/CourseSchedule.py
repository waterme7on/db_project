from django.http import HttpResponse
from qqa.models import Course

def index(request):
    return HttpResponse("Nothing")