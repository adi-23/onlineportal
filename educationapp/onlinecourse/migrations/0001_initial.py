# Generated by Django 3.1.7 on 2022-06-22 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('educator', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
