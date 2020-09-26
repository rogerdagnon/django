# Generated by Django 3.0.3 on 2020-09-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=264, unique=True)),
                ('email', models.EmailField(max_length=264, unique=True)),
                ('texto', models.CharField(max_length=264, unique=True)),
                ('endereco', models.CharField(max_length=264, unique=True)),
                ('cidade', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
