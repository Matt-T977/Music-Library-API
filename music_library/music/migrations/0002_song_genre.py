# Generated by Django 3.2.7 on 2021-10-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default='music', max_length=50),
            preserve_default=False,
        ),
    ]
