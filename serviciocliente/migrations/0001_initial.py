# Generated by Django 3.2.7 on 2021-11-19 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='soporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PQR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=64)),
                ('info', models.TextField()),
                ('created', models.DateField()),
                ('soport_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='serviciocliente.soporte')),
            ],
        ),
    ]
