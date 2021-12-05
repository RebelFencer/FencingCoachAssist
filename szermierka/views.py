from django.shortcuts import render
from django.http import HttpResponse
from .models import Film




def wszystkie_filmy(request):
   wszystkie = Film.objects.all()
   return render(request, 'filmy.html', {'filmy': wszystkie})



   # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
   # test = "To jest cos we views"
   # return render(request, 'filmy.html', {'text':test}) - statyczne
   # return render(request, 'filmy.html', {'filmy': ["Avatar", "Titanic"]}) - bardziej dynamiczne, ale wciąż statyczne
# Create your views here.