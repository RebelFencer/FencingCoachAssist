from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required



#WYŚWIETLANIE FILMU

def wszystkie_filmy(request):
   wszystkie = Film.objects.all()
   # wszystkie = []
   return render(request, 'filmy.html', {'filmy': wszystkie})

#DODAWANIE FILMU
@login_required
def nowy_film(request):
   form = FilmForm(request.POST or None, request.FILES or None)

   if form.is_valid():
      form.save()
      return redirect(wszystkie_filmy)

   return render(request, 'film_form.html', {'form': form})

#EDYTOWANIE FILMU
@login_required
def edytuj_film(request, id):
   film = get_object_or_404(Film, pk=id)
   form = FilmForm(request.POST or None, request.FILES or None, instance=film)

   if form.is_valid():
      form.save()
      return redirect(wszystkie_filmy)

   return render(request, 'film_form.html', {'form': form})

#USUWANIE FILMU
@login_required
def usun_film(request, id):
   film = get_object_or_404(Film, pk=id)

   if request.method == "POST":
      film.delete()
      return redirect(wszystkie_filmy)

   return render(request, 'potwierdz.html', {'film': film})


# Create
# Read - all, filter, get
# Upgrade
# Delete

   # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
   # test = "To jest cos we views"
   # return render(request, 'filmy.html', {'text':test}) - statyczne
   # return render(request, 'filmy.html', {'filmy': ["Avatar", "Titanic"]}) - bardziej dynamiczne, ale wciąż statyczne
# Create your views here.