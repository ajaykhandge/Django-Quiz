# Generated by Django 3.0 on 2020-09-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200829_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='quiz_status',
            field=models.BooleanField(default=False),
        ),
    ]
