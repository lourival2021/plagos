# Generated by Django 4.2 on 2023-05-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=45, verbose_name='CNPJ')),
            ],
            options={
                'db_table': 'empresa',
            },
        ),
    ]