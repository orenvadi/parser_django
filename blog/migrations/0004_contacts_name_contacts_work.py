# Generated by Django 4.1 on 2022-10-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='work',
            field=models.CharField(max_length=40, null=True),
        ),
    ]