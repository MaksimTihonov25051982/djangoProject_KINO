# Generated by Django 5.0.3 on 2024-04-27 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoisk', '0004_modelprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelkino',
            name='otziv',
        ),
        migrations.AddField(
            model_name='modelotziv',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kinopoisk.modelkino', verbose_name='Кино'),
        ),
    ]
