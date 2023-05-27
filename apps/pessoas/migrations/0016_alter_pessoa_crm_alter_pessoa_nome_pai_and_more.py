# Generated by Django 4.2 on 2023-05-26 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0015_alter_pessoa_crm_alter_pessoa_nome_pai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='crm',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='CRM'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome_pai',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Nome do Pai'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='rg',
            field=models.CharField(blank=True, max_length=45, null=True, unique=True, verbose_name='RG'),
        ),
    ]