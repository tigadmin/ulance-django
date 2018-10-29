# Generated by Django 2.1 on 2018-10-26 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20181026_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationmodel',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.MajorModel'),
        ),
        migrations.AlterField(
            model_name='educationmodel',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.SchoolModel'),
        ),
    ]
