# Generated by Django 3.1.4 on 2020-12-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafico',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]