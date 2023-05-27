# Generated by Django 4.2 on 2023-05-26 00:32

import apps.agendas.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(help_text='Insira uma data para agenda', validators=[apps.agendas.models.Agenda.validar_dia])),
                ('horario', models.CharField(choices=[('1', '07:00 ás 08:00'), ('2', '08:00 ás 09:00'), ('3', '09:00 ás 10:00'), ('4', '10:00 ás 11:00'), ('5', '11:00 ás 12:00')], max_length=10)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa')),
            ],
            options={
                'db_table': 'agenda',
            },
        ),
    ]
