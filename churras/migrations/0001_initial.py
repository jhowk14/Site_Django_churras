# Generated by Django 4.1 on 2022-09-01 23:58

import churras.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prato', models.CharField(max_length=100)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('date_prato', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('foto_prato', models.ImageField(blank=True, upload_to=churras.models.get_file_path)),
                ('publicado', models.BooleanField(default=False)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa')),
            ],
        ),
    ]
