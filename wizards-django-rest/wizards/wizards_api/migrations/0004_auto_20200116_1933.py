# Generated by Django 3.0.2 on 2020-01-16 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizards_api', '0003_spell_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='learnt_in',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='wizards_api.Subject'),
        ),
    ]
