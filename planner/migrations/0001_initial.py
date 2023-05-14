# Generated by Django 4.2.1 on 2023-05-13 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fazenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receita', models.IntegerField()),
                ('gasto_previsto', models.IntegerField()),
                ('data_receita_inicial', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('custo', models.IntegerField()),
                ('categoria', models.CharField(max_length=30)),
                ('feito', models.BooleanField(default=False)),
                ('fazenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.fazenda')),
                ('tarefa_dependente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='planner.tarefa')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('quantidade', models.IntegerField()),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.tarefa')),
            ],
        ),
    ]
