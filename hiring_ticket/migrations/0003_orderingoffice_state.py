# Generated by Django 2.2 on 2019-04-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring_ticket', '0002_auto_20190411_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderingoffice',
            name='state',
            field=models.CharField(default='ca', max_length=80),
            preserve_default=False,
        ),
    ]
