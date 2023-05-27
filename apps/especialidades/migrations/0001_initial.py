# Generated by Django 4.2 on 2023-05-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd', models.CharField(max_length=45, verbose_name='Cd')),
                ('descricao', models.CharField(max_length=45, verbose_name='Descricao')),
                ('registro_atualizado', models.DateTimeField(auto_now=True)),
                ('registro_criado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'especialidade',
            },
        ),
    ]