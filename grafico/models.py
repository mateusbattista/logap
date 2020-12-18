from django.db import models

# Create your models here.


class Grafico(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    coo_x = models.TextField()
    coo_y = models.TextField()

    def __str__(self):
        return self.nome
