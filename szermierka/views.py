from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm




def wszystkie_filmy(request):
   wszystkie = Film.objects.all()
   # wszystkie = []
   return render(request, 'filmy.html', {'filmy': wszystkie})

def nowy_film(request):
   form = FilmForm(request.POST or None, request.FILES or None)

   if form.is_valid():
      form.save()
   return render(request, 'nowy_film.html', {'form': form})


# Create
# Read - all, filter, get
# Upgrade
# Delete

   # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
   # test = "To jest cos we views"
   # return render(request, 'filmy.html', {'text':test}) - statyczne
   # return render(request, 'filmy.html', {'filmy': ["Avatar", "Titanic"]}) - bardziej dynamiczne, ale wciąż statyczne
# Create your views here.