# Generated by Django 4.0 on 2021-12-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ime', models.CharField(max_length=30)),
                ('student_prezime', models.CharField(max_length=30)),
                ('student_jmbag', models.CharField(max_length=10)),
            ],
        ),
    ]
