# Generated by Django 5.0.3 on 2024-04-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionVisiteurs', '0005_medecin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nomCommercial', models.CharField(max_length=100)),
                ('composition', models.CharField(blank=True, max_length=255, null=True)),
                ('effets', models.CharField(max_length=20)),
                ('contreIndications', models.CharField(blank=True, max_length=255, null=True)),
                ('quantite', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='rapport',
            old_name='composition',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='contreIndications',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='effets',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='libelle',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='nomCommercial',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='quantite',
        ),
    ]
