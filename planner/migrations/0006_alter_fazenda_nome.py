# Generated by Django 4.2.1 on 2023-05-13 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_fazenda_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fazenda',
            name='nome',
            field=models.CharField(default='Sem nome', max_length=20),
        ),
    ]