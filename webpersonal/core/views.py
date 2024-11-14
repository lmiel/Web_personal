from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")

def about(request):
    return HttpResponse("""<h1>Mi Web Personal</h1>
    <h2>Acerca de</h2>
    <p>Me llamo Héctor y me encanta Django!</p>
    """)
