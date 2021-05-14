# Generated by Django 3.1.3 on 2021-04-16 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasktrackerapp', '0003_remove_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasktrackerapp.user'),
            preserve_default=False,
        ),
    ]
