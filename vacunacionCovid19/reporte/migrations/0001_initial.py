# Generated by Django 3.2.7 on 2021-09-15 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('vacunado', models.BooleanField(default=False)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id_vacuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('productor', models.CharField(max_length=40)),
                ('cuantas_dosis', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar_vacunacion', models.CharField(max_length=50)),
                ('fecha_vacunacion', models.DateField()),
                ('dosis', models.IntegerField()),
                ('lote_vacuna', models.CharField(max_length=10)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.persona')),
                ('vacuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporte.vacuna')),
            ],
        ),
    ]
