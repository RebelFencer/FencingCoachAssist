from django.urls import path
from szermierka.views import wszystkie_filmy


urlpatterns = [
    path('wszystkie/', wszystkie_filmy)
]