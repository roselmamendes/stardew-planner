# Generated by Django 4.2.1 on 2023-05-13 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_tarefa_tarefa_dependente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='tarefa_dependente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='planner.tarefa'),
        ),
    ]
