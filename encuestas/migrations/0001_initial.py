# Generated by Django 4.0.6 on 2022-07-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('idNoticia', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('imgNoticia', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100))
            ],
        ),
    ]
