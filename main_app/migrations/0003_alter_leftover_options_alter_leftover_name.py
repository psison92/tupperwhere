# Generated by Django 4.1 on 2022-08-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_leftover_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leftover',
            options={'ordering': ['expiration']},
        ),
        migrations.AlterField(
            model_name='leftover',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
