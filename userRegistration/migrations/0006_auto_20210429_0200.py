# Generated by Django 3.2 on 2021-04-28 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0005_auto_20210429_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buspass',
            name='id',
        ),
        migrations.AddField(
            model_name='buspass',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userRegistration.userinfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buspass',
            name='userID',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]