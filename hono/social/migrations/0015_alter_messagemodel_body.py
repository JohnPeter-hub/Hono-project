# Generated by Django 3.2.4 on 2021-07-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_alter_messagemodel_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='body',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
