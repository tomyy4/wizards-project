# Generated by Django 3.0.2 on 2020-01-16 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizards_api', '0002_auto_20200115_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spell_name', models.CharField(max_length=50)),
                ('learnt_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_id', to='wizards_api.Subject')),
            ],
        ),
    ]
