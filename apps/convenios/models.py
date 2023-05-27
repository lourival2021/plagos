from django.contrib.auth.models import User
from django.db import models

class Convenio(models.Model):
    cd_convenio = models.CharField(verbose_name="Convenio", max_length=45)
    descricao = models.CharField(verbose_name="Descrição", max_length=45)
    registro_atualizado = models.DateTimeField(auto_now=True)
    registro_criado = models.DateTimeField(auto_now_add=True)
    pessoa = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.cd_convenio

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'convenio'