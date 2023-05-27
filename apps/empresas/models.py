from django.urls import reverse
from django.db import models

class Empresa(models.Model):
    cnpj = models.CharField(verbose_name="CNPJ", max_length=45)

    def __str__(self):
        return self.cnpj

    class Meta:
        db_table = 'empresa'

    def get_absolute_url(self):
        return reverse('home')
