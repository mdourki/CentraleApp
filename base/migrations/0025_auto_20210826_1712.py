# Generated by Django 3.2.5 on 2021-08-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_produit_code_barre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='Code_Produit',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='produit',
            name='Nom',
            field=models.CharField(max_length=50),
        ),
    ]
