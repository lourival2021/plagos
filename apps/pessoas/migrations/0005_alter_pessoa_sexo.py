# Generated by Django 4.2 on 2023-05-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_alter_pessoa_convenio_alter_pessoa_especialidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Sexo'),
        ),
    ]
