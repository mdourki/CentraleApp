# Generated by Django 3.2.5 on 2021-08-27 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20210826_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='depot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.depot'),
            preserve_default=False,
        ),
    ]
