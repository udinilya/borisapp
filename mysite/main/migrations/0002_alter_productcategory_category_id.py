# Generated by Django 4.0.2 on 2022-02-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='category_id',
            field=models.IntegerField(verbose_name='id категории'),
        ),
    ]
