# Generated by Django 4.1.7 on 2023-03-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaApp', '0006_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='AutoTienda/media'),
        ),
    ]
