from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Film
from .forms import FilmForm, DodatkoweInfoForm
from django.contrib.auth.decorators import login_required



#WYŚWIETLANIE FILMU

def wszystkie_filmy(request):
   wszystkie = Film.objects.all()
   # wszystkie = []
   return render(request, 'filmy.html', {'filmy': wszystkie})

#DODAWANIE FILMU
@login_required
def nowy_film(request):
   form_film = FilmForm(request.POST or None, request.FILES or None)
   form_dodatkowe = DodatkoweInfoForm(request.POST or None)

   if all((form_film.is_valid(), form_dodatkowe.is_valid())):
      film = form_film.save(commit=False)
      dodatkowe = form_dodatkowe.save()
      film.dodatkowe = dodatkowe
      film.save()
      return redirect(wszystkie_filmy)

   return render(request, 'film_form.html', {'form': form_film, 'form_dodatkowe': form_dodatkowe, 'nowy': True})

#EDYTOWANIE FILMU
@login_required
def edytuj_film(request, id):
   film = get_object_or_404(Film, pk=id)
   form = FilmForm(request.POST or None, request.FILES or None, instance=film)

   if form.is_valid():
      form.save()
      return redirect(wszystkie_filmy)

   return render(request, 'film_form.html', {'form': form, 'nowy': False})

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