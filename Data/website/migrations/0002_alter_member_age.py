# Generated by Django 5.0.6 on 2024-10-05 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(),
        ),
    ]
