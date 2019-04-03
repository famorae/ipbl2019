# Generated by Django 2.0.2 on 2019-04-03 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principio_ativo', models.CharField(max_length=120)),
                ('descricao', models.CharField(max_length=120)),
                ('grau_risco', models.IntegerField()),
            ],
            options={
                'db_table': 'alergia',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=120)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
                ('tipo_sanguineo', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
        migrations.CreateModel(
            name='PacienteTemAlergia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consulta_id', models.IntegerField()),
                ('alergia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Alergia')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Paciente')),
            ],
            options={
                'db_table': 'paciente_tem_alergia',
            },
        ),
        migrations.CreateModel(
            name='QuadroClinico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
                ('imc', models.CharField(max_length=120)),
                ('fuma', models.BooleanField()),
                ('fuma_frequencia', models.CharField(max_length=120)),
                ('bebe', models.BooleanField()),
                ('bebe_frequencia', models.CharField(max_length=120)),
                ('pratica_atividade', models.BooleanField()),
                ('pratica_frequencia', models.CharField(max_length=120)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Paciente')),
            ],
            options={
                'db_table': 'quadro_clinico',
            },
        ),
    ]
