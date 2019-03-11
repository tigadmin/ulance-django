# Generated by Django 2.1 on 2019-03-10 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='levelmodel',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='levelmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='skillmodel',
            name='is_parent',
            field=models.BooleanField(default=False, verbose_name='is a parent category'),
        ),
        migrations.AddField(
            model_name='skillmodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='profiles.SkillModel'),
        ),
        migrations.DeleteModel(
            name='LevelModel',
        ),
    ]
