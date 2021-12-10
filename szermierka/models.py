from django.db import models

class DodatkoweInfo(models.Model):
   GATUNEK = {
      (0,'Inne'),
      (1,'Horror'),
      (2,'Komedia'),
      (3,'Sci-Fi'),
      (4,'Drama')
   }

   czas_trwania = models.PositiveSmallIntegerField(default=0)
   gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)

# Create your models here.
class Film(models.Model):
   tytul = models.CharField(max_length=64, blank=False, unique=True)
   rok = models.PositiveSmallIntegerField(default=2000)
   opis = models.TextField(default="")
   premiera = models.DateField(null=True, blank=True)
   imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
   plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
   dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
      return self.tytul_z_rokiem()

   def tytul_z_rokiem(self):
      return "{} ({})".format(self.tytul, self.rok)

class Ocena(models.Model):
   recenzja = models.TextField(default="", blank=True)
   gwiazdki = models.PositiveSmallIntegerField(default=5)
   film = models.ForeignKey(Film, on_delete=models.CASCADE) #many to one

class Aktor(models.Model):
   imie = models.CharField(max_length=32)
   nazwisko = models.CharField(max_length=32)
   filmy = models.ManyToManyField(Film)



# class Student(models.Model):
#     number = models.AutoField(max_length=9999)
#     name = models.CharField(max_length=256, blank=False)
#     surname = models.CharField(max_length=256, blank=False)
#     data = models.DateTimeField(auto_now=False, auto_now_add=True)
#
# class Answer(models.IntegerChoices):
#     M = 0, _('Mężczyzna')
#     K = 1, _('Kobieta')
#     Inny = models.CharField(max_length=256, blank=False) #zastosować tutaj jeśli się wybierze inny możliwość wpisania
#     __empty__ = _('(Unknown)')


