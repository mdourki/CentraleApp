# Generated by Django 3.2.6 on 2021-08-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_fournisseur_page_accueil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fournisseur',
            name='page_accueil',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
