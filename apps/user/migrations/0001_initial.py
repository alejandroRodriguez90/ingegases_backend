# Generated by Django 5.1.7 on 2025-03-19 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'rol',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=55)),
                ('correo', models.CharField(max_length=99)),
                ('contrasena', models.CharField(max_length=8)),
                ('usuario', models.CharField(max_length=55)),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.rol')),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
