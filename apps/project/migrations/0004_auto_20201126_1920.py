# Generated by Django 3.1.3 on 2020-11-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
