from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    cree_par = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evenements')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre