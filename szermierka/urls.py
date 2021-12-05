from django.urls import path
from szermierka.views import wszystkie_filmy, nowy_film


urlpatterns = [
    path('wszystkie/', wszystkie_filmy),
    path('nowy/', nowy_film)

]