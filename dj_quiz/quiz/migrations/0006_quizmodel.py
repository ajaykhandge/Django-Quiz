# Generated by Django 3.0 on 2020-08-23 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0005_useranswermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_quiz_name', models.CharField(choices=[('COC', 'Clash of Codes'), ('WEBER', 'Weber'), ('HOTKEYS', 'Hotkeys')], default='COC', max_length=100)),
                ('quiz_no_questions', models.PositiveIntegerField(default=30)),
                ('user_quiz_attempted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
