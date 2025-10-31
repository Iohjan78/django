from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>conexion con backend funciona!!</h1>")