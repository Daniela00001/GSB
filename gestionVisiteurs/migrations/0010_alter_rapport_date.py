# Generated by Django 5.0.3 on 2024-04-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionVisiteurs', '0009_alter_rapport_date_alter_rapport_medecin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapport',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]