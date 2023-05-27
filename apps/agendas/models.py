from datetime import date
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import ForeignKey
from apps.pessoas.models import Pessoa
from plagos import settings

class Agenda(models.Model):

    def validar_dia(value):
        today = date.today()
        weekday = date.fromisoformat(f'{value}').weekday()

        if value < today:
            raise ValidationError('Não é possivel escolher um data atrasada.')
        if (weekday == 5) or (weekday == 6):
            raise ValidationError('Escolha um dia útil da semana.')

    profissional = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    dia = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])

    HORARIOS = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)
    pessoa = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('horario', 'dia')

    class Meta:
        db_table = 'agenda'

    def __str__(self):
        return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.pessoa}'