# Generated by Django 2.1 on 2019-03-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20190310_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='profile', to='profiles.SkillModel'),
        ),
    ]
