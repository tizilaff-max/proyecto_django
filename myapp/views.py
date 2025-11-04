from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'mensaje': " Bienvenidos a mi app"}
    return render(request, "myapp/index.html", context)

#cuando creo una web, me salta request y lo responde con un html.