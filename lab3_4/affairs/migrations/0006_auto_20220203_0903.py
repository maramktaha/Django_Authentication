# Generated by Django 2.2.12 on 2022-02-03 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0005_track_trainee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='intake',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='affairs.Intake'),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='affairs.Track'),
        ),
    ]
