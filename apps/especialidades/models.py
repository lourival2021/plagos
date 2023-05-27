from django.db import models

class Especialidade(models.Model):
    cd = models.CharField(verbose_name="Cd", max_length=45)
    descricao = models.CharField(verbose_name="Descricao", max_length=45)
    registro_atualizado = models.DateTimeField(auto_now=True)
    registro_criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cd

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'especialidade'