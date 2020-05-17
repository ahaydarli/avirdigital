# Generated by Django 3.0.6 on 2020-05-17 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='portfolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Portfolio'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(max_length=255, upload_to='partners'),
        ),
    ]