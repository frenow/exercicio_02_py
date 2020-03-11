# Generated by Django 3.0.4 on 2020-03-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=60)),
                ('numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=15)),
                ('cidade', models.CharField(max_length=60)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='data_nacimento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(null=True),
        ),
    ]