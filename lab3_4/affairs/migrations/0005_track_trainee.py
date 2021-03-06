# Generated by Django 2.2.12 on 2022-02-03 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0004_auto_20220202_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('bdate', models.DateField()),
                ('promotion', models.DecimalField(decimal_places=1, max_digits=5)),
                ('intake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affairs.Intake')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affairs.Track')),
            ],
        ),
    ]
