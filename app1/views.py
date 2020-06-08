from django.http import HttpResponse

def hello(request):
    message="Hello world"
    return HttpResponse(message)
