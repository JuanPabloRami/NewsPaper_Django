# Generated by Django 4.0.6 on 2022-08-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_alter_noticias_imgnoticia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('idAd', models.BigAutoField(primary_key=True, serialize=False)),
                ('imgAd', models.ImageField(null=True, upload_to='publicidad')),
                ('placement', models.CharField(max_length=10)),
            ],
        ),
    ]