# Generated by Django 4.0.4 on 2022-04-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='contact_number',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default=None, max_length=128),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default=None, max_length=32),
        ),
    ]
