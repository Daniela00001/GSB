# Generated by Django 5.0.3 on 2024-04-22 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionVisiteurs', '0008_remove_medicament_quantite_rapport_quantite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapport',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='medecin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionVisiteurs.medecin'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='medicament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionVisiteurs.medicament'),
        ),
    ]