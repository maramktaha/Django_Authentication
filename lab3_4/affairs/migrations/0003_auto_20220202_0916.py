# Generated by Django 2.2.12 on 2022-02-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0002_user_cpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='track',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
    ]