# Generated by Django 3.2 on 2021-04-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0003_buspass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buspass',
            name='email',
        ),
        migrations.RemoveField(
            model_name='buspass',
            name='id',
        ),
        migrations.AddField(
            model_name='buspass',
            name='userID',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]
