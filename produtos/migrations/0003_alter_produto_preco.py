# Generated by Django 4.1 on 2023-12-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.IntegerField(),
        ),
    ]