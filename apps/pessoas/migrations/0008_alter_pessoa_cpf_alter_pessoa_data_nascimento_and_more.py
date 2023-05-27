# Generated by Django 4.2 on 2023-05-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0007_alter_pessoa_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=14, null=True, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='registro_atualizado',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='registro_criado',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='rg',
            field=models.CharField(max_length=45, null=True, unique=True, verbose_name='RG'),
        ),
    ]