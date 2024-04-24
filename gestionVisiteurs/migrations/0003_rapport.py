# Generated by Django 5.0.3 on 2024-04-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionVisiteurs', '0002_alter_utilisateur_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motif', models.CharField(max_length=100)),
                ('bilan', models.CharField(max_length=100)),
                ('nomCommercial', models.CharField(max_length=100)),
                ('composition', models.CharField(max_length=100)),
                ('effets', models.CharField(max_length=100)),
                ('contreIndications', models.CharField(max_length=100)),
                ('libelle', models.CharField(max_length=100)),
                ('quantite', models.CharField(max_length=100)),
            ],
        ),
    ]