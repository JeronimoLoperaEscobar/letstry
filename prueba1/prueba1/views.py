from django.http import HttpRequest,HttpResponse

def hola(request):
    return HttpResponse("hola mundo")