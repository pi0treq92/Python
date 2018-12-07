from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

#utworzenie klasy umożliwiającej tworzenie nowych postów i ich edycji

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tytul = models.CharField(max_length = 500)
    text = models.TextField()
    data_utworzenia = models.DateTimeField(default=timezone.now)
    data_publikacji = models.DateTimeField(blank=True, null=True)


    #Metoda umożliwiająca po zatwierdzeniu publikacji godzina publikacji przyjmuje wartość now i zapisują ją
    def publish(self):
        self.data_publikacji = timezone.now()
        self.save()

    # metoda pozwalająca na zatwierdzanie komentarzy
    def zatwierdzone_komentarze(self):
        return self.komentarze.filter(approved=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.tytul

# umożliwiająca dodawanie komentarzy do postu - prawie taka sama jak klasa POST
class Komentarz(models.Model):
    post = models.ForeignKey('blog.Post', related_name = 'komentarze', on_delete=models.CASCADE)
    autor = models.CharField(max_length=500)
    text = models.TextField()
    data_utworzenia = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)


    def approve(self):
        self.approved = True
        self.save()

#metoda mówiaca stronie gdzie zwracać utworzone komentarze
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
