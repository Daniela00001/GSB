# Generated by Django 5.0.3 on 2024-04-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionVisiteurs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]