# Generated by Django 3.0.8 on 2020-07-29 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicaments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personnes',
            name='nom',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='personnes',
            name='prenom',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Recuperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('quantite', models.IntegerField(max_length=10)),
                ('Medicaments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdc.Medicaments')),
                ('Personnes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdc.Personnes')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bacth_id', models.FloatField()),
                ('quantite', models.IntegerField(max_length=10)),
                ('Livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdc.Livraison')),
                ('Medicaments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdc.Medicaments')),
            ],
        ),
    ]
