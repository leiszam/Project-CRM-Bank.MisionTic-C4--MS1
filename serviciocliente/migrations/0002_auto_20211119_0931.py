# Generated by Django 3.2.7 on 2021-11-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciocliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soporte',
            name='address',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='soporte',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]