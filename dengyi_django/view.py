from  django.http import HttpResponse

def hello(req):
    return HttpResponse("<h1>hello world<h1>")