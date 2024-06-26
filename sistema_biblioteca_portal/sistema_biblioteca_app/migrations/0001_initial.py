# Generated by Django 4.2.11 on 2024-05-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lectores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('curso', models.CharField(max_length=200)),
                ('correo', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
